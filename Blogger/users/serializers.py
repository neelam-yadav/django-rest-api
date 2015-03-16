'''
Created on Mar 12, 2015

@author: Neelam Yadav
'''

from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email')

