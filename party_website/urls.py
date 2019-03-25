from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('party.urls')),
    re_path(r'^select2/', include('django_select2.urls')),
]
