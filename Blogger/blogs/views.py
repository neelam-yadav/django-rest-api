from .models import Blog
from rest_framework import viewsets
from .serializers import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

