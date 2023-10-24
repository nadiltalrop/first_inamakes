from django.urls import path

from. import views


app_name = 'travelapp'
urlpatterns = [
    path('', views.index, name='index'),
]
