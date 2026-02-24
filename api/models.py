from django.conf import settings
from django.db import models


class Profile(models.Model):
    """
    Matrimony profile with fields similar to the React Native mock data.
    """

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profiles',
        null=True,
        blank=True,
        help_text='Owner account for this profile (optional).',
    )
    full_name = models.CharField(max_length=120)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    age = models.PositiveIntegerField()
    height = models.CharField(max_length=20, blank=True)
    education = models.CharField(max_length=120, blank=True)
    profession = models.CharField(max_length=120, blank=True)
    location = models.CharField(max_length=200, blank=True)
    religion = models.CharField(max_length=80, blank=True)
    caste = models.CharField(max_length=80, blank=True)
    image_url = models.URLField(blank=True)
    verified = models.BooleanField(default=False)
    premium = models.BooleanField(default=False)
    bio = models.TextField(blank=True)
    interests = models.JSONField(default=list, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-premium', '-verified', 'full_name']

    def __str__(self):
        return self.full_name


class Match(models.Model):
    """
    Represents a match between the current user and a profile,
    with a match percentage similar to the app UI.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='matches',
    )
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='matched_with',
    )
    match_percentage = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'profile')
        ordering = ['-match_percentage', '-created_at']

    def __str__(self):
        return f'{self.user} ↔ {self.profile} ({self.match_percentage}%)'


class Favorite(models.Model):
    """
    User's favorite / shortlisted profiles.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='favorites',
    )
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='favorited_by',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'profile')
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user} ❤ {self.profile}'

