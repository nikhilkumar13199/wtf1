from django.urls import path

from . import views
app_name='museo'
urlpatterns = [
    path('', views.index, name='index'),
]