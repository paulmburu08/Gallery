from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.core.exceptions import ObjectDoesNotExist
from . models import Image

# Create your views here.

def landing_page(request):
    title = 'Photospace'
    images = Image.objects.all()

    return render(request, 'index.html', {'title':title, 'images':images})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def image(request,id):

    try:
        image = Image.get_image_by_id(id)

    except ObjectDoesNotExist:
        raise Http404()

    return render(request, 'image.html',{'image':image})