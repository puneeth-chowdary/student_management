from django.urls import path
from . import views
urlpatterns=[
    path('',views.display,name='display'),
    path('registered',views.second,name='registered'),
    path('delk',views.delk,name='delk'),
    path('search',views.search,name="search")
]