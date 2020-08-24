from django.urls import path
from first_app import views


urlpatterns = [
  path(r'', views.index, name='index'),
]