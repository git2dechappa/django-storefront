from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.say_hello),
    path("fees/", views.show_fees)

]