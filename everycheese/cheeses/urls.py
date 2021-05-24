from django.urls import path
from django.views.generic.base import View
from .views import *

app_name = 'cheeses'
urlpatterns = [
    path(
        route='add/',
        view=CheeseCreateView.as_view(),
        name='add'
    ),
    path(
        route='',
        view=CheeseListView.as_view(),
        name='list'
    ),
    path(
        route='<slug:slug>/',
        view=CheeseDetailView.as_view(),
        name='detail'
    ),
]
