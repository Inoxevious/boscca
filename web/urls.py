from django.urls import path, include
from web import views
from django.conf.urls import url
app_name = 'web'

urlpatterns = [
	path('home', views.Index.as_view(), name="home"),
	path('apply', views.Apply.as_view(), name="apply"),
	path('alumni', views.Alumni.as_view(), name="alumni"),
	path('contacts', views.Contacts.as_view(), name="contacts"),
	path('help', views.Help.as_view(), name="help"),
	path('sign_in', views.SignIn.as_view(), name="sign_in"),
	path('sign_up', views.SignUp.as_view(), name="sign_up"),
	path('research', views.Research.as_view(), name="research"),
	path('communites', views.Communites.as_view(), name="communites"),
	path('events', views.Events.as_view(), name="events"),
	path('our_staff', views.FacultyStaff.as_view(), name="our_staff"),
	path('future_members', views.FutureStudents.as_view(), name="future_members"),
	path('current_members', views.CurrentStudents.as_view(), name="current_members"),
	path('courses', views.Courses.as_view(), name="courses"),

]