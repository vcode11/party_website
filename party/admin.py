from django.contrib import admin

from .models import State, District, Member

admin.site.register(State)
admin.site.register(District)
admin.site.register(Member)
