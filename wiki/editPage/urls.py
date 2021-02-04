from django.urls import path

from . import views

app_name = "editPage"
urlpatterns = [path("<str:titleName>", views.viewPageToChange, name="modify"),
               path("", views.viewPageToChange, name="modify")]
