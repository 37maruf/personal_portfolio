from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm
from .models import Education, Experience, Profile, Project, SkillCategory


def home(request):
    return render(request, "portfolio/home.html", {
        "projects": Project.objects.all()[:3],
        "categories": SkillCategory.objects.prefetch_related("skills")[:6],
    })


def about(request):
    return render(request, "portfolio/about.html")


def education(request):
    return render(request, "portfolio/education.html", {"items": Education.objects.all()})


def experience(request):
    return render(request, "portfolio/experience.html", {"items": Experience.objects.all()})


def skills(request):
    return render(request, "portfolio/skills.html", {
        "categories": SkillCategory.objects.prefetch_related("skills"),
    })


def projects(request):
    return render(request, "portfolio/projects.html", {"projects": Project.objects.all()})


def project_detail(request, pk):
    return render(request, "portfolio/project_detail.html", {"p": get_object_or_404(Project, pk=pk)})


def resume(request):
    """Shows the CV on the page. Add ?download=1 to download it."""
    profile = Profile.objects.first()
    has_cv = bool(profile and profile.cv)
    if request.GET.get("download"):
        if not has_cv:
            raise Http404("No CV uploaded yet.")
        return FileResponse(profile.cv.open("rb"), as_attachment=True,
                            filename="Md_Maruf_Khan_CV.pdf", content_type="application/pdf")
    return render(request, "portfolio/resume.html", {"has_cv": has_cv})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = form.save()
            _notify_owner(msg)
            messages.success(request, "Thanks! Your message was sent. I will reply soon.")
            return redirect("portfolio:contact")
        messages.error(request, "Your message was not sent. Please fix the highlighted fields.")
    else:
        form = ContactForm()
    return render(request, "portfolio/contact.html", {"form": form})


def _notify_owner(msg):
    """Email the owner a copy. Never break the page if email fails."""
    profile = Profile.objects.first()
    if not profile or not settings.EMAIL_HOST_USER:
        return
    try:
        send_mail(
            subject=f"[Portfolio] {msg.subject}",
            message=f"From: {msg.name} <{msg.email}>\n\n{msg.message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[profile.email],
            fail_silently=True,
        )
    except Exception:
        pass
