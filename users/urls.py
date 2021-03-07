from django.urls import path, include
from users.views import *
from django.conf.urls import url
app_name = 'users'
urlpatterns = [
   path('index/', index, name='index'),
   path('logout/', logout, name='logout'),
   path('add_tutor/', add_tutor, name='add_tutor'),
   path('add_new_member/', add_new_member, name='add_new_member'),
   path('add_sacco/', add_sacco, name='add_sacco'),
   path('add_city/', add_city, name='add_city'),
   path('get_citites/', get_citites, name='get_citites'),
   path('get_countries/', get_countries, name='get_countries'),
   path('assign_member/', assign_member, name='assign_member'),
   path('view_members/', view_members, name='view_members'),
   path('view_tutors/', view_tutors, name='view_tutors'),
   path('assign_tutor/', assign_tutor, name='assign_tutor'),
   path('view_executives/', view_executives, name='view_executives'),
   path('sign_up/',sign_up,name='sign_up'),
   path('sign_in/', sign_in, name='sign_in'),
#    path('profile/$', profile, name='profile'),
    # path('login/', APILoginView.as_view(), name='api_login')
   url(
        r"^profile/(?P<profile_id>.)", profile, name="profile"
    ),
]