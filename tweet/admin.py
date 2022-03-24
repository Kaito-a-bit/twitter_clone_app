from unittest.mock import AsyncMockMixin
from django.contrib import admin
from .models import tweet

admin.site.register(tweet)

