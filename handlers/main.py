from django.http import HttpResponse
from django.shortcuts import render_to_response
def index(*args, **kwargs):
    return render_to_response('papers.html')