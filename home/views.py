from django.shortcuts import render,get_object_or_404
from . models import Projectinfo,Blogs,BlogSection

def home(request):
    projectinfo = Projectinfo.objects.all()
    bloginfo = Blogs.objects.all()
    pi={
        "pi":projectinfo,
        "bloginfo":bloginfo,
    }
    return render(request,"index.html",pi)

def projects(request,project_id):
    project = get_object_or_404(Projectinfo,id=project_id)
    print(project.image1)
    return render(request,'projects.html',{"project":project})

def blogs(request,blog_id):
    blogs = get_object_or_404(Blogs,id=blog_id)
    sections = blogs.sections.all()
    return render(request,'blogs.html',{"blogs":blogs, 'sections': sections})

def certificate(request):
    
    return render(request,'certificate.html')