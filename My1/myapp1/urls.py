from django.urls import path
from . import views
urlpatterns = [
    path('myapp1/', views.learn_django),
]