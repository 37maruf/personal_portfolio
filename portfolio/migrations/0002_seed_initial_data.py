"""Fills the site with the details from Maruf's CV so it is not empty on first run.
Everything here can be edited or deleted later from the admin panel."""
from django.db import migrations

BIO = (
    "I am a Computer Science and Engineering graduate from Green University of Bangladesh, "
    "passionate about web development, with a strong focus on Python and Django. I have hands-on "
    "experience in building responsive web applications, developing REST APIs, implementing "
    "authentication, and managing databases using SQL and Django ORM. I am also familiar with "
    "HTML, CSS, JavaScript, and Bootstrap.\n\n"
    "I also have experience in Software Quality Assurance, including manual testing and test "
    "automation using Playwright and Pytest."
)

CAREER_GOAL = (
    "I want to build innovative, user-friendly web solutions while continuously improving "
    "my technical skills."
)

INTERESTS = "Web development with Python and Django\nSoftware quality assurance\nTest automation with Playwright and Pytest\nBuilding responsive, user-friendly web apps"

SKILLS = [
    ("Backend", "bi-server", "Building the logic behind a website", [
        "Python", "Django", "REST APIs", "Authentication", "Django ORM"]),
    ("Frontend", "bi-window-stack", "Pages that look good on every screen", [
        "HTML", "CSS", "JavaScript", "Bootstrap"]),
    ("Database", "bi-database", "Storing and querying data", [
        "SQL", "Django ORM", "SQLite"]),
    ("Testing / QA", "bi-bug", "Finding bugs before users do", [
        "Manual Testing", "Test Case Design", "Bug Reporting", "Playwright", "Pytest", "Page Object Model"]),
    ("Tools", "bi-git", "Daily workflow", ["Git", "GitHub"]),
]


def seed(apps, schema_editor):
    Profile = apps.get_model("portfolio", "Profile")
    Education = apps.get_model("portfolio", "Education")
    Experience = apps.get_model("portfolio", "Experience")
    SkillCategory = apps.get_model("portfolio", "SkillCategory")
    Skill = apps.get_model("portfolio", "Skill")

    if Profile.objects.exists():
        return

    Profile.objects.create(
        full_name="Md. Maruf Khan",
        tagline="Computer Science and Engineering graduate who builds with Python and Django",
        typed_roles="Django Developer, Python Developer, SQA Engineer, Test Automation Learner",
        bio=BIO,
        interests=INTERESTS,
        career_goal=CAREER_GOAL,
        email="marufkhanmk07@gmail.com",
        phone="01700921553",
        whatsapp_number="8801700921553",
        facebook_url="https://www.facebook.com/share/19fwo8StzS/",
        github_url="https://github.com/37maruf",
        linkedin_url="https://www.linkedin.com/in/maruf-khan-5a27b5393/",
    )

    Education.objects.create(
        level="BSc", order=1, year="2022 - 2026", result="CGPA 3.82 / 4.00",
        degree="BSc in Computer Science and Engineering",
        institution="Green University of Bangladesh, Purbachal American City, Kanchon 1460",
    )
    Education.objects.create(
        level="HSC", order=2, year="2020 - 2021", result="GPA 5.00 / 5.00",
        degree="Higher Secondary Certificate (HSC)",
        institution="Baharpur Degree College, Rajbari",
    )
    Education.objects.create(
        level="SSC", order=3, year="2019", result="GPA 4.83 / 5.00",
        degree="Secondary School Certificate (SSC)",
        institution="Baharpur High School, Rajbari",
    )

    Experience.objects.create(
        order=1, title="Software Quality Assurance (SQA) Intern", company="QA Harbor Limited",
        period="2026",
        description=(
            "Gained practical experience in manual testing, test case design, and bug reporting.\n"
            "Developed automated tests using Playwright, Pytest, and Page Object Model (POM).\n"
            "Tested web features including registration, login, product search, and cart functionality."
        ),
    )

    for i, (name, icon, summary, skills) in enumerate(SKILLS, start=1):
        cat = SkillCategory.objects.create(name=name, icon=icon, summary=summary, order=i)
        for j, s in enumerate(skills, start=1):
            Skill.objects.create(category=cat, name=s, order=j)


def unseed(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [("portfolio", "0001_initial")]
    operations = [migrations.RunPython(seed, unseed)]
