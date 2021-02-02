from django.shortcuts import render
from encyclopedia import util
from viewEntry import views
from django.urls import reverse
from django.http import HttpResponseRedirect
import random
# Create your views here.


def randomizedPage(request):
    title_names = util.list_entries()

    titleIndex = random.randint(0,len(title_names)-1)
    return HttpResponseRedirect(reverse('viewEntry:viewEntries', args=[title_names[titleIndex]]))
