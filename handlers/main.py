from django.http import HttpResponse

def index(*args, **kwargs):
    return HttpResponse("Hello, world.")