from django.urls import path
from . import views 

urlpatterns=[
    path('',views.user_login,name='login'),
    path('register',views.register,name='register'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('reset_password/',views.reset_password,name='reset_password')
]