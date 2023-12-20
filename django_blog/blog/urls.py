from django.urls import path
from blog import views

urlpatterns = [
    path('login', views.login),
    path('home', views.home),
    path('newpost', views.newPost),
    path('mypost', views.myPost),
    path('signout', views.signout),
    path('', views.signup),
]
