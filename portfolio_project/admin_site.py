from django.contrib import admin


class SuperuserAdminSite(admin.AdminSite):
    site_header = "Maruf Portfolio Admin"
    site_title = "Portfolio Admin"
    index_title = "Manage your portfolio"

    def has_permission(self, request):
        # Normal Django lets any "staff" user in. Here only an active superuser can.
        user = request.user
        return bool(user.is_active and user.is_superuser)
