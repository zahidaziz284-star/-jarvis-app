[app]
title = JARVIS
package.name = jarvis
package.domain = com.zahid.jarvis
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0,kivymd,plyer,requests,android
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
android.permissions = INTERNET,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 24
android.accept_sdk_license_agreement = True
android.archs = arm64-v8a, armeabi-v7a
