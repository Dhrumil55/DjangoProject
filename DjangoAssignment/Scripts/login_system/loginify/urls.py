from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world),  # Example URL
    path('template/',views.hello_world_loginify),
    path('all-data/',views.all_data),
    path('signup/', views.signup),
    path('login/', views.login),
    path('sud/<str:email>/',views.single_user_data),
]
