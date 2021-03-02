from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass



@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(NationalBoards)
class NationalBoardsAdmin(admin.ModelAdmin):
    pass



@admin.register(SACCO)
class SACCOAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass



@admin.register(NationalStaffMember)
class NationalStaffMemberAdmin(admin.ModelAdmin):
    pass


@admin.register(SaccoMember)
class SaccoMemberAdmin(admin.ModelAdmin):
    pass



@admin.register(SaccoStaffMember)
class SaccoStaffMemberAdmin(admin.ModelAdmin):
    pass