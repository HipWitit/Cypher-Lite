[app]
# This is the name that will display on your phone's home screen
title = Cypher Lite
package.name = cypher
package.domain = org.lilpeachbat
source.dir = .

# Added 'spec' and 'txt' just to be safe
source.include_exts = py,png,jpg,ttf,json,spec,txt
version = 1.0

# These are correct for your encryption app
requirements = python3,kivy==2.3.0,requests,cryptography,openssl,urllib3,certifi,idna,charset-normalizer

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.allow_backup = True

# Explicitly pin the API and NDK to prevent Gradle/Java crashes
android.api = 33
android.minapi = 21
android.ndk = 25b

# App Icon
icon.filename = CYLI.png

# Grant the app permission to send and receive data over the web
android.permissions = INTERNET

# THE BIG FIX: These lines ensure the Android bouncer lets you through
android.accept_sdk_license = True
android.skip_update = False

[buildozer]
log_level = 2
