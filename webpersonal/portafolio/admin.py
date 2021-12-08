from django.contrib import admin
from .models import Project
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    ReadOnly_fields = ('created','updated')

admin.site.register(Project, ProjectAdmin)
