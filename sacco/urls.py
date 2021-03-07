from django.urls import path, include
from sacco import views
from django.conf.urls import url
app_name = 'sacco'

urlpatterns = [
	path('dashboard', views.Dashboard.as_view(), name="dashboard"),
    path('articles/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),


]