'''
Created on Mar 12, 2015

@author: Neelam Yadav
'''

from rest_framework import serializers

from .models import Blog


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializes Blog model into its representation
    """

    class Meta:
        model = Blog
        fields = ('url', 'author', 'title', 'description', 'body')
