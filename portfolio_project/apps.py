from django.contrib.admin.apps import AdminConfig


class SuperuserAdminConfig(AdminConfig):
    """Swap Django's default admin site for one that only lets superusers in."""
    default_site = "portfolio_project.admin_site.SuperuserAdminSite"
