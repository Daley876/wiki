from django.urls import path

from . import views

app_name = "viewEntry"
urlpatterns = [
    path("", views.titleData, name="viewEntries"),
    path("<str:entryName>", views.givenTitleData, name="viewEntries")
]