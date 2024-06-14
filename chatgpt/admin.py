from django.contrib import admin
from .models import ChatHistory
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta

admin.site.register(ChatHistory)