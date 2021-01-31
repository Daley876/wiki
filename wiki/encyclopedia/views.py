from django.shortcuts import render
from django import forms

from . import util
from . import urls



def index(request):
    return render(request, "encyclopedia/index.html",
                  {"entries": util.list_entries()}
                  )
