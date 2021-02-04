from django.shortcuts import render
from encyclopedia import util
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
import markdown2


# Create your views here.

def titleData(request):
    return render(request, "viewEntry/index.html")


#  return HttpResponseRedirect(reverse('editPage:modify', args=[entryName]))
# same argument name here should be the same from url file

def givenTitleData(request, entryName):
    if util.get_entry(entryName):
        titles = markdown2.markdown(util.get_entry(entryName))
        return render(request, "viewEntry/index.html",

                      # we pass multiple components to page by separating with comma
                      {"data": titles, "entryName": entryName}
                      )

    else:
        return render(request, "viewEntry/index.html", {"entryName": entryName})
