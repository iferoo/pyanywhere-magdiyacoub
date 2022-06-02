from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Room)
admin.site.register(Bed)
admin.site.register(Patient)
