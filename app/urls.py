from django.urls import path

from app import views

urlpatterns = [
    path('show/', views.app_show, name="app_show"),
    path('like/', views.click_like,name="click_like"),
    path('reserve/', views.click_reserve,name="click_reserve")

]