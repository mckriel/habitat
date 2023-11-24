from django.shortcuts import render
from .models import ArtistLineup


def base_layout(request):
    template = 'habitat_pwa/base.html'

    lineup_list = ArtistLineup.objects.filter(day_of_week=0)
    print(lineup_list)
    context = {
        "lineup_list": lineup_list
    }

    return render(request, template, context)
