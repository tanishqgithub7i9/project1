from django.contrib import admin
from .models import Admin
from .models import Student,login
# Register your models here.
admin.site.register(Admin)
admin.site.register(Student)
admin.site.register(login)