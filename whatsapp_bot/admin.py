from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import PaynowPayment
# Register your models here.




admin.site.register(PaynowPayment)