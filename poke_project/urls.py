from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt import views as jwt_views

from .views import CustomizeTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('v1.urls')),
    path('login', CustomizeTokenObtainPairView.as_view(), name='login'),
    path('refresh_token', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
