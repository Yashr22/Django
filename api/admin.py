from django.contrib import admin
from api.models import SignupData,Note,ContactMessage,Chat

# Register your models here.

admin.site.register(SignupData),
admin.site.register(Note),
admin.site.register(ContactMessage),
admin.site.register(Chat),