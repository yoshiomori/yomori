from django.contrib import admin

from portifolio.models import App


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    pass
