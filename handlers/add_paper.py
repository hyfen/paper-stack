from forms.new_paper import NewPaperForm
from django.shortcuts import render_to_response


def add(request):
    """Add action"""
    return render_to_response('add_paper.html', {"form" : NewPaperForm()})