from django.contrib import admin
from .models import MusicType, Music, Ads, Profile
# Register your models here.

class MusicAdmin(admin.ModelAdmin):
    list_display = ('name', 'music', 'musicType')

class AdsAdmin(admin.ModelAdmin):
    list_display = ('name', 'music')

class ProfileInline(admin.StackedInline):
    model = Ads

class ProfileAdmin(admin.ModelAdmin):
    filter_horizontal = ['musicType']
    inlines = [ProfileInline]

admin.site.register(Music, MusicAdmin)
admin.site.register(MusicType)
admin.site.register(Ads, AdsAdmin)
admin.site.register(Profile, ProfileAdmin)