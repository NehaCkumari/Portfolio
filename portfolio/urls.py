from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("conn",views.conn,name="conn"),
    
]'''
from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^email/$',
        views.email,
        name='email'
        ),
    url(r'^thanks/$',
        views.thanks,
        name='thanks'
        ),
)'''