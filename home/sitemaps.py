from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Projectinfo, Blogs

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return ['home', 'certificate']

    def location(self, item):
        return reverse(item)

class ProjectSitemap(Sitemap):
    priority = 0.9
    changefreq = 'weekly'

    def items(self):
        return Projectinfo.objects.all().order_by('-post_date')

    def lastmod(self, obj):
        return obj.post_date

class BlogSitemap(Sitemap):
    priority = 0.7
    changefreq = 'weekly'

    def items(self):
        return Blogs.objects.all().order_by('-post_date')

    def lastmod(self, obj):
        return obj.post_date
