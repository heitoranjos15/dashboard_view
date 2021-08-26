from django.urls import path
from . import views
urlpatterns = [
    path('facebook', views.facebook),
    path('twitter', views.twitter),
    path('instagram', views.instagram),

]
