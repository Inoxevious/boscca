"""mainapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# machine learning calls
# from prediction.urls import urlpatterns as endpoints_urlpatterns

# static files config
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url


from web import views
urlpatterns = [
    # APIs
    path('login', views.Index.as_view(), name="index"),
    path('admin/', admin.site.urls),
    # path('api/auth/', include('users.urls')),
    # path('api/', include('prediction.urls')),


    # Templates
    path('', views.Index.as_view(), name='index'),
    path('users/', include('users.urls')),
    path('web/', include('web.urls')),
    path('sacco/', include('sacco.urls')),

    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    
]
# urlpatterns += endpoints_urlpatterns
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

