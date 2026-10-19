"""Updates RentEase text if the earlier draft wording is still in place."""
from django.db import migrations

GITHUB = "https://github.com/37maruf/Property-Rental-Management-System"
OLD_START = "RentEase is a web application that connects property owners and tenants"
DESC = (
    "RentEase is a web-based property rental and management system developed using Django. It allows property owners to list, manage, update, and delete their properties, while tenants can browse, search, and filter available rentals by location, property type, and rent range. The system includes role-based authentication, rental request management, owner and tenant dashboards, request approval and rejection, reviews and ratings, email notifications, and Django Admin integration. It also ensures secure access control and prevents unauthorized property management."
)
TECH = "Python, Django, HTML5, CSS3, Bootstrap, PostgreSQL, SQLite"


def update(apps, schema_editor):
    Project = apps.get_model("portfolio", "Project")
    for p in Project.objects.filter(github_url=GITHUB, description__startswith=OLD_START):
        p.description = DESC
        p.technologies = TECH
        p.save()


class Migration(migrations.Migration):
    dependencies = [("portfolio", "0004_add_rentease_project")]
    operations = [migrations.RunPython(update, migrations.RunPython.noop)]
