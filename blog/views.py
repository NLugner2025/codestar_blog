from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def my_blog(request):
    return HttpResponse("Hello, Blog!", content_type="text/plain")
template_name = "blog/index.html"
paginate_by = 6