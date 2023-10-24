from django.contrib import admin

from.models import *


class SpotlightAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)

admin.site.register(Spotlight, SpotlightAdmin)


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'text','image',)

admin.site.register(SocialMedia, SocialMediaAdmin)