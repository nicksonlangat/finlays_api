from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .import views

router = DefaultRouter()
router.register(r'signup', views.SignUpUserView)

urlpatterns = [
    path('login/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('current/user', views.UserAPIView.as_view(), name='current_user'),
] + router.urls
