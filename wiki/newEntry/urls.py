from django.urls import path
from . import views

app_name = "newEntry"
urlpatterns = [
    path("", views.index, name="index")
]