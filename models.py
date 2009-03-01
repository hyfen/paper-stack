from google.appengine.ext import db
#from google.appengine.api import users

import random
import logging


class Paper(db.Model):
    title = db.StringProperty(required=True, multiline=False)
    description = db.TextProperty()
    
    tags = db.StringListProperty()
    def spaced_tags(self, spacer=', '):
        return spacer.join(self.tags)
    
    date = db.DateTimeProperty(auto_now_add=True)
    
    # reference for future properties
    #creator = db.UserProperty()
    #author(s).. = db.ReferenceProperty(Hat)
    
    points = db.IntegerProperty(default=0)
    # TODO: points should track who gave points so each user can only add one point 
    # eg. a Point model w/ references to Paper & User objects
    
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

    @classmethod  
    def sample_init(debug=False):
        import datetime
        import time
        import string

        fp = open('english_dict.txt')
        words = fp.read().split('\n')

        def strTimeProp(start, end, format, prop):
            # from http://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates
            stime = time.mktime(time.strptime(start, format))
            etime = time.mktime(time.strptime(end, format))

            ptime = stime + prop * (etime - stime)

            return datetime.datetime.fromtimestamp(ptime)#.localtime(ptime))

        def randomDate(start, end, prop):
            return strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop)

        def random_text(min, max, sentences=False, join=' '):
            txt = ""
            tlen = random.randint(min, max)
            for x in range(tlen):
                txt += random.choice(words)
                if sentences and random.randint(0,25) == 0:
                    txt += '.  '
                else:
                    txt += join
    
            if sentences:
                txt += '.'
            return txt 

        def add_paper():#title, desc, tags, date, points, link="", pdf_link=""):
            title = string.capwords(random_text(5,12))
            desc = string.capwords(random_text(0,100,True), sep='.  ')
            tags = filter(lambda x: x, random_text(0,8).split(' '))
            date = randomDate("1/1/2009 1:30 PM", "2/28/2009 6:45 PM", random.random())
            points = random.randint(0,500)
    
            link = None
            if random.randint(0,10) < 8:
                link = 'http://'+random_text(1,1,join='')+'.com/'+random_text(0,5,join='/')
    
            pdf_link = None
            if random.randint(0,4) == 0:
                pdf_link = 'http://'+random_text(1,1,join='')+'.com/'+random_text(0,5,join='/')+random_text(1,1,join='')+'.pdf'
    
            if debug:
              print "%s\n%s\n%s\n%s\n%s\n%s\n%s\n" % (title, desc, tags, date, points, link, pdf_link)
    
            p = Paper(title=title, description=desc, tags=tags, date=date, 
                      points=points, link=link, pdf_link=pdf_link)
            p.put()

        for i in range(random.randint(5,30)):
            add_paper()






def init():
    logging.info('initializing db')
    
    # nothing to do yet..

        
        
        
        
        