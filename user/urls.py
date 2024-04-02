from django.urls import path

from user import views

urlpatterns = [
    path('regsiter/', views.user_signup, name="user_create"),
    path('login/', views.user_login, name="user_login"),
    path('user_info/{id}/', views.user_info, name="user_info")
]