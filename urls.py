from django.conf.urls.defaults import *

urlpatterns = patterns('', 
    (r'^$', 'handlers.main.index'),
    (r'^submit$', 'handlers.add_paper.add'),
    (r'^papers/(\d+)/', 'handlers.paperhandler.view'),
    (r'^new$', 'handlers.main.new'),
    )