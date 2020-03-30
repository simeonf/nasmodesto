from django.contrib import admin

from video import models

@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'author', 'title', 'date', 'youtube_link')

    
@admin.register(models.Klass)
class KlassAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
