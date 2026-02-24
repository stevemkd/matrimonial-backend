from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import (
    RegisterView,
    LoginView,
    ProfileViewSet,
    MatchViewSet,
    FavoriteViewSet,
)


router = DefaultRouter()
router.register('profiles', ProfileViewSet, basename='profile')
router.register('matches', MatchViewSet, basename='match')
router.register('favorites', FavoriteViewSet, basename='favorite')


urlpatterns = [
    # Auth
    path('auth/register/', RegisterView.as_view(), name='auth-register'),
    path('auth/login/', LoginView.as_view(), name='auth-login'),
    # Optional: DRF built-in token login
    path('auth/token-login/', obtain_auth_token, name='auth-token-login'),

    # API resources
    path('', include(router.urls)),
]

