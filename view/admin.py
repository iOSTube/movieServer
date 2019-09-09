from django.contrib import admin
from .models import Video

class viewAdmin(admin.ModelAdmin):
    list_display = ['name', 'videofile', 'updated']

admin.site.register(Video, viewAdmin)