from django.shortcuts import render

from encyclopedia import util


def index(request, title):
    return render(request, "titles/index.html", {
        "title": title })
