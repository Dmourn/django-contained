from django.contrib import admin
from .models import Accounts, Contacts, ClockifyTimeEntry, ClockifyClient, ClockifyProject
from .auth.models import ClockifyWebhook

admin.site.register(ClockifyWebhook)

admin.site.register(Accounts)
admin.site.register(Contacts)
admin.site.register(ClockifyTimeEntry)
admin.site.register(ClockifyClient)
admin.site.register(ClockifyProject)
