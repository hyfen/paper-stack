from google.appengine.ext.db import djangoforms
from models import Paper

class NewPaperForm(djangoforms.ModelForm):
    """Form to add a new paper to the site."""
    
    class Meta:
        model = Paper
        exclude = ['points']