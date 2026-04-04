from django.db import models
import datetime
import os
from django.urls import reverse

def GetFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)

class Projectinfo(models.Model):
    project_name = models.CharField(max_length=150)
    project_slug = models.SlugField(max_length=150, unique=True, null=True, blank=True) # SEO friendly URL
    project_description = models.CharField(max_length=500)
    overview = models.TextField(blank=True, null=True)
    challenges = models.TextField(blank=True, null=True)
    results = models.TextField(blank=True, null=True)
    technologies_used = models.CharField(max_length=225)
    role = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to=GetFileName, null=True, blank=True)
    start_timeline = models.DateField()
    end_timeline = models.DateField(null=True, blank=True) # Allow current projects
    post_date = models.DateTimeField(auto_now_add=True)
    project_link = models.CharField(max_length=255, blank=True, null=True)
    github_link = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):  
        return self.project_name

    def get_absolute_url(self):
        return reverse('projects', kwargs={'project_slug': self.project_slug})

class ProjectSection(models.Model):
    SECTION_TYPES = [
        ('feature', 'Key Feature'),
        ('gallery', 'Gallery Image'),
        ('other', 'Other'),
    ]
    project = models.ForeignKey(Projectinfo, related_name='sections', on_delete=models.CASCADE)
    section_type = models.CharField(max_length=20, choices=SECTION_TYPES, default='feature')
    heading = models.CharField(max_length=100, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to=GetFileName, null=True, blank=True)
    order = models.IntegerField(default=0) # To maintain story flow

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.project.project_name} - {self.get_section_type_display()} - {self.heading}"

class Blogs(models.Model):
    blog_title = models.CharField(max_length=150)
    blog_slug = models.SlugField(max_length=150, unique=True, null=True, blank=True) # SEO friendly URL
    thumbnail = models.ImageField(upload_to=GetFileName, null=True, blank=True)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_title

    def get_absolute_url(self):
        return reverse('blogs', kwargs={'blog_slug': self.blog_slug})
    
class BlogSection(models.Model):
    blog = models.ForeignKey(Blogs, related_name='sections', on_delete=models.CASCADE)
    subheading = models.CharField(max_length=150, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to=GetFileName, null=True, blank=True)
    order = models.IntegerField(default=0) # To maintain story flow

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.blog.blog_title} - {self.subheading}"

class Certification(models.Model):
    name = models.CharField(max_length=150)
    issuer = models.CharField(max_length=150)
    date_earned = models.DateField()
    credential_id = models.CharField(max_length=100, blank=True, null=True)
    credential_url = models.URLField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to=GetFileName, null=True, blank=True)

    def __str__(self):
        return f"{self.name} by {self.issuer}"