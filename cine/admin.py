from django.contrib import admin

from . models import *
admin.site.register(Movie)
admin.site.register(Room)
admin.site.register(TimeTable)
admin.site.register(Client)
admin.site.register(Session)
# Register your models here.
