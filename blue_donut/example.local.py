# flake8: noqa

import os

from .settings import *

############################
# Django Settings
############################

# Make sure to not run a production server with debug on.
DEBUG = True

# https://randomkeygen.com/
SECRET_KEY = ""

# Add your domain name here.
ALLOWED_HOSTS = []

# I wouldn't modify the database location, but it's up to you.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Stuff doesn't work with STATIC_ROOT set to the same directory as STATICFILES_DIRS.
if DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, "static_root")
else:
    STATIC_ROOT = os.path.join(BASE_DIR, "static")

############################
# ESI Settings
############################

# Go to https://developers.eveonline.com/applications and make an application.
# It needs these scopes:
# esi-location.read_location.v1
# esi-ui.write_waypoint.v1

# Leave this be.
ESI_SWAGGER_JSON = "https://esi.tech.ccp.is/latest/" \
    "swagger.json?datasource=tranquility"

# Change to the callback URL you made.
ESI_CALLBACK = "http://localhost/auth/callback"

# Your ESI app's client ID.
ESI_CLIENT_ID = ""

# Your ESI app's secret key.
ESI_SECRET_KEY = ""

# Your ESI app's "name".
ESI_USER_AGENT = ""


############################
# Extra Settings
############################

# Webhook URL for Discord notifications about reports. Comment out if you want to disable.
WEBHOOK_URL = ""
