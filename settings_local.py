# -*- coding: utf8 -*-
# This file is part of PyBossa.
#
# Copyright (C) 2013 SF Isle of Man Limited
#
# PyBossa is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBossa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBossa.  If not, see <http://www.gnu.org/licenses/>.
DEBUG = True

## webserver host and port
HOST = '0.0.0.0'
SERVER_NAME = 'localhost'
PORT = 8080

SECRET = '{{SECRET}}'
SECRET_KEY = '{{SECRET_KEY}}'

SQLALCHEMY_DATABASE_URI = '{{POSTGRES_URL}}'

ITSDANGEROUSKEY = '{{ITSDANGEROUSKEY}}'

## project configuration
BRAND = 'PyBossa'
TITLE = 'PyBossa'
LOGO = 'default_logo.svg'
COPYRIGHT = 'PyBossa'
DESCRIPTION = 'Your description'
TERMSOFUSE = 'http://okfn.org/terms-of-use/'
DATAUSE = 'http://opendatacommons.org/licenses/by/'
CONTACT_EMAIL = '{{DEFAULT_EMAIL}}'
CONTACT_TWITTER = 'PyBossa'

## Default number of projects per page
## APPS_PER_PAGE = 20

## External Auth providers
# TWITTER_CONSUMER_KEY=''
# TWITTER_CONSUMER_SECRET=''
# FACEBOOK_APP_ID=''
# FACEBOOK_APP_SECRET=''
# GOOGLE_CLIENT_ID=''
# GOOGLE_CLIENT_SECRET=''

## Supported Languages
## NOTE: You need to create a symbolic link to the translations folder, otherwise
## this wont work.
# @TODO move this command to dockerfiles
# ln -s pybossa/themes/your-theme/translations pybossa/translations
DEFAULT_LOCALE = 'en'
LOCALES = [('en', 'English'), ('de', 'Deutsch')]
#LOCALES = [('en', 'English'), ('es', u'Español'),
#           ('it', 'Italiano'), ('fr', u'Français'),
#           ('ja', u'日本語'),('pt_BR','Brazilian Portuguese')]


## list of administrator emails to which error emails get sent
ADMINS = ['{{DEFAULT_EMAIL}}']

## CKAN URL for API calls
#CKAN_NAME = "Demo CKAN server"
#CKAN_URL = "http://demo.ckan.org"


## logging config
# Sentry configuration
# SENTRY_DSN=''
## set path to enable
LOG_FILE = '/opt/pybossa/logs.txt'
## Optional log level
import logging
LOG_LEVEL = logging.DEBUG

## Mail setup
# MAIL_SERVER = 'localhost'
# MAIL_USERNAME = '{{DEFAULT_EMAIL}}'
# MAIL_PASSWORD =  '{{MAIL_PASSWORD}}'
# MAIL_PORT = 587
# MAIL_FAIL_SILENTLY = True
# MAIL_DEFAULT_SENDER = 'PyBossa Support <info@pybossa.com>'
# MAIL_USE_TLS = True

## Announcement messages
## Use any combination of the next type of messages: root, user, and app owners
## ANNOUNCEMENT = {'admin': 'Root Message', 'user': 'User Message', 'owner': 'Owner Message'}

## Enforce Privacy Mode, by default is disabled
## This config variable will disable all related user pages except for admins
## Stats, top users, leaderboard, etc
ENFORCE_PRIVACY = False


## Cache setup. By default it is enabled
## Redis Sentinel
# List of Sentinel servers (IP, port)
REDIS_CACHE_ENABLED = True
REDIS_SENTINEL = [('{{REDIS_SENTINEL}}', 26379)]
REDIS_MASTER = '{{REDIS_MASTER}}'
REDIS_DB = 0
REDIS_KEYPREFIX = 'pybossa_cache'
REDIS_SOCKET_TIMEOUT = None
REDIS_RETRY_ON_TIMEOUT = True
REDIS_URL = 'redis://{{REDIS_MASTER}}:6379'
REDIS_HOST = '{{REDIS_MASTER}}'

## Allowed upload extensions
ALLOWED_EXTENSIONS = ['js', 'css', 'png', 'jpg', 'jpeg', 'gif', 'zip']

## If you want to use the local uploader configure which folder
UPLOAD_METHOD = 'local'
UPLOAD_FOLDER = 'uploads'

## If you want to use Rackspace for uploads, configure it here
# RACKSPACE_USERNAME = 'username'
# RACKSPACE_API_KEY = 'apikey'
# RACKSPACE_REGION = 'ORD'

## Default number of users shown in the leaderboard
# LEADERBOARD = 20
## Default shown presenters
# PRESENTERS = ["basic", "image", "sound", "video", "map", "pdf"]
# Default Google Docs spreadsheet template tasks URLs
TEMPLATE_TASKS = {}

# Expiration time for password protected project cookies
PASSWD_COOKIE_TIMEOUT = 60 * 30

# Expiration time for account confirmation / password recovery links
ACCOUNT_LINK_EXPIRATION = 5 * 60 * 60

## Ratelimit configuration
# LIMIT = 300
# PER = 15 * 60

# Disable new account confirmation (via email)
ACCOUNT_CONFIRMATION_DISABLED = True

# Mailchimp API key
# MAILCHIMP_API_KEY = "your-key"
# MAILCHIMP_LIST_ID = "your-list-ID"

# Flickr API key and secret
# FLICKR_API_KEY = 'your-key'
# FLICKR_SHARED_SECRET = 'your-secret'

# Dropbox app key
# DROPBOX_APP_KEY = 'your-key'

# Send emails weekly update every
# WEEKLY_UPDATE_STATS = 'Sunday'

# Youtube API server key
# YOUTUBE_API_SERVER_KEY = 'your-key'

# Enable Server Sent Events
# WARNING: this will require to run PyBossa in async mode. Check the docs.
# WARNING: if you don't enable async when serving PyBossa, the server will lock
# WARNING: and it will not work. For this reason, it's disabled by default.
# SSE = False

# Add here any other ATOM feed that you want to get notified.
NEWS_URL = ['https://github.com/pybossa/enki/releases.atom', 
            'https://github.com/pybossa/pybossa-client/releases.atom',
            'https://github.com/pybossa/pbs/releases.atom']

# Pro user features. False will make the feature available to all regular users,
# while True will make it available only to pro users
PRO_FEATURES = {
    'auditlog':              True,
    'webhooks':              True,
    'updated_exports':       True,
    'notify_blog_updates':   True,
    'project_weekly_report': True,
    'autoimporter':          True,
    'better_stats':          True
}

# Libsass style. You can use nested, expanded, compact and compressed
LIBSASS_STYLE = 'compressed'

# CORS resources configuration.
# WARNING: Only modify this if you know what you are doing. The below config
# are the defaults, allowing PYBOSSA to have full CORS api. 
# For more options, check the Flask-Cors documentation: https://flask-cors.readthedocs.io/en/latest/
# CORS_RESOURCES = {r"/api/*": {"origins": "*",
#                               "allow_headers": ['Content-Type',
#                                                 'Authorization'],
#                               "methods": "*"
#                               }}

# Email notifications for background jobs.
FAILED_JOBS_MAILS = 7
FAILED_JOBS_RETRIES = 3

# Language to use stems, full text search, etc. from postgresql.
# FULLTEXTSEARCH_LANGUAGE = 'english'

# A 32 char string for AES encryption of public IPs.
#CRYPTOPAN_KEY =  '{{CRYPTOPAN_KEY}}'
CRYPTOPAN_KEY = '32-char-str-for-AES-key-and-pad.'


# TTL for ZIP files of personal data
TTL_ZIP_SEC_FILES = 3

# Instruct PYBOSSA to generate HTTP or HTTPS 
PREFERRED_URL_SCHEME='https'

# Inactive users months to send email notification
USER_INACTIVE_NOTIFICATION = 5
# Inactive users months to delete users
USER_INACTIVE_DELETE = 6
