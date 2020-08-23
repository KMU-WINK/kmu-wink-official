from django.contrib import admin
from .models import User, Emoji
# Register your models here.

admin.site.register(User)
admin.site.register(Emoji)