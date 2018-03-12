from django.contrib import admin
from bbm.models import Pins, PinMeta, Contacts

class PinsViewAdmin(admin.ModelAdmin):
    list_display = ['id', 'pin']
    search_fields = ['pin']


class PinMetaViewAdmin(admin.ModelAdmin):
    list_display = ['id', 'pin', 'meta_key', 'meta_value']
    search_fields = ['pin__pin','meta_key', 'meta_value']

class ContactsViewAdmin(admin.ModelAdmin):
    list_display = ['id', 'pin', 'contact']
    search_fields = ['pin__pin', 'contact__pin']

admin.site.register(Pins, PinsViewAdmin)
admin.site.register(PinMeta, PinMetaViewAdmin)
admin.site.register(Contacts, ContactsViewAdmin)