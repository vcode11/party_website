from django.urls import path
from . import views

app_name = 'party'

urlpatterns = [
          path('', views.home, name='home'), 
          path('apply/',views.apply, name='apply')
]