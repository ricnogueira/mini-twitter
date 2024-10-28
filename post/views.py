from rest_framework import generics, viewsets, permissions
from .models import Post
from .serializers import PostSerializer
from .permissions import PostOwnerOrDenyAll


"""
class PostCreateListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
"""


class PostModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.DjangoModelPermissions, PostOwnerOrDenyAll]  # A ORDEM AQUI IMPORTA. SEQUE PRIMEIRO AS PERMISSOES DO DJANGO E DEPOIS A PERSONALIZADA
