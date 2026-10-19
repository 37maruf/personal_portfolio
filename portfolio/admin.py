from django.contrib import admin
from django.utils.html import format_html

from .models import (ContactMessage, Education, Experience, Profile, Project,
                     Skill, SkillCategory)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "has_cv")
    fieldsets = (
        ("Basic info", {"fields": ("full_name", "tagline", "typed_roles", "photo")}),
        ("About", {"fields": ("bio", "interests", "career_goal")}),
        ("Resume", {"fields": ("cv",)}),
        ("Contact and social links", {"fields": (
            "email", "phone", "whatsapp_number", "facebook_url", "github_url", "linkedin_url")}),
    )

    @admin.display(boolean=True, description="CV uploaded")
    def has_cv(self, obj):
        return bool(obj.cv)

    def has_add_permission(self, request):
        # Only one profile is needed
        return not Profile.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("level", "institution", "year", "result", "order")
    list_editable = ("order",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "period", "order")
    list_editable = ("order",)


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 3


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "icon", "skill_names", "order")
    list_editable = ("order",)
    inlines = [SkillInline]

    @admin.display(description="Skills")
    def skill_names(self, obj):
        return ", ".join(s.name for s in obj.skills.all())


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "technologies", "has_live", "order")
    list_editable = ("order",)
    search_fields = ("title", "technologies")

    @admin.display(boolean=True, description="Live link")
    def has_live(self, obj):
        return bool(obj.live_url)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "subject", "email", "created_at", "is_read")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("name", "email", "subject", "message", "created_at")
    actions = ["mark_read", "mark_unread"]

    def has_add_permission(self, request):
        return False

    @admin.action(description="Mark selected messages as read")
    def mark_read(self, request, queryset):
        queryset.update(is_read=True)

    @admin.action(description="Mark selected messages as unread")
    def mark_unread(self, request, queryset):
        queryset.update(is_read=False)
