from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('project/<slug:project_slug>/',views.projects,name="projects"),
    path('blogs/<slug:blog_slug>/',views.blogs,name="blogs"),
    path('certificate/',views.certificate,name="certificate")
]
