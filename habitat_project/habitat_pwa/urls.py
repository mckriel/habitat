from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("base_layout", views.base_layout, name="base_layout"),
    path("map/", views.page_map, name="page_map"),
    path("directions/", views.page_directions, name="page_directions"),
    path("getdata", views.getdata, name='getdata'),
]
