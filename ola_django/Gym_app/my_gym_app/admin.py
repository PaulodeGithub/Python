from django.contrib import admin
from .models import Login, UserRegistration

# Register your models here, register our login table to display it
# on the Admin page
admin.site.register(Login)
admin.site.register(UserRegistration)
