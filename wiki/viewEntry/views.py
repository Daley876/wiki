from django.shortcuts import render
from encyclopedia import util
from django.contrib import messages
from django.http import HttpResponseRedirect
import markdown2
# Create your views here.

# get this template by tping to into url directly
def titleData(request):
        return render(request, "viewEntry/index.html"
                      )

#same argument name here should be the same from url file
def titleData(request, entryName):
        if (util.get_entry(entryName)):
            titles = markdown2.markdown(util.get_entry(entryName))
            return render(request, "viewEntry/index.html",
                      {"data": titles,"entryName":entryName} # we pass multiple components to page by separating with comma
                      )
        else:
            return render(request, "viewEntry/index.html",{"entryName":entryName}
                          )


