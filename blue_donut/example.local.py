# flake8: noqa

import os

from .settings import *

############################
# Django Settings
############################

# https://randomkeygen.com/
SECRET_KEY = ""

# Make sure to not run a production server with debug on.
DEBUG = True
SEND_ROUTE = False

# Add your domain name here.
ALLOWED_HOSTS = []

# I wouldn't modify the database location, but it's up to you.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

############################
# ESI Settings
############################

# Go to https://developers.eveonline.com/applications and make an application.

# Leave this be.
ESI_SWAGGER_JSON = "https://esi.tech.ccp.is/latest/", \
    "swagger.json?datasource=tranquility"

# Change to the callback URL you made.
ESI_CALLBACK = ""

# Your ESI app's client ID.
ESI_CLIENT_ID = ""

# Your ESI app's secret key.
ESI_SECRET_KEY = ""

# Your ESI app's "name".
ESI_USER_AGENT = ""


# Stuff doesn't work with STATIC_ROOT set to the same directory as STATICFILES_DIRS.
if DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, "static_root")
else:
    STATIC_ROOT = os.path.join(BASE_DIR, "static")


############################
# Extra Settings
############################

# Webhook URL for Discord notifications about reports. Comment out if you want to disable.
REPORT_WEBHOOK = "https://discordapp.com/api/webhooks/647096557669187609/XBxdtSoMNU1S5K4Nko0UQ8-ov1BRgd7u-GKlXcD1NZqvP4pzK1Ge6jXN30TvmyUQT5Z_"
FEEDBACK_WEBHOOK = "https://discordapp.com/api/webhooks/691452521658712125/QoePtNxR1s-3Lxn_3nduyjLe7a7eD92UvJBWW_KAz7INN-rvTPSAIL5Te3Z1fX0z__nz"
