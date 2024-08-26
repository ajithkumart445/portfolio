from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('projects/<int:project_id>/',views.projects,name="projects"),
    path('blogs/<int:blog_id>/',views.blogs,name="blogs"),
    path('certificate/',views.certificate,name="certificate")
]
