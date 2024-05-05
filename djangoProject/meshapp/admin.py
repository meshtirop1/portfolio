from django.contrib import admin
from .models import Project, GalleryImage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'start_date', 'end_date', 'github_url')
    list_filter = ('status', 'start_date', 'end_date')
    search_fields = ('name', 'description')


admin.site.register(GalleryImage)
