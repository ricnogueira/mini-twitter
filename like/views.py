from rest_framework import viewsets
from .models import Like
from .serializers import LikeSerializer
from .permissions import LikeOwnerOrDenyAll


class LikeModelViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [LikeOwnerOrDenyAll]
