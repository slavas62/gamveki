from django.contrib import admin
from solo.admin import SingletonModelAdmin
from fires_app.models import FireModis, FireViirs, Satellite, SiteConfiguration


class ModisFireAdmin(admin.ModelAdmin):
    list_display = ('date', 'satellite', 'confidence', 'frp', 'brightness21', 'brightness31')
    ordering = ('-date',)
    class Media:
        css = {'all':('css/admin/fireadmin.css',)}

class ViirsFireAdmin(admin.ModelAdmin):
    list_display = ('date', 'satellite', 'confidence', 'frp', 'brightness_ti4', 'brightness_ti5')
    ordering = ('-date',)
    class Media:
        css = {'all':('css/admin/fireadmin.css',)}

admin.site.register(FireModis, ModisFireAdmin)
admin.site.register(FireViirs, ViirsFireAdmin)
admin.site.register(Satellite)
admin.site.register(SiteConfiguration, SingletonModelAdmin)