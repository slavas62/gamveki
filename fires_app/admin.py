from django.contrib import admin
from solo.admin import SingletonModelAdmin
from fires_app.models import Fire, Satellite, SiteConfiguration


class FireAdmin(admin.ModelAdmin):
    list_display = ('date', 'satellite', 'confidence', 'frp', 'brightness21', 'brightness31')
    ordering = ('-date',)
    class Media:
        css = {'all':('css/admin/fireadmin.css',)}



admin.site.register(Fire, FireAdmin)
admin.site.register(Satellite)
admin.site.register(SiteConfiguration, SingletonModelAdmin)