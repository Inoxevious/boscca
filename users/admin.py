from django.contrib import admin
from .models import *
# Register your models here.
from web.models import *
from sacco.models import *
@admin.register(AccountUser)
class AccountUserAdmin(admin.ModelAdmin):
    pass



@admin.register(MembershipRole)
class MembershipRoleAdmin(admin.ModelAdmin):
    pass

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

@admin.register(BoardMembers)
class BoardMembersAdmin(admin.ModelAdmin):
    pass

@admin.register(Facts)
class FactsAdmin(admin.ModelAdmin):
    pass

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    pass

@admin.register(HomePageObjective)
class TestimonialAdmin(admin.ModelAdmin):
    pass


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    inlines = (
        HomePageSliderLineInline,HomePageFactsLineInline,HomePageObjectiveLineInline, HomePageArticleLineInline, HomePageTestimonialLineInline
    )

