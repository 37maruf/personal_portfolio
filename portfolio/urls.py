from django.urls import path

from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("education/", views.education, name="education"),
    path("experience/", views.experience, name="experience"),
    path("skills/", views.skills, name="skills"),
    path("projects/", views.projects, name="projects"),
    path("projects/<int:pk>/", views.project_detail, name="project_detail"),
    path("resume/", views.resume, name="resume"),
    path("contact/", views.contact, name="contact"),
]
