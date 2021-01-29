from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from encyclopedia import util


# remember to reference class form in the html where it is needed.
class newTitleForm(forms.Form):
    newTitle = forms.CharField(label="Title Name")
    newTitleDesc = forms.CharField(label="Title Description")


def index(request):
    if request.method == "POST":
        form = newTitleForm(request.POST)
        if form.is_valid():
            for entry in util.list_entries():
                if entry form.newTitle:
                    return render(request, "newEntry/index.html",
                                  {"form": form})
                else:
                    util.save_entry(form.newTitle, form.newTitleDesc)
                    return render(request, "newEntry/index.html", {"form": newTitleForm})
        else:
            return render(request, "newEntry/index.html",
                          {"form": form})

    return render(request, "newEntry/index.html", {"form": newTitleForm})
