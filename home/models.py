from django.db import models
import datetime
import os

def GetFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)

class Projectinfo(models.Model):
    project_name = models.CharField(max_length=50)
    project_description = models.CharField(max_length=225)
    technologies_used = models.CharField(max_length=225)
    role = models.CharField(max_length=50)
    challenges = models.TextField()
    results_learnings = models.TextField()
    start_timeline = models.DateField()
    end_timeline = models.DateField()
    post_date = models.DateTimeField(auto_now_add=True)
    project_link = models.CharField(max_length=255)
    image1=models.ImageField(upload_to=GetFileName,null=True,blank=True) 
    image2=models.ImageField(upload_to=GetFileName,null=True,blank=True)
    image3=models.ImageField(upload_to=GetFileName,null=True,blank=True)

    def __str__(self):  
        return self.project_name

class Blogs(models.Model):
    blog_title = models.CharField(max_length=50)
    image_1 = models.ImageField( upload_to = GetFileName, null=True, blank=True )
    image_2 = models.ImageField(upload_to = GetFileName, null=True, blank=True) 
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.blog_title
    
class BlogSection(models.Model):
    blog = models.ForeignKey(Blogs, related_name='sections', on_delete=models.CASCADE)
    subheading = models.CharField(max_length=50)
    content = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.subheading} - {self.blog.blog_title}"