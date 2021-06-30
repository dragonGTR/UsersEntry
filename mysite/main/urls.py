from django.urls import path

from . import views

urlpatterns = [
    path('main', views.index, name="index"),
    path('allUser', views.display_user, name="index2")
]
