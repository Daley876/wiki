from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
from encyclopedia import util
from editPage import views  # import form from editPage app
from django.contrib import messages


# Create your views here.


def savePage(request, titleName):
    if request.method == 'POST':
        form = views.modifyEntryForm(request.POST)
        # data entered in form must be cleaned before it is used in code
        if form.is_valid():
            entryDetails = form.cleaned_data["entryDetails"]
            print(entryDetails)
            util.save_entry(titleName, entryDetails)

            return HttpResponseRedirect(reverse('viewEntry:viewEntries', args=[titleName]))
        else:
            messages.error(request, "Change to entry content has failed. Updates were not saved")
            return HttpResponseRedirect(reverse('viewEntry:viewEntries', args=[titleName]))
