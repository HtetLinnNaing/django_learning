from django.contrib import admin


class CustomAdminSite(admin.AdminSite):
    site_header = "Ecommerce System"
    site_title = "eAdmin"
