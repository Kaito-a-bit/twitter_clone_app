from django.contrib import admin
from .models import Tweet, LikeModel

admin.site.register(Tweet)
admin.site.register(LikeModel)

