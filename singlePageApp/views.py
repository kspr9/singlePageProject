from django.shortcuts import render
from django.http import Http404, HttpResponse

# Create your views here.
def index(request):
    return render(request, "singlePageApp/index.html")

texts = ["This is page 1","This is page 2","This is page 3"]

def section(request, num):
    if num <= num <= 3:
        return HttpResponse(texts[num-1])
    else:
        raise Http404("No such section")

