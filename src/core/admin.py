from django.contrib import admin

from models import Session
from models import Spec

class SessionAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'started_at']

class SpecAdmin(admin.ModelAdmin):
    list_display = ['code', 'session', 'author', 'saved_at']

admin.site.register(Session, SessionAdmin)
admin.site.register(Spec, SpecAdmin)
