from django.shortcuts import render, get_object_or_404
from .models import Projectinfo, Blogs, BlogSection, Certification

def home(request):
    projectinfo = Projectinfo.objects.all().order_by('-post_date')
    bloginfo = Blogs.objects.all().order_by('-post_date')
    certifications = Certification.objects.all().order_by('-date_earned')
    context = {
        "projects": projectinfo,
        "blogs": bloginfo,
        "certifications": certifications,
    }
    return render(request, "index.html", context)

def projects(request, project_slug):
    project = get_object_or_404(Projectinfo, project_slug=project_slug)
    features = project.sections.filter(section_type='feature')
    galleries = project.sections.filter(section_type='gallery')
    return render(request, 'projects.html', {"project": project, "features": features, "galleries": galleries})

def blogs(request, blog_slug):
    blog = get_object_or_404(Blogs, blog_slug=blog_slug)
    sections = blog.sections.all()
    return render(request, 'blogs.html', {"blog": blog, 'sections': sections})

def certificate(request):
    certifications = Certification.objects.all().order_by('-date_earned')
    return render(request, 'certificate.html', {"certifications": certifications})