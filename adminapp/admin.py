from django.contrib import admin
from .models import *
#register your models
admin.site.register(News)
admin.site.register(Branch)
admin.site.register(Course)
admin.site.register(Session)
admin.site.register(study)
