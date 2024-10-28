""" from django.urls import path
from . import views

urlpatterns = [
    path("post/", views.PostCreateListView.as_view(), name="post-list"),
    path("post/<int:pk>/", views.PostRetrieveUpdateDestroyView.as_view(), name="post-detail-update-delete"),
]
 """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("post", views.PostModelViewSet, basename="post")

urlpatterns = [
    path("", include(router.urls)),
]
