from django.shortcuts import render
import time

from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, "posts/index.html")

def posts(request):
    # Get start and end points
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))

    # Generate list of posts
    data = []
    for i in range(start, end + 1):
        data.append(f"Post #{i}")

    # Artificially delay speed of response
    time.sleep(1)

    # Return list of posts e.g. http://127.0.0.1:8888/posts?start=1&end=25
    return JsonResponse({
        "posts": data
    })