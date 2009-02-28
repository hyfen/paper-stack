from google.appengine.ext import db
#from google.appengine.api import users

import random
import logging


class Paper(db.Model):
    title = db.StringProperty(multiline=False)
    description = db.TextProperty()
    tags = db.StringListProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    
    # reference for future properties
    #creator = db.UserProperty()
    #author(s).. = db.ReferenceProperty(Hat)

    
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

        
        
        
        
        