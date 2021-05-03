from django.contrib import admin

import polls.models
from .models import *

admin.site.register(Question)
admin.site.register(Choice)

# Register your models here.
