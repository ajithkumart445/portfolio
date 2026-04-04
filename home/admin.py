from django.contrib import admin
from .models import Projectinfo, ProjectSection, Blogs, BlogSection, Certification

class ProjectSectionInline(admin.StackedInline):
    model = ProjectSection
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectSectionInline]
    prepopulated_fields = {'project_slug': ('project_name',)}

class BlogSectionInline(admin.StackedInline):
    model = BlogSection
    extra = 1

class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogSectionInline]
    prepopulated_fields = {'blog_slug': ('blog_title',)}

admin.site.register(Projectinfo, ProjectAdmin)
admin.site.register(Blogs, BlogAdmin)
admin.site.register(Certification)