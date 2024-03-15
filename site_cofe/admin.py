from django.contrib import admin

from site_cofe.models import Site


@admin.register(Site)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
