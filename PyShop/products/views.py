from django.http import HttpResponse 

def index(request):
    return HttpResponse("Hello, world. You're at the products index.")


def new(request):
    return HttpResponse("Hello, world. You're at the products index.")
