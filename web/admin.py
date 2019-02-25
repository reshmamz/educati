from django.contrib import admin
from . import  models

# Register your models here.

admin.site.register(models.Gallery)
admin.site.register(models.Event)
admin.site.register(models.Career)
admin.site.register(models.Departments)
admin.site.register(models.Faculty)
admin.site.register(models.Courses)