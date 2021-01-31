from django.urls import path

from . import views

app_name = "search"
# search bar will always look like search/result
urlpatterns = [
    path("result", views.searchDataDefault, name="index")
]