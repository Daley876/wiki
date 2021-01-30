from django.urls import path

from . import views

app_name = "titles"
urlpatterns = [
    path("<str:title>", views.index, name="index")
]
