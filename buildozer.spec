[app]
title = DEPORT
package.name = deport
package.domain = org.justifiedreasoning
source.dir = .
source.include_exts = py,png,jpg,kv
version = 1.9
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow
orientation = portrait
fullscreen = 0
icon.filename = icon.png

[android]
android.api = 36
android.minapi = 24
android.ndk = 25b
android.build_tools = 34.0.0
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,READ_MEDIA_IMAGES,READ_MEDIA_VIDEO,READ_MEDIA_AUDIO
android.arch = arm64-v8a
android.enable_16kb_page_size = True
