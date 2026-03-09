[app]
title = Cypher
package.name = cypher
package.domain = org.lilpeachbat
source.dir = .
# Added 'spec' and 'txt' just to be safe
source.include_exts = py,png,jpg,ttf,json,spec,txt
version = 1.0

# These are correct for your encryption app
requirements = python3,kivy,requests,cryptography,openssl,urllib3,certifi,idna,charset-normalizer

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.allow_backup = True

# TEST FIX: We are commenting this out to prove the code works first. 
# Once you get a green checkmark, we will fix the PNG and put this back.
# icon.filename = CYPHER.png

# THE BIG FIX: These lines ensure the Android bouncer lets you through
android.accept_sdk_license = True
android.skip_update = False
android.warn_on_root = False

[buildozer]
log_level = 2
warn_on_root = 1
