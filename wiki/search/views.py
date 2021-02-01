from django.shortcuts import render
from encyclopedia import util
from encyclopedia import views
import viewEntry
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
import markdown2
import re


# Create your views here.

def searchDataDefault(request):
# checks to see if form has been submitted

    if request.method == "POST":
# please not this method of getting data was implemented because a HTML form was used
        res = request.POST['q'] # this is how we save data from HTML form
        conv_res = str(res) #converts data from form into a string variable

        #stores existing a titles in a local list for easy manipulation
        list_of_tiles = util.list_entries()
        tracked_titles = []

    # this loop scans through the list of titles and compares it to the data from form(the search bar)
    # both strings are changed to upper case to make for easy comparisons
        for title in list_of_tiles:
            if re.search(conv_res.upper(),title.upper()):
          # when pattern match is found, we append that a second list we created
                tracked_titles.append(title)

        if len(tracked_titles) == 1:
           #stores found title in a new variable
            found_title = tracked_titles[0]

            # the below redirects to viewEntry page based on title typed in search bar.
            # the format for the reverse arguments are "app_name:app_nickame". these are taken from url file
            # if the url is expects an input/argument (like the case below) then "args" is used to send that over
            return HttpResponseRedirect(reverse('viewEntry:viewEntries', args=[found_title]))

        elif len(tracked_titles) >= 2:
            return render(request, "search/results.html",{"found_entries": tracked_titles,
                                                          "entries": util.list_entries()})

        # this else clause is for scenarios where no pattern match is found
        else:
            return render(request, "search/results.html",{"entries": util.list_entries(),
                                                          "found_entries": tracked_titles})
    else:
        return render(request, "search/results.html",{"entries": util.list_entries(),
                                                      "found_entries": tracked_titles})