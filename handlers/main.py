from django.http import HttpResponse
from django.shortcuts import render_to_response

from models import Paper

def index(request):
    return render_to_response('papers.html', {"papers": Paper.all()})