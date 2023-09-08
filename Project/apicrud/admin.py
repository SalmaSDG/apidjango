from django.contrib import admin
from .models import Dataphone, UserProfile


class DataphoneAdmin(admin.ModelAdmin):
    list_display = ['RunningOn', 'imeiNumber', 'deviceModel', 'apiLevel', 'manufactureName', 'deviceName', 'productName', 'cpuType', 'hardwareName', 'created_at']
    list_display_links = ['imeiNumber']  # Choisir un champ approprié qui aura un lien pour la suppression

admin.site.register(Dataphone, DataphoneAdmin)

admin.site.register(UserProfile)