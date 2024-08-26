from django.contrib import admin
from .models import Projectinfo,Blogs,BlogSection

admin.site.register(Projectinfo)
admin.site.register(Blogs)
admin.site.register(BlogSection)

class BlogSectionInline(admin.StackedInline):  # Or admin.StackedInline for a different layout
    model = BlogSection
    extra = 1  # Number of empty sections to display by default in the admin form

class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogSectionInline]