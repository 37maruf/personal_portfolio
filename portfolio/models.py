from django.core.validators import FileExtensionValidator
from django.db import models


class Profile(models.Model):
    """Your personal details. Only one row is needed."""
    full_name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=150, help_text="Short line under your name")
    typed_roles = models.CharField(
        max_length=300, blank=True,
        help_text="Roles that type out on the home page, separated by commas",
    )
    bio = models.TextField(help_text="About you. Press Enter twice for a new paragraph.")
    interests = models.TextField(blank=True, help_text="One interest per line")
    career_goal = models.TextField(blank=True)
    photo = models.ImageField(
        upload_to="profile/", blank=True,
        help_text="Leave empty to use the default photo that comes with the project",
    )
    cv = models.FileField(
        upload_to="cv/", blank=True,
        validators=[FileExtensionValidator(["pdf"])],
        help_text="Upload your CV as a PDF",
    )
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    facebook_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    whatsapp_number = models.CharField(
        max_length=20, blank=True, help_text="With country code, like 8801700921553"
    )

    def __str__(self):
        return self.full_name

    @property
    def interest_list(self):
        return [i.strip() for i in self.interests.splitlines() if i.strip()]

    @property
    def role_list(self):
        return [r.strip() for r in self.typed_roles.split(",") if r.strip()]

    @property
    def bio_paragraphs(self):
        return [p.strip() for p in self.bio.split("\n\n") if p.strip()] or [self.bio]

    @property
    def whatsapp_url(self):
        digits = "".join(c for c in self.whatsapp_number if c.isdigit())
        return f"https://wa.me/{digits}" if digits else ""


class Education(models.Model):
    LEVELS = [("BSc", "BSc"), ("HSC", "HSC"), ("SSC", "SSC"), ("Other", "Other")]
    level = models.CharField(max_length=10, choices=LEVELS)
    degree = models.CharField(max_length=150, help_text="Like: BSc in Computer Science and Engineering")
    institution = models.CharField(max_length=200)
    year = models.CharField(max_length=30, help_text="Like: 2022 - 2026")
    result = models.CharField(max_length=60, help_text="Like: CGPA 3.82 / 4.00")
    order = models.PositiveIntegerField(default=0, help_text="Smaller number shows first")

    class Meta:
        ordering = ["order", "id"]
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.level} - {self.institution}"


class Experience(models.Model):
    title = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    period = models.CharField(max_length=60, blank=True, help_text="Like: Aug 2026 - Present")
    description = models.TextField(help_text="One point per line")
    order = models.PositiveIntegerField(default=0, help_text="Smaller number shows first")

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.title} at {self.company}"

    @property
    def points(self):
        return [p.strip().lstrip("-•* ").strip() for p in self.description.splitlines() if p.strip()]


class SkillCategory(models.Model):
    name = models.CharField(max_length=80, help_text="Like: Frontend")
    summary = models.CharField(max_length=200, blank=True, help_text="One short line shown with the skills")
    icon = models.CharField(
        max_length=40, default="bi-code-slash",
        help_text="Bootstrap icon class, like bi-code-slash. Find more at icons.getbootstrap.com",
    )
    order = models.PositiveIntegerField(default=0, help_text="Smaller number shows first")

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Skill category"
        verbose_name_plural = "Skill categories"

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name="skills")
    name = models.CharField(max_length=80)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.category.name}: {self.name}"


class Project(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    technologies = models.CharField(max_length=250, help_text="Separate with commas. Like: Python, Django, Bootstrap")
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True, help_text="Optional. Add it only if the project is live")
    order = models.PositiveIntegerField(default=0, help_text="Smaller number shows first")

    class Meta:
        ordering = ["order", "-id"]

    def __str__(self):
        return self.title

    @property
    def tech_list(self):
        return [t.strip() for t in self.technologies.split(",") if t.strip()]


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=3000)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name}: {self.subject}"
