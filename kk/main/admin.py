from django.contrib import admin

from .models import User
from .models import Topic
from .models import Comment

admin.site.register(Comment)
admin.site.register(Topic)