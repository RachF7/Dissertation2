from django.urls import path
from diss import views
app_name = 'diss'
urlpatterns = [
    path('', views.index, name='index'),
      path('map/', views.map, name='map')
    ]
