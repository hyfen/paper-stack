from google.appengine.ext import db
#from google.appengine.api import users

import random
import logging


class Paper(db.Model):
    title = db.StringProperty(required=True, multiline=False)
    description = db.TextProperty()
    tags = db.StringListProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    
    # reference for future properties
    #creator = db.UserProperty()
    #author(s).. = db.ReferenceProperty(Hat)
    
    points = db.IntegerProperty(default=0)
    # TODO: points should track who gave points so each user can only add one point 
    
    link = db.LinkProperty() # for fully qualified links
    pdf_link = db.LinkProperty()
    # Links aren't required.  We support linking to papers or just discussing
    # them or some part of them submitted via the description.
    
    #To be auto-filled:
    #name = db.StringProperty()
    #abstract = db.TextProperty()
    #references = ..?
    #keywords = db.StringListProperty()
    #authors = ...? (add Author model?)

    
    def permalink(self):
        return "/papers/%(id)s/" % {'id' : self.key().id()}

    @classmethod
    def get_random(cls):
        papers = Paper.all().fetch(1000)
        if not papers:
            logging.info('random paper returning None')
            return None
        else:
            return random.choice(papers)


def init():
    logging.info('initializing db')
    
    # nothing to do yet..

        
        
        
        
        