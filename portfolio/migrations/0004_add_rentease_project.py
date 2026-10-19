"""Adds the RentEase project. Skipped if it already exists, so it never duplicates."""
from django.db import migrations

GITHUB = "https://github.com/37maruf/Property-Rental-Management-System"


def add_project(apps, schema_editor):
    Project = apps.get_model("portfolio", "Project")
    if Project.objects.filter(github_url=GITHUB).exists():
        return
    Project.objects.create(
        title="RentEase \u2013 Property Rental & Management System",
        description=(
            "RentEase is a web-based property rental and management system developed using Django. It allows property owners to list, manage, update, and delete their properties, while tenants can browse, search, and filter available rentals by location, property type, and rent range. The system includes role-based authentication, rental request management, owner and tenant dashboards, request approval and rejection, reviews and ratings, email notifications, and Django Admin integration. It also ensures secure access control and prevents unauthorized property management."
        ),
        technologies="Python, Django, HTML5, CSS3, Bootstrap, PostgreSQL, SQLite",
        github_url=GITHUB,
        live_url="https://peaky.pythonanywhere.com/",
        order=1,
    )


class Migration(migrations.Migration):
    dependencies = [("portfolio", "0003_remove_project_image")]
    operations = [migrations.RunPython(add_project, migrations.RunPython.noop)]
