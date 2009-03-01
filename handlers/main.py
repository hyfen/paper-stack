from django.http import HttpResponse
from django.shortcuts import render_to_response

from models import Paper

def index(request):
    papers = Paper.all()
    papers.order('-date')
    papers = papers.fetch(1000)
    
    def paper_compare(a, b):
        return b.score() - a.score()
    
    papers.sort(paper_compare)
        
    return render_to_response('papers.html', {"papers": papers[:30]})
    
def new(request):
    papers = Paper.all()
    papers.order('-date')
    papers = papers.fetch(30)
    
    return render_to_response('papers.html', {"papers": papers})