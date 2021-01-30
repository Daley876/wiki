from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.contrib import messages
from encyclopedia import util


# remember to reference class form in the html where it is needed.
class newTitleForm(forms.Form):
    newTitle = forms.CharField(label="Title Name")
    newTitleDesc = forms.CharField(label="Title Description")


def index(request):
    if request.method == "POST":
        form = newTitleForm(request.POST)
        if form.is_valid():

# data entered in form must be cleaned before it is used in code
            newTitle=form.cleaned_data["newTitle"]
            newTitleDesc= form.cleaned_data["newTitleDesc"]

            if util.get_entry(newTitle):
                messages.error(request, "This title already exists.")
                return render(request, "newEntry/index.html", {"form": form})


            else:
                util.save_entry(newTitle, newTitleDesc)
                messages.success(request, "New title has been added successfully.")
                return render(request, "newEntry/index.html", {"form": newTitleForm})

        else:
            return render(request, "newEntry/index.html",
                          {"form": form})

    return render(request, "newEntry/index.html", {"form": newTitleForm})
