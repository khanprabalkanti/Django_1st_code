from django.urls import path
from new import views

urlpatterns = [
    path('', views.new, name='new'),
]