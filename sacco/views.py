from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
# Create your views here.
from sacco.models import *
class Dashboard(TemplateView):
    template_name='web/dashboard/home/home.html'
# Create your views here.

class ArticleList(ListView):
    template_name = 'web/pages/research/home.html'
    queryset = Article.objects.order_by('-publication_date')
    context_object_name = 'article_list'

    def get_queryset(self):
        self.publisher = get_object_or_404(SACCO, name=self.kwargs['publisher'])
        return Article.objects.filter(publisher=self.publisher)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['article_list'] = self.publisher
        return context


class ArticleDetailView(DetailView):
    template_name = 'web/pages/research/detail.html'
    queryset = Article.objects.all()
    context_object_name = 'article_list'
    def get_object(self):
        obj = super().get_object()
        # Record the last accessed date
        obj.last_accessed = timezone.now()
        obj.save()
        return obj