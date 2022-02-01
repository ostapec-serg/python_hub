from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect





import re
import requests

import sqlite3

from django.urls import reverse

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
    content_to_write = {}
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
    id_list = create_list_id(story_name)

    for result in id_list:
        try:
            to_write = save_data(result)
            story_model = story_name_model_map[story_name]
            story = story_model(**to_write)
            story.save()
        except IntegrityError:
            pass
    return HttpResponse(f"{story_name} scraped")
    # return HttpResponseRedirect(reverse('scrap:main'))
