import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#################################################################
    ##  Get Django environment set by docker (i.e either development or production), or else set it to local ##
#################################################################
try:
    DJANGO_ENV = os.environ.get("DJANGO_ENV")
except:
    DJANGO_ENV = 'local'

#################################################################
    ##  If Django environement has been set by docker it would be either development or production otherwise it would be undefined or local ##
#################################################################
if DJANGO_ENV == 'development' or DJANGO_ENV == 'production':

    try:
        SECRET_KEY = os.environ.get("SECRET_KEY")
    except:
        SECRET_KEY = 'localsecret'

    try:
        DEBUG = int(os.environ.get("DEBUG", default=0))
    except:
        DEBUG = False

    try:
        ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
    except:
        ALLOWED_HOSTS = ['*','127.0.0.1', '0.0.0.0', 'localhost' ,'boscca.sacconstellation.coop']

    DATABASES = {
        "default": {
            "ENGINE": os.environ.get("DB_ENGINE", "django.db.backends.sqlite3"),
            "NAME": os.environ.get("DB_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
            "USER": os.environ.get("DB_USER", "user"),
            "PASSWORD": os.environ.get("DB_PASSWORD", "password"),
            "HOST": os.environ.get("DB_HOST", "localhost"),
            "PORT": os.environ.get("DB_PORT", "5432"),
        }
    }
else:
    SECRET_KEY = 'localsecret'
    DEBUG = True
    ALLOWED_HOSTS = ['127.0.0.1','boscca.sacconstellation.coop']
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'USER': 'sacconstellation_boscca',
            'NAME': 'sacconstellation_boscca',
            'PASSWORD': 'boscca@1#',
            'HOST': 'localhost',
            'PORT': '3306',
            'default-character-set' : 'utf8'
 
        }
    }

#################################################################
    ##  (CORS) Cross-Origin Resource Sharing Settings ##
#################################################################

#################################################################
    ##  STATIC FILES ROOT AND URL ##
#################################################################
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
