
from django.shortcuts import render_to_response

from models import Paper

import logging
import util

def view(request, id):
    
    #Paper.sample_init()
    
    """Handler for individual papers"""
    paper = Paper.get_by_id(int(id))
    values = {
        "paper": paper,
        "paper_date":util.as_time_ago(paper.date),
        "paper_html_description" : util.plaintext2html(paper.description),
    }
    return render_to_response('paper.html', values)
