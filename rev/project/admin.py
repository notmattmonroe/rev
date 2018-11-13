from rev.project.models import Project,ProjectType
from django.contrib import admin


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectType)
