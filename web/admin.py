from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from web.models import *
from sacco.models import *



class HomePageSliderLineInline(admin.TabularInline):
    model = HomePageSlider
    extra = 1

class HomePageFactsLineInline(admin.TabularInline):
    model = HomePageFacts
    extra = 1

class HomePageTestimonialLineInline(admin.TabularInline):
    model = HomePageTestimonial
    extra = 1

class HomePageArticleLineInline(admin.TabularInline):
    model = HomePageArticle
    extra = 1

class HomePageObjectiveLineInline(admin.TabularInline):
    model = HomePageObjective
    extra = 1

class NationalStaffMemberLineInline(admin.TabularInline):
    model = NationalStaffMember
    extra = 1

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    inlines = (
        HomePageSliderLineInline,HomePageFactsLineInline,HomePageObjectiveLineInline, HomePageArticleLineInline, HomePageTestimonialLineInline
    )


@admin.register(BoardMembers)
class BoardMembersAdmin(admin.ModelAdmin):
    pass

@admin.register(Facts)
class FactsAdmin(admin.ModelAdmin):
    pass

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    pass

# @admin.register(BoardMembers)
# class HomePageAdmin(admin.ModelAdmin):
#     pass

# @admin.register(BoardMembers)
# class HomePageAdmin(admin.ModelAdmin):
#     pass
# Register your models here.
