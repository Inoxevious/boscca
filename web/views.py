from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .choices import countries_choices
from sacco.models import *
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from web.models import *
# Create your views here.
class Index(ListView):
    template_name='web/pages/home/home.html'
    def get_queryset(self):
        # self.publisher = get_object_or_404(SACCO, name=self.kwargs['publisher'])
        self.home_slides = HomePageSlider.objects.all()
       

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        most_recent =  Article.objects.all().order_by('-publication_date')[:1]
        testimonials = Testimonial.objects.all()
        home_objectives = HomePageObjective.objects.all()
        home_facts = HomePageFacts.objects.all()[:4]
        home_mission = HomePage.objects.all()

        context['most_recent'] = most_recent
        context['home_slides'] = self.home_slides
        context['testimonials'] = testimonials
        context['home_mission'] = home_mission
        context['home_facts'] = home_facts
        context['home_objectives'] = home_objectives



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

class FacultyStaff(ListView):
    template_name='web/pages/our_staff/home.html'
    def get_queryset(self):
        # self.publisher = get_object_or_404(SACCO, name=self.kwargs['publisher'])
        self.staff = SaccoStaffMember.objects.all().order_by('-appointment_date')
       

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        most_recent =  SaccoStaffMember.objects.all().order_by('-appointment_date')[:1]
        print(most_recent)
        if BoardMembers.objects.filter(id=1).exists():
            board_statement = BoardMembers.objects.get(id=1)
        else:
            board_statement = BoardMembers(
                board_statement = 'The society has a Management Board consisting of 7 members who run the society.'
            )
            board_statement.save()
        context['board_statement'] = board_statement.board_statement
        context['stafflist'] = self.staff

class Research(ListView):
    template_name='web/pages/research/home.html'
    def get_queryset(self):
        # self.publisher = get_object_or_404(SACCO, name=self.kwargs['publisher'])
        self.articles = Article.objects.all().order_by('-publication_date')
       

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        most_recent =  Article.objects.all().order_by('-publication_date')[:1]
        print(most_recent)
        context['most_recent'] = most_recent
        context['article_list'] = self.articles
        context['research_article_list'] = self.articles

        return context


class ResearchDetailView(ListView):
    template_name='web/pages/research/detail.html'
    queryset = Article.objects.all()
    context_object_name = 'article'
    def get_queryset(self):
        # self.publisher = get_object_or_404(SACCO, name=self.kwargs['publisher'])
        self.articles = Article.objects.get(id=self.kwargs['pk'])
       

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        related_post =  Article.objects.filter(category=self.articles.category).order_by('-publication_date')[:1]
        comments_count = ArticleComment.objects.filter(Article=self.articles).count()
        comments = ArticleComment.objects.filter(Article=self.articles).order_by('-publication_date')
        print(related_post)
        context['article'] = self.articles
        context['related_post'] = related_post
        context['comments_count'] = comments_count
        context['comments'] = comments
        context['recommended'] = self.articles

        return context
        
    # def get_object(self):
    #     obj = super().get_object()
    #     # Record the last accessed date
    #     obj.last_accessed = timezone.now()
    #     obj.save()
    #     return obj
    #     return context

def comment_post(request,**kwargs):
    art_id = kwargs['pk']
    print(art_id)
    article = Article.objects.get(id=art_id)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']
        comments =  ArticleComment(
                        Article = article,
                        comment = comment,
                        comment_by = name,
                        email = email
                        )

        comments.save()
        messages.success(request,"Comment succesfully saved.")
        return redirect('web:research_detail', pk=art_id)
    else:
        messages.error(request,"Sorry comment not save!")
        return redirect('web:research_detail', pk=art_id)
