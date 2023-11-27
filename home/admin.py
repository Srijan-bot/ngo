from django.contrib import admin

# Register your models here.
from .models import Service,Faq

admin.site.register(Service)
admin.site.register(Faq)