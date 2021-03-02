from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    pass

@admin.register(ModuleItems)
class ModuleItemsAdmin(admin.ModelAdmin):
    pass


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    pass
@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    pass

@admin.register(SurveyItem)
class SurveyItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass
@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    pass