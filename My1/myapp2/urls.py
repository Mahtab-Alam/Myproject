from django.urls import path
from . import views
urlpatterns = [
    path('myapp2/', views.learn_django),
]