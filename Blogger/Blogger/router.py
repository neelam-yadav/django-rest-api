'''
Created on Mar 13, 2015

@author: Neelam Yadav
'''

from rest_framework.routers import SimpleRouter, DefaultRouter

class SharedAPIRootRouter(SimpleRouter):
    shared_router = DefaultRouter()

    def register(self, *args, **kwargs):
        self.shared_router.register(*args, **kwargs)
        super(SharedAPIRootRouter, self).register(*args, **kwargs)
