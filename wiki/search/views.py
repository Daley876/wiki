from django.shortcuts import render
from encyclopedia import util
from encyclopedia import views
import viewEntry
from django import forms, http
import markdown2


# Create your views here.

def searchDataDefault(request):
# checks to see if form has been submitted

    if request.method == "POST":
#please not this method of getting data was implemented because a HTML form was used
        res = request.POST['q'] # this is how we save data from HTML form
        if util.get_entry(res):
            title = markdown2.markdown(util.get_entry(res)) #searches for entry and marksdown result returned
            return render(request, "search/results.html",
                          # we pass multiple components to page by separating with comma
                          {"data": title, "entryName": res,"entries": util.list_entries()}
                          )
        else:
            return render(request, "search/results.html",{"entries": util.list_entries()}
                      )

    else:
        return render(request, "search/results.html",{"entries": util.list_entries()}
                      )
