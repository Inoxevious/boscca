from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(AccountUser)
class AccountUserAdmin(admin.ModelAdmin):
    pass



@admin.register(MembershipRole)
class MembershipRoleAdmin(admin.ModelAdmin):
    pass
