from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.UserLogin.as_view() , name='login'),
    path('register/',views.register , name='register'),
    path('buy_now/<int:id>/',views.buy_now , name='buy_now'),
    path('profile/',views.ProfileView.as_view() , name='profile'),
    path('logout/',views.user_logout , name='logout'), 
    path('profile/pass_change/',views.pass_change , name='pass_change'), 

]
