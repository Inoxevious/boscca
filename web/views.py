from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .choices import countries_choices
# Create your views here.
class Index(TemplateView):
    template_name='web/pages/home/home.html'

class Apply(TemplateView):
    template_name='web/pages/apply/home.html'

class Contacts(TemplateView):
    template_name='web/pages/contact/home.html'

class SignIn(TemplateView):
    template_name='web/pages/signIn/home.html'
    def get_queryset(self, **kwargs):
        print(countries_choices)
        for key, val in countries_choices.items():
            print(key, ':', val)
        return countries_choices


    def get_context_data(self, **kwargs):
        print(countries_choices)
        context = super().get_context_data(**kwargs)
        context['countries_choices'] = countries_choices
        return context



class SignUp(TemplateView):
    template_name='web/pages/signUp/home.html'

class Communites(TemplateView):
    template_name='web/pages/communites/home.html'

class Help(TemplateView):
    template_name='web/pages/help/home.html'


class Alumni(TemplateView):
    template_name='web/pages/alumni/home.html'

class FutureStudents(TemplateView):
    template_name='web/pages/future_members/home.html'

class CurrentStudents(TemplateView):
    template_name='web/pages/current_members/home.html'

class Courses(TemplateView):
    template_name='web/pages/courses/home.html'

class Events(TemplateView):
    template_name='web/pages/events/home.html'

class FacultyStaff(TemplateView):
    template_name='web/pages/our_staff/home.html'

class Research(TemplateView):
    template_name='web/pages/research/home.html'


