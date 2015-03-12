from django.contrib import admin
from fires_app.models import Fire, Satellite

from salmonella.admin import SalmonellaMixin


class FireAdmin(SalmonellaMixin, admin.ModelAdmin):
    salmonella_fields = ('satellite',)
    class Media:
        css = {'all':('css/admin/fireadmin.css',)}

admin.site.register(Fire, FireAdmin)
admin.site.register(Satellite)