from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import ArtistLineup
from .forms import DaySelector


def index(request):
    # day_selector = DaySelector()
    # running = True
    template = 'habitat_pwa/index.html'

    return render(request, template)

    # while running:
    #     if request.method == 'POST':
    #         day_selector = DaySelector(request.POST)
    #         print(request.POST['day'])
    #         selected_day = request.POST['day']
    #         day_selector.day = selected_day
    #         lineup_list = ArtistLineup.objects.filter()
    #         print(lineup_list)
    #         context = {
    #             "lineup_list": lineup_list,
    #             'day_selector': day_selector,
    #         }
    #         return render(request, template, context)
    #
    #     else:
    #         lineup_list = ArtistLineup.objects.filter()
    #         print(lineup_list)
    #         context = {
    #             "lineup_list": lineup_list,
    #             'day_selector': day_selector,
    #         }
    #         return render(request, template, context)


def getdata(request):
    results = ArtistLineup.objects.all()
    jsondata = serializers.serialize('json', results)
    return HttpResponse(jsondata)


def base_layout(request):
    template = 'habitat_pwa/base.html'
    return render(request, template)


def page_map(request):
    template = 'habitat_pwa/map.html'
    return render(request, template)


def page_directions(request):
    template = 'habitat_pwa/directions.html'
    return render(request, template)
