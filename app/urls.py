from django.urls import path

from user import views

urlpatterns = [
    path('show/', views.app_show, name="app_show"),
]