from django.contrib import admin
from main.models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contact, ContactAdmin)