from django.urls import path
from . import views 

urlpatterns=[
    path('',views.home,name="home"),
    path('register/',views.register_user,name="register"),
    path('login/',views.login,name="login"),
    path('bus_ticket/',views.bus_ticket,name="bus_ticket"),
    path('book_hotel/',views.book_hotel,name="book_hotel"),
    path('profile/',views.profile,name="profile"),
    path('logout/',views.logout,name="logout")
]