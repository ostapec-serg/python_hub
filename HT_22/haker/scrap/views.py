from django.shortcuts import render
from django.http import HttpResponse

from .models import StoryCategory
from .tasks import scrap_category


def main(request):
    category_list = StoryCategory.objects.all().order_by('category')
    context = []
    for category in category_list:
        context.append(category.category)
    return render(request, 'scrap/index.html', {'context': context})


def scrap(request):
    if request.POST:
        story_name = request.POST['story_name']
        scrap_category.delay(story_name)
        massage = {"massage": f"Scrap '{story_name}' category in background progress"}
        return render(request, 'scrap/success_scrap.html', massage)
    else:
        return HttpResponse("Ooops, something go wrong")
