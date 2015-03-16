'''
Created on Mar 13, 2015

@author: Neelam Yadav
'''

from django.conf.urls import patterns, url, include
from Blogger.router import SharedAPIRootRouter
from users import views

router = SharedAPIRootRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
