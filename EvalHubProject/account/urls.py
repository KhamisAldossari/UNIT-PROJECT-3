from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [

    path('register/', views.register_user_view, name='register_user_view'),
    path('login/', views.login_user_view, name='login_user_view'),
    path('logout/', views.logout_user_view, name='logout_user_view'),
    path('profile/<int:user_id>/', views.user_profile_view, name='user_profile_view'),
    path('update_profile/', views.update_user_view, name='update_user_view'),
    
]
