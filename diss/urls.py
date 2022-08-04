from django.urls import path
from diss import views
app_name = 'diss'
urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.map, name='map'),
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),
    path('events/', views.events, name='events'),

]

