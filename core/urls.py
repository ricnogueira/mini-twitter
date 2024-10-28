"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenBlacklistView


urlpatterns = [
    # path('', admin.site.urls),
    path('admin/', admin.site.urls),
    path('api/v1/', include('post.urls')),
    path('api/v1/', include('user.urls')),
    # path('api/v1/', include('like.urls')),
    # path('api/v1/', include('follow.urls')),
    path('api/v1/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
]
