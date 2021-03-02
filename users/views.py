from rest_auth.views import (LoginView, LogoutView)
from rest_auth.views import (LoginView, LogoutView, PasswordChangeView)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import *
from .models import *
from sacco.models import *
from rest_framework import status , generics , mixins, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib import messages, auth
from django.utils.datastructures import MultiValueDictKeyError
from datetime import datetime, date
from .forms import *
from django.http import JsonResponse

# Create your views here.

#############################################################
# LOGOUT MEMBER
##############################################################
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,"Logged Out")
    return redirect('web:sign_in')



#############################################################
# ACCESS MAIN DASHBOARD
##############################################################
@login_required(login_url='/web/sign_in/')
def index(request, **kwargs):
	if request.user:
		# request['user'] = user
		user = request.user
		print('user' ,request.user)
		context= {'user': user }
		loged_in_user = AccountUser.objects.get(user=user)
		if loged_in_user.membership_role.group == 'member':
			if SaccoStaffMember.objects.filter(profile=loged_in_user, role__name='manager' ).exists():
				manager = SaccoStaffMember.objects.get(profile=loged_in_user, role__name='manager' )

				print('manager', manager)
				context = {
					'user': manager,
					'loged_in_user' : loged_in_user,
					
				}
				if loged_in_user.organization == '':
					return redirect('users:add_sacco')
				else:
					return render(request,'web/dashboards/manager/home/index.htm' , context)

			elif SaccoStaffMember.objects.filter(profile=loged_in_user, role__name='secretary' ).exists():
				secretary = Secretary.objects.get(profile=loged_in_user)
				print('secretary', secretary)
				context = {
					'user': secretary,
				}                    
				
				return render(request,'web/dashboards/secretary/home/index.htm' , context)

			elif Tutor.objects.filter(profile=loged_in_user).exists():
				tutor = Tutor.objects.get(profile=loged_in_user)
				print('tutor', tutor)
				context = {
					'tutor': tutor,
				}                      
				
				return render(request,'web/dashboards/tutor/home/index.htm' , context)

			else:
				member = AccountUser.objects.get(profile=loged_in_user)
				print('member', member.membership_role)
				context = {
					'member': member,
				} 
				return render(request,'web/dashboards/member/home/index.htm' , context)
		
		elif loged_in_user.user_role.group == 'student':
			return render(request,'web/dashboards/student/home/index.htm' , context)            
		

		# return Response({"token": user.auth_token.key})
	else:
		
		context= {'status': status.HTTP_400_BAD_REQUEST }
		return render(request,'web/pages/signIn/home.html',context )


#############################################################
# LOGIN MEMBER
##############################################################
def sign_in(request):
	if request.method == "POST":
		username = request.POST["email"]
		password = request.POST["password"]
		print('password',password)
		print('username',username)
		# user = auth.login().
		user = auth.authenticate(username=username, password=password)
		print('user',user)
		if user:
			auth.login(request,user)
			messages.success(request,"You are now logged in.")
			return redirect('users:index')

		else:
				messages.error(request,"Invalid Credentials")
				return redirect('users:sign_in')       
	else:
		return render(request,'web/pages/signIn/home.html')


#############################################################
# SIGNUP NEW  MEMBER
##############################################################
def sign_up(request):
	role_choices = MembershipRole.objects.all()
	if request.method == "POST":
		# Get form values
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		city = request.POST["city"]
		national_id = request.POST["national_id"]
		whatsapp_number = request.POST["whatsapp_number"]
		country = request.POST["country"]


		try:
			role = request.POST['role']
			print("role found", role)
		except MultiValueDictKeyError:
			role = 'undefined'

		try:
			password = request.POST['password']
			print("password found", password)
		except MultiValueDictKeyError:
			password = 'undefined'


		try:
			password1 = request.POST['password1']
			print("password1 found", password1)
		except MultiValueDictKeyError:
			password1 = 'undefined'


		# Check if passwords match
		if password == password1:
			# Check username
			if User.objects.filter(username = national_id).exists():
				messages.error(request,"That user already registered.")
				return redirect('web:sign_in')
			else:
				if User.objects.filter(email = email).exists():
					messages.error(request,"That email is taken.")
					return redirect('web:sign_in')
				else:
					# looks good
					if MembershipRole.objects.filter(name=role).exists():
						mrole =  MembershipRole.objects.get(name=role)

					else: 
						if role ==  'student':
							group = 'student'
						else:
							group = 'member'

						mrole = MembershipRole(
							name=role,
							group=group
						)
						mrole.save()
						
					user = User.objects.create_user(username = national_id,
					password = password,email=email,first_name = first_name,
					last_name = last_name, is_staff = True )
					user.save()
					if mrole.group == 'member':
						if MembershipRole.objects.filter(name='manager').exists():
							exrole =  MembershipRole.objects.get(name='manager')
						else: 
							exrole = MembershipRole(
								name='manager',
								group = 'member'
							)
							exrole.save()

						acc = AccountUser(user = user, city = city,
										  national_id=national_id,
										  whatsapp_number = whatsapp_number,
										  country=country,
										  membership_role=exrole
										   
										  )          
						acc.save()
						
						auth.login(request,user)
						messages.success(request,"You are now logged in.")
						return redirect('users:add_sacco')
					else:
						if MembershipRole.objects.filter(name='student').exists():
							exrole =  MembershipRole.objects.get(name='student')
						else: 
							exrole = MembershipRole(
								name='student',
								group = 'student'
							)
							exrole.save()
						acc = AccountUser(user = user, city = city, 
										  national_id = national_id,
										  whatsapp_number = whatsapp_number,
										  country=country,
										  membership_role=exrole

										  )          
						acc.save()
						auth.login(request,user)
						messages.success(request,"You are now registered.")
						return redirect('users:index')

		else:
			messages.error(request,'Passwords do not match.')
			return redirect('web:sign_in')
	else:
		role_choices = MembershipRole.objects.all()
		context = {
			'role_choices': role_choices,
		   
		}
		return render(request,'web/pages/signIn/home.html' , context)
#############################################################
# SEARCH MEMBER PROFILE
##############################################################

def profile(request,profile_id):
	print("profile_id", profile_id)
	user_id = profile_id
	print('loged_in_user', request.user)
	loged_in_user = AccountUser.objects.get(user=request.user)
	# user_id = request.GET.get['id']
	user = AccountUser.objects.get(id=user_id)
	print("user", user)
	context = {
		'loged_in_user': loged_in_user,
		'user':user,
	}
	return render(request,'web/dashboards/manager/profile/index.html', context)



#############################################################
# ADD ORGANIZATIONS MEMBER
##############################################################


@login_required(login_url='/web/sign_in/')
def add_sacco(request):
	if request.method == "POST":
		user = request.user
		loged_in_user = AccountUser.objects.get(user=user)
		og_count = SACCO.objects.all().count()
		sacco_id = 'ZWCU-{}-{}'.format(date.today(),og_count)
		registered_by_id = loged_in_user.id

		name = request.POST["business_name"]
		city = request.POST["city"]
		country = request.POST["country"]
		address = request.POST["address"]
		phone = request.POST["phone"]



		sacco = SACCO(
			sacco_id=sacco_id,name=name,
			country = country,
			city=city,
			address=address, phone=phone, 
			registered_by_id=registered_by_id
		)
		sacco.save()

		loged_in_user.sacco = SACCO
		loged_in_user.save()

		staff_count = SaccoStaffMember.objects.filter(sacco=sacco).count()
		print('staff_count',staff_count)
		staff_id = 'SACCO-{}-SM-{}-{}'.format(sacco.id,staff_count,date.today())
		if Department.objects.filter(sacco=sacco, name='general management').exists():
			department = Department.objects.get(sacco=sacco, name='general management')
		else:
			department = Department(sacco=sacco, name='general management')
			department.save()

		if MembershipRole.objects.filter(name='manager').exists():
			role =  MembershipRole.objects.get(name='manager')
		else: 
			role = MembershipRole(
				name='manager'
			)
			role.save()
		manager_account = SaccoStaffMember(profile=loged_in_user, 
								  staff_id_id= staff_id_id, 
								  sacco=sacco,department=department,
								  role=role,is_executive=True
								  
								  )
		manager_account.save()
		print('accunt user', manager_account)
		return redirect('users:index')
	else:
		xrole = MembershipRole.objects.all()
		from web.choices import countries_choices
		form = CityForm()
		cities = City.objects.all()
		context = {'xrole':xrole, 'countries_choices': countries_choices, 'form': form}

		return render(request,'web/dashboards/manager/home/add_sacco.html', context)


# ############################################################
# ADD NEW MEMBER

##############################################################

@login_required(login_url='/web/sign_in/')
def add_new_member(request, **kwargs):
	if request.method == "POST":
		whatsapp_number = request.POST["whatsapp_number"]
		direct_number = request.POST["direct_number"]
		first_name = request.POST["first_name"]
		last_name = request.POST["last_name"]
		national_id = request.POST["national_id"]
		home_address = request.POST["home_address"]
		email = request.POST["email"]
		facebook_url = request.POST["url"]

		# user = auth.login().
		password = '{}@{}'.format(last_name, national_id)
		user = User.objects.create_user(username = national_id,
		password = password,email=email,first_name = first_name,
		last_name = last_name, is_staff = False )
		user.save()
		# mrole =  MembershipRole.objects.get(name='member')
		if MembershipRole.objects.filter(name='member').exists():
			mrole =  MembershipRole.objects.get(name='member')
		else: 
			group = 'member'
			mrole = MembershipRole(
				name='member',
				group=group
			)
			mrole.save()
		acc = AccountUser(user = user, whatsapp_number =whatsapp_number, direct_number = direct_number,
		national_id =national_id, home_address =home_address, facebook_url =facebook_url,
		 user_role = mrole )          
		acc.save()
		print('user',user)
		if acc:
			messages.success(request,"Member successfully added.")
			return redirect('users:add_new_member')

		else:
				messages.error(request,"Invalid Details")
				return redirect('users:add_new_member')       
	else:
		return render(request,'web/dashboards/manager/members/add_member.html')


# ############################################################
# ASSIGN MEMBER

##############################################################
@login_required(login_url='/web/sign_in/')
def assign_member(request):
	if request.method == "POST":
		user = request.user
		loged_in_user = AccountUser.objects.get(user=user)
		print('logged in user', loged_in_user.organization)
		og_count = Organization.objects.all().count()
		registered_by_id = loged_in_user.id

		try:
			member = request.POST['member']
			print("member found", member)
		except MultiValueDictKeyError:
			member = 'undefined'


		try:
			role = request.POST['role']
			print("role found", role)
		except MultiValueDictKeyError:
			role = 'undefined'


		qry_member = AccountUser.objects.get(id=member)
		qry_role = MembershipRole.objects.get(id=role)
		if qry_role.name == 'secretary':
			secretary_count = Secretary.objects.filter(organization=loged_in_user.organization.id).count()

			secretary_id = 'ZWCU-{}-SS-{}-{}'.format(loged_in_user.organization.id,secretary_count,date.today())

			secretary = Secretary(secretary_id=secretary_id, profile = qry_member, organization=loged_in_user.organization)
			secretary.save()
			
		elif qry_role.name == 'tutor':
			tutor_count = Tutor.objects.filter(organization=loged_in_user.organization.id).count()

			tutor_id = 'ZWCU-{}-ST-{}-{}'.format(loged_in_user.organization.id,tutor_count,date.today())

			tutor = Tutor(tutor_id=tutor_id, profile = qry_member, organization=loged_in_user.organization)
			tutor.save()
		else:
			officer_count = FinanceOfficer.objects.filter(organization=loged_in_user.organization.id).count()

			officer_id = 'ZWCU-{}-SFO-{}-{}'.format(loged_in_user.organization.id,officer_count,date.today())

			officer = FinanceOfficer(finance_officer_id=officer_id, profile = qry_member, organization=loged_in_user.organization)
			officer.save()
		return redirect('users:index')
	else:
		user = request.user
		loged_in_user = AccountUser.objects.get(user=user)
		members = AccountUser.objects.filter(organization = loged_in_user.organization)
		xrole = MembershipRole.objects.all()
		context = {'roles':xrole, 'members':members}
		return render(request,'web/dashboards/manager/members/assign_member.html', context)


		# ############################################################
# ASSIGN TUTOR

##############################################################
@login_required(login_url='/web/sign_in/')
def assign_tutor(request):
	if request.method == "POST":
		user = request.user
		loged_in_user = AccountUser.objects.get(user=user)
		print('logged in user', loged_in_user.organization)
		og_count = Organization.objects.all().count()
		registered_by_id = loged_in_user.id

		try:
			member = request.POST['member']
			print("member found", member)
		except MultiValueDictKeyError:
			member = 'undefined'


		try:
			role = request.POST['role']
			print("role found", role)
		except MultiValueDictKeyError:
			role = 'undefined'


		qry_member = AccountUser.objects.get(id=member)
		qry_role = MembershipRole.objects.get(id=role)
		if qry_role.name == 'secretary':
			secretary_count = Secretary.objects.filter(organization=loged_in_user.organization.id).count()

			secretary_id = 'ZWCU-{}-SS-{}-{}'.format(loged_in_user.organization.id,secretary_count,date.today())

			secretary = Secretary(secretary_id=secretary_id, profile = qry_member, organization=loged_in_user.organization)
			secretary.save()
			
		elif qry_role.name == 'tutor':
			tutor_count = Tutor.objects.filter(organization=loged_in_user.organization.id).count()

			tutor_id = 'ZWCU-{}-ST-{}-{}'.format(loged_in_user.organization.id,tutor_count,date.today())

			tutor = Tutor(tutor_id=tutor_id, profile = qry_member, organization=loged_in_user.organization)
			tutor.save()
		else:
			officer_count = FinanceOfficer.objects.filter(organization=loged_in_user.organization.id).count()

			officer_id = 'ZWCU-{}-SFO-{}-{}'.format(loged_in_user.organization.id,officer_count,date.today())

			officer = FinanceOfficer(finance_officer_id=officer_id, profile = qry_member, organization=loged_in_user.organization)
			officer.save()
		return redirect('users:index')
	else:
		user = request.user
		loged_in_user = AccountUser.objects.get(user=user)
		members = AccountUser.objects.filter(organization = loged_in_user.organization)
		xrole = MembershipRole.objects.all()
		context = {'roles':xrole, 'members':members}
		return render(request,'web/dashboards/manager/members/assign_tutor.html', context)


# ############################################################
# VIEW MEMBERS

##############################################################
@login_required(login_url='/web/sign_in/')
def view_members(request):
	user = request.user
	loged_in_user = AccountUser.objects.get(user=user)
	members = AccountUser.objects.filter(organization = loged_in_user.organization)
	xrole = MembershipRole.objects.all()
	context = {'roles':xrole, 'members':members}
	return render(request,'web/dashboards/manager/members/view_members.html', context)


# ############################################################
# VIEW  executives

##############################################################
@login_required(login_url='/web/sign_in/')
def view_executives(request):
	user = request.user
	loged_in_user = AccountUser.objects.get(user=user)
	tutor = Tutor.objects.filter(organization = loged_in_user.organization)
	xrole = MembershipRole.objects.all()
	context = {'roles':xrole, 'members':tutor}
	return render(request,'web/dashboards/manager/members/view_executives.html', context)
# ############################################################
# VIEW  executives

##############################################################
@login_required(login_url='/web/sign_in/')
def add_tutor(request):
	user = request.user
	loged_in_user = AccountUser.objects.get(user=user)
	tutor = Tutor.objects.filter(organization = loged_in_user.organization)
	xrole = MembershipRole.objects.all()
	context = {'roles':xrole, 'members':tutor}
	return render(request,'web/dashboards/manager/education/course/add_tutor.html', context)




# ############################################################
# VIEW TUTORS

##############################################################
@login_required(login_url='/web/sign_in/')
def view_tutors(request):
	user = request.user
	loged_in_user = AccountUser.objects.get(user=user)
	tutor = Tutor.objects.filter(organization = loged_in_user.organization)
	xrole = MembershipRole.objects.all()
	context = {'roles':xrole, 'members':tutor}
	return render(request,'web/dashboards/manager/members/view_tutors.html', context)

# ############################################################
# VIEW COURSES

##############################################################
@login_required(login_url='/web/sign_in/')
def view_tutors(request):
	user = request.user
	loged_in_user = AccountUser.objects.get(user=user)
	tutor = Tutor.objects.filter(organization = loged_in_user.organization)
	xrole = MembershipRole.objects.all()
	context = {'roles':xrole, 'members':tutor}
	return render(request,'web/dashboards/manager/members/view_tutors.html', context)


# ############################################################
# VIEW STUDENTS

##############################################################
@login_required(login_url='/web/sign_in/')
def view_students(request):
	user = request.user
	loged_in_user = AccountUser.objects.get(user=user)
	tutor = Tutor.objects.filter(organization = loged_in_user.organization)
	xrole = MembershipRole.objects.all()
	context = {'roles':xrole, 'members':tutor}
	return render(request,'web/dashboards/manager/members/view_tutors.html', context)



def add_city(request):
	if request.method == "POST" and request.is_ajax():
		try:
			city = request.query_params.get('city')
			print("city found", city)
		except MultiValueDictKeyError:
			city = 'undefined'

		print("cityyyyyy",city)
		data = {"city": city}
		return JsonResponse(data, status = 200)

def add_city(request):
	# request should be ajax and method should be POST.
	if request.is_ajax and request.method == "POST":
		# get the form data
		form = CityForm(request.POST)
		# save the data and after fetch the object in instance
		if form.is_valid():
			print('form', form)
			instance = form.save()
			# serialize in new friend object in json
			ser_instance = serializers.serialize('json', [ instance, ])
			# send to client side.
			return JsonResponse({"instance": ser_instance}, status=200)
		else:
			# some form errors occured.
			return JsonResponse({"error": form.errors}, status=400)

	# some error occured
	return JsonResponse({"error": ""}, status=400)
	get_citites

def get_citites(request):
	if request.method == "GET" and request.is_ajax():
		country = request.GET.get('country')
		city = City.objects.filter(country = country).\
			exclude(state__isnull=True).exclude(state__exact='').\
			order_by('state').values_list('state').distinct()
		city = [i[0] for i in list(city)]
		print('city', city)

		data = {
			"city": city, 
		}
		return JsonResponse(data, status = 200)

def get_countries(request):
    # get all the countreis from the database excluding 
    # null and blank values

	if request.method == "GET" and request.is_ajax():
		countries = City.objects.exclude(country__isnull=True).\
			exclude(country__exact='').order_by('country').values_list('country').distinct()
		countries = [i[0] for i in list(countries)]
		print('countries', countries)
		data = {
			"countries": countries, 
		}
		return JsonResponse(data, status = 200)
