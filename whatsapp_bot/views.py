from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
# from products.models import Product
from django.db.models import Q
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.contrib.auth.models import User
from django.db.models import Count
from django.conf import settings
from vap.models import Business
# from cart.cart import Cart
from paynow import Paynow
from .models import PaynowPayment
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
from twilio.twiml.messaging_response import MessagingResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import datetime
import emoji
import random
import json
import time
import os

# Create your views here.
def generate_transaction_id():
    """
    Generates a unique id which will be used by paynow to refer to the payment
    initiated
    """
    return str(int(time.time() * 1000))


@csrf_exempt
def index(request):
    paynow = Paynow(
    '9437',
	'5f8250e8-1c59-4d2c-ba00-8bd74693e6c2',
    'http://example.com/gateways/paynow/update', 
    'http://example.com/return?gateway=paynow'
    )
    if request.method == 'POST':
        # retrieve incoming message from POST request in lowercase
        incoming_msg = request.POST['Body'].lower()
        # create Twilio XML response
        resp = MessagingResponse()
        msg = resp.message()

        responded = False
        if incoming_msg == 'hello':
            response = emoji.emojize("""
*Hello Member! Welcome to SACCOSTALLION APP,* :wave:
Let me assist you :wink:
You can type any of the following:
:black_small_square: *'members':* To get a list of members in your community and phone numbers! :rocket:
:black_small_square: *'add member *national id*name*surname*phone*gender*age*location*specialization# *e.g Add member *29275558h26*innocent*mpasi#0777757603*male*27*mkoba*farming# '*: To register with us. choose one of these categories 1.business 2.individual 3.sacco 4.other. on location just write city name not specific address* 
""", use_aliases=True)
            msg.body(response)
            responded = True

        elif incoming_msg.startswith('add member'):
            result = ''

            # search for recipe based on user input (if empty, return featured recipes)
            search_text = incoming_msg.replace('add member', '')
            search_text = search_text.replace('*', ' ')
            search_text = search_text.replace('#', ' ')
            search_text = search_text.strip()
            text = str(search_text )
            national_id, name, surname, phone, gender, age, location, category, *_ = l = text.split()
            national_id = str(national_id)
            name = str(name)
            surname = str(surname)
            phone = str(phone)
            gender = str(gender)
            age = int(age)
            location = str(location)
            if (national_id):
                request.session['national_id'] = national_id
                request.session['name'] = name
                request.session['surname'] = surname
                request.session['phone'] = phone
                request.session['gender'] = gender
                request.session['location'] = location
                request.session['category'] = category
                request.session['age'] = age



                result += """

Nationa ID: {}
Name:   {} 
Surname: {}
Phone: {}
""".format(national_id, name, surname, phone)
                result = 'Great, Is this correct National ID - *{}* Name- *{}* Surname- *{}* Phone *{}*. If Yes types "yes member"'.format(national_id, name,  surname, phone )

            else:
                result = 'Sorry, I could not add member: {} of national ID: {} to database.'.format(name,  national_id )
            # image = str(image)
            # image = image.replace('/', "\\")
            # image = image.strip()
            # base = os.path.dirname(os.path.dirname(os.path.abspath(str(image))))
            # site_url = '127.0.0.1'
            # image = os.path.join(site_url + '/mush_store', image.url)
            # msg.media(image)
            msg.body(result)
            responded = True

        elif incoming_msg.startswith('yes member'):
            result = ''
            national_id = request.session['national_id']
            name = request.session['name']
            surname = request.session['surname']
            phone = request.session['phone']
            gender = request.session['gender']
            location = request.session['location'] 
            category = request.session['category'] 
            age = request.session['age']
            password = national_id
            email = 'member@valueaddition.co.zw'
            role = 'member'
            # username = str(name) + str(surname)
            # Check username
            if User.objects.filter(username = national_id).exists():
                result = 'Sorry, member: {} of national ID: {} is already registered.'.format(name,  national_id )
                # msg.body(result)
                # responded = True
            else :
                user = User.objects.create_user(username = national_id,
                password = password,email=email,first_name = name,
                last_name = surname )
                user.save()

                user = get_object_or_404(User, username = national_id)
                from users.models import AccountUser
                acc = AccountUser(user_id = user.id, role = role, phone=phone, address =location, age = age, category=category, gender = gender,id_number=national_id)
                acc.save()

                result += """

Nationa ID: {}
Name:   {} 
Surname: {}
Phone: {}
""".format(national_id, name, surname, phone)
                result = 'Great, National ID - *{}* Name- *{}* Surname- *{}* Phone *{}*. was addes successfully.'.format(national_id, name,  surname, phone )

           
            # image = str(image)
            # image = image.replace('/', "\\")
            # image = image.strip()
            # base = os.path.dirname(os.path.dirname(os.path.abspath(str(image))))
            # site_url = '127.0.0.1'
            # image = os.path.join(site_url + '/mush_store', image.url)
            # msg.media(image)
            msg.body(result)
            responded = True

        elif incoming_msg == 'members':
            from users.models import AccountUser
            s = AccountUser.objects.filter(role__icontains='member')
            num_members = AccountUser.objects.filter(role__icontains='member').count()
            separator = ' - '
            if s:
                        result = ''

                        for member in s:
                            name = member.user.last_name
                            cat = member.category
                            phone = member.phone

                            result += """
{}
Name:  {} 
Major Specialization: {}
Phone: *{}*
""".format(separator, name, cat, phone)

            else:
                result = 'Sorry, I could not find any results'

            title = """*Number of Registered members: ({})*""".format(num_members)
            message = title + '\n'
            msg.body(message)
            msg.body(result)
            responded = True


        elif incoming_msg == 'news':
            r = requests.get('https://newsapi.org/v2/top-headlines?sources=bbc-news,the-washington-post,the-wall-street-journal,cnn,fox-news,cnbc,abc-news,business-insider-uk,google-news-uk,independent&apiKey=3ff5909978da49b68997fd2a1e21fae8')
            
            if r.status_code == 200:
                data = r.json()
                articles = data['articles'][:5]
                result = ''
                
                for article in articles:
                    title = article['title']
                    url = article['url']
                    if 'Z' in article['publishedAt']:
                        published_at = datetime.datetime.strptime(article['publishedAt'][:19], "%Y-%m-%dT%H:%M:%S")
                    else:
                        published_at = datetime.datetime.strptime(article['publishedAt'], "%Y-%m-%dT%H:%M:%S%z")
                    result += """
*{}*
Read more: {}
_Published at {:02}/{:02}/{:02} {:02}:{:02}:{:02} UTC_
""".format(
    title,
    url, 
    published_at.day, 
    published_at.month, 
    published_at.year, 
    published_at.hour, 
    published_at.minute, 
    published_at.second
    )

            else:
                result = 'I cannot fetch news at this time. Sorry!'

            msg.body(result)
            responded = True

        elif incoming_msg.startswith('statistics'):
            # runs task to aggregate data from Apify Covid-19 public actors
            requests.post('https://api.apify.com/v2/actor-tasks/5MjRnMQJNMQ8TybLD/run-sync?token=qTt3H59g5qoWzesLWXeBKhsXu&ui=1')
            
            # get the last run dataset items
            r = requests.get('https://api.apify.com/v2/actor-tasks/5MjRnMQJNMQ8TybLD/runs/last/dataset/items?token=qTt3H59g5qoWzesLWXeBKhsXu')
            
            if r.status_code == 200:
                data = r.json()

                country = incoming_msg.replace('statistics', '')
                country = country.strip()
                country_data = list(filter(lambda x: x['country'].lower().startswith(country), data))

                if country_data:
                    result = ''

                    for i in range(len(country_data)):
                        data_dict = country_data[i]
                        last_updated = datetime.datetime.strptime(data_dict.get('lastUpdatedApify', None), "%Y-%m-%dT%H:%M:%S.%fZ")

                        result += """
*Statistics for country {}*
Infected: {}
Tested: {}
Recovered: {}
Deceased: {}
Last updated: {:02}/{:02}/{:02} {:02}:{:02}:{:03} UTC
""".format(
    data_dict['country'], 
    data_dict.get('infected', 'NA'), 
    data_dict.get('tested', 'NA'), 
    data_dict.get('recovered', 'NA'), 
    data_dict.get('deceased', 'NA'),
    last_updated.day,
    last_updated.month,
    last_updated.year,
    last_updated.hour,
    last_updated.minute,
    last_updated.second
    )
                else:
                    result = "Country not found. Sorry!"
            
            else:
                result = "I cannot retrieve statistics at this time. Sorry!"

            msg.body(result)
            responded = True

        
        if not responded:
             msg.body("Sorry, I don't understand. Send 'hello' for a list of commands.")

        return HttpResponse(str(resp))

    return HttpResponse('ok')
