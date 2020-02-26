from django.urls import path
from votingapp import views

app_name='votingapp'



urlpatterns=[
    path('user_login/',views.user_login,name='user_login'),
    path('register/',views.user_register,name='register'),
    path('logout/',views.user_logout,name='logout'),
    path('vote/',views.voting,name='vote'),
]