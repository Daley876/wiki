from django.shortcuts import render

from . import util
from . import urls

def index(request):
    return render(request, "encyclopedia/index.html",
                  {"entries": util.list_entries()}
                  )
