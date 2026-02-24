from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Profile, Match, Favorite


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):
    owner = UserSerializer(source='user', read_only=True)

    class Meta:
        model = Profile
        fields = [
            'id',
            'owner',
            'full_name',
            'gender',
            'age',
            'height',
            'education',
            'profession',
            'location',
            'religion',
            'caste',
            'image_url',
            'verified',
            'premium',
            'bio',
            'interests',
            'created_at',
            'updated_at',
        ]


class MatchSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    profile_id = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all(),
        write_only=True,
        source='profile',
    )

    class Meta:
        model = Match
        fields = [
            'id',
            'profile',
            'profile_id',
            'match_percentage',
            'created_at',
        ]


class FavoriteSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    profile_id = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all(),
        write_only=True,
        source='profile',
    )

    class Meta:
        model = Favorite
        fields = [
            'id',
            'profile',
            'profile_id',
            'created_at',
        ]

