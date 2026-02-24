from django.contrib import admin

from .models import Profile, Match, Favorite


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'age',
        'location',
        'religion',
        'caste',
        'premium',
        'verified',
    )
    list_filter = ('premium', 'verified', 'religion', 'caste')
    search_fields = ('full_name', 'location', 'profession')


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile', 'match_percentage', 'created_at')
    list_filter = ('match_percentage',)


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile', 'created_at')

