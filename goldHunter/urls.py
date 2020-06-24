from django.urls import path
from . import views


urlpatterns = [
  path('', views.index),
  path('show_gold', views.show_gold),
  path('process', views.process),
  path('reset', views.reset)
]