from django.urls import path

from . import views


urlpatterns = [
    path('', views.volah_home, name='volah_home'),
]

