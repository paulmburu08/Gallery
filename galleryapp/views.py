from django.shortcuts import render
from django.http import HttpResponse
from . models import Image

# Create your views here.

def landing_page(request):
    title = 'Photospace'

    return render(request, 'index.html', {'title':title})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})