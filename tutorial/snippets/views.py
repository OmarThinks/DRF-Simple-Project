from .models import Snippet
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import SnippetSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

