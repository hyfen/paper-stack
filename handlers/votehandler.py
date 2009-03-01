
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from django.core.urlresolvers import reverse

from models import Paper

import logging
import util

# TODO: no redirects, do AJAX voting w/ POST
def vote(request, id):
    paper = Paper.get_by_id(int(id))
    if request.method == 'GET':
        paper.points += 1
        paper.put()
    return HttpResponseRedirect(paper.permalink())