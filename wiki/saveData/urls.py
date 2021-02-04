from django.urls import path

from . import views

app_name = "saveData"
urlpatterns = [path("<str:titleName>", views.savePage, name="save"),
               path("", views.savePage, name="save")]