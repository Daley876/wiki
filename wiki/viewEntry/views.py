from django.shortcuts import render
from encyclopedia import util
import markdown2
# Create your views here.

# get this template by tping to into url directly
def titleData(request):
     #   titles = markdown2.markdown(util.get_entry(title))
        return render(request, "viewEntry/index.html"
                      )
def titleData(request, title):
        titles = markdown2.markdown(util.get_entry(title))
        return render(request, "viewEntry/index.html",
        {"data": titles}
                      )


