from django.urls import path
from .views import UserRegisterView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"users", UserRegisterView, basename="auth_user")

# urlpatterns = router.urls

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="user-register"),
    path("unregister/", UserRegisterView.as_view(), name="user-unregister"),
]
