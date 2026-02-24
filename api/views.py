from django.contrib.auth import authenticate
from rest_framework import generics, permissions, viewsets, mixins
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Profile, Match, Favorite
from .serializers import (
    UserSerializer,
    RegisterSerializer,
    ProfileSerializer,
    MatchSerializer,
    FavoriteSerializer,
)


class RegisterView(generics.CreateAPIView):
    """
    POST /api/auth/register/
    Body: { username, email, password }
    Returns: user + auth token
    """

    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        Token.objects.get_or_create(user=user)
        return user

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = self.get_queryset().filter(id=response.data['id']).first() if hasattr(self, 'get_queryset') else None
        if user is None:
            # Fallback: fetch by username
            from django.contrib.auth import get_user_model
            User = get_user_model()
            user = User.objects.filter(username=response.data['username']).first()
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {
                'user': response.data,
                'token': token.key,
            },
            status=response.status_code,
        )


class LoginView(generics.GenericAPIView):
    """
    POST /api/auth/login/
    Body: { username, password }
    Returns: user + auth token
    """

    serializer_class = RegisterSerializer  # reuse fields
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({'detail': 'Invalid credentials'}, status=400)
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {
                'user': UserSerializer(user).data,
                'token': token.key,
            }
        )


class ProfileViewSet(viewsets.ModelViewSet):
    """
    CRUD + list/search for profiles.
    - GET /api/profiles/             (list + filters)
    - POST /api/profiles/            (create, auth required)
    - GET /api/profiles/{id}/
    - PATCH/PUT/DELETE /api/profiles/{id}/ (owner only)
    """

    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        qs = Profile.objects.all()
        # Basic filters mapped to React Native search filters
        age_min = self.request.query_params.get('age_min')
        age_max = self.request.query_params.get('age_max')
        location = self.request.query_params.get('location')
        education = self.request.query_params.get('education')
        profession = self.request.query_params.get('profession')
        religion = self.request.query_params.get('religion')
        caste = self.request.query_params.get('caste')
        q = self.request.query_params.get('q')

        if age_min:
            qs = qs.filter(age__gte=age_min)
        if age_max:
            qs = qs.filter(age__lte=age_max)
        if location:
            qs = qs.filter(location__icontains=location)
        if education:
            qs = qs.filter(education__icontains=education)
        if profession:
            qs = qs.filter(profession__icontains=profession)
        if religion:
            qs = qs.filter(religion__icontains=religion)
        if caste:
            qs = qs.filter(caste__icontains=caste)
        if q:
            qs = qs.filter(
                models.Q(full_name__icontains=q)
                | models.Q(location__icontains=q)
                | models.Q(profession__icontains=q)
            )

        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MatchViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    """
    Matches for the logged-in user.
    - GET /api/matches/
    - POST /api/matches/ { profile_id, match_percentage }
    """

    serializer_class = MatchSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Match.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FavoriteViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    """
    Favorites (shortlisted profiles) of the logged-in user.
    - GET /api/favorites/
    - POST /api/favorites/ { profile_id }
    - DELETE /api/favorites/{id}/
    """

    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

