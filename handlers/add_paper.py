from forms.new_paper import NewPaperForm
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from models import Paper

from django.core.urlresolvers import reverse




def add(request):
    """Add action"""

    form = None

    if request.method == "POST":
        form = NewPaperForm(request.POST)

        if form.is_valid():
            if hasattr(form.cleaned_data['tags'], 'split'):
                form.cleaned_data['tags'] = form.cleaned_data['tags'].split(",")
            

            p = Paper(**form.cleaned_data)
            p.put()
            return HttpResponseRedirect(p.permalink())
        else:
            pass
    elif request.method == "GET":
        form = NewPaperForm()
    else:
        pass
        
    return render_to_response('add_paper.html', 
        {"form" : form,
         "dest_url" : reverse(__name__+'.add')
         })