from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from encyclopedia import util
import markdown2


#  textarea will act as form
class modifyEntryForm(forms.Form):
    # style:resize:none ensures the text area's size is constant
    entryDetails = forms.CharField(widget=forms.Textarea(attrs={'style': 'resize:none'}))


def viewPageToChange(request, titleName):
    # initializes form textarea with current entry content
    form = modifyEntryForm(initial={"entryDetails": util.get_entry(titleName)})
    return render(request, "editPage/index.html", {"form": form, "entryName": titleName})
