from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponse

import re
import requests

from scrap import models
import html
from datetime import datetime


def main(request):
    context = {
        'news_story': ['askstories', 'showstories', 'newstories', 'jobstories'],
    }
    return render(request, 'scrap/index.html', context)


def create_list_id(topic):
    """
    Method makes a request to the hacker-news api.
    from the response generates a list of ids
    in accordance with the category selected by the user
    :return: list of story IDs for the selected category
    """
    url = f"https://hacker-news.firebaseio.com/v0/{topic}.json"
    response = requests.get(url)
    id_list = []
    for i_d in response.json():
        id_list.append(i_d)
    return id_list


def time_convert(time):
    """ Method convert timestamp to utc """
    utc_time = datetime.utcfromtimestamp(time).strftime('%Y-%m-%d  %H:%M')
    return utc_time


def clean_up_text(text):
    """ Convert all named and numeric character references
    in the string to the corresponding Unicode characters """
    clean_text = re.sub('<[^<]+?>', '', text)
    clean_text = html.unescape(clean_text)
    return clean_text


def save_data(i_d):
    """
    the method sends requests to the hacker-news api
    for all ids from the list(create_list_id).  query results
    are formed dictionary and sent for saving
    :param i_d: str
        id from list
    :return: dictionary with content to write
    """
    url = f"https://hacker-news.firebaseio.com/v0/item/{i_d}.json"
    response = requests.get(url)
    check = response.content
    if check is None:
        return None
    content_to_write = {}
    try:
        for key, val in response.json().items():
            if key == 'kids':
                val = str(val)
            elif key == 'id':
                content_to_write['id_story'] = val
                continue
            elif key == 'time':
                content_to_write[key] = time_convert(val)
                continue
            elif key == 'title' or key == 'text':
                content_to_write[key] = clean_up_text(val)
                continue
            content_to_write[key] = val
        return content_to_write
    except AttributeError:
        return None


def check_uniq(id_list, story_model):
    """
    the method checks if the id from the parsing list is unique.
    If the database has an entry with a specific id, then it is
    excluded from the list for parsing
    return: checked list for parsing or empty
        list if all ids are in the database
    """
    objects_list = story_model.objects.all()
    id_story_from_objects = []
    for element in objects_list:
        id_story_from_objects.append(element.id_story)
    if id_story_from_objects:
        checked_id_list = []
        for element in id_list:
            if element not in id_story_from_objects:
                checked_id_list.append(element)
        return checked_id_list
    return id_list


def get_data(request):
    """
    The method makes queries on the generated list of id
    numbers(method create_list_id) and saves it in the
    corresponding table column in the database
    """
    story_name = request.GET.get('story_name', '')
    story_name_model_map = {
        'askstories': models.Ask,
        'showstories': models.Show,
        'newstories': models.New,
        'jobstories': models.Job,
    }
    story_model = story_name_model_map[story_name]
    id_list = create_list_id(story_name)
    checked_id_list = check_uniq(id_list, story_model)
    if checked_id_list:
        for result in checked_id_list:
            try:
                to_write = save_data(result)
                if to_write is None:
                    continue
                story = story_model(**to_write)
                story.save()
            except IntegrityError:
                pass
        return HttpResponse(f"Category {story_name} scraped")
    return HttpResponse(f"Nothing to scrap in {story_name} category")
    # return HttpResponseRedirect(reverse('scrap:main'))
