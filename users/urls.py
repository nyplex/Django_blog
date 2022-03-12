from django.urls import path
from . import views


urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>', views.user_profile, name='user_profile'),
    path('account', views.user_account, name='user_account'),
    
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_page, name='logout'),
]
