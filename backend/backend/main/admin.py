from django.contrib import admin

# Register your models here.

from backend.main.models import User, Hashtag, Subscription, Queue, Analysis

admin.site.register(User)
admin.site.register(Hashtag)
admin.site.register(Subscription)
admin.site.register(Queue)
admin.site.register(Analysis)
