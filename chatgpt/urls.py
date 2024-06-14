# blog/urls.py
from django.urls import path
from django.contrib import admin
from . import views
from .views import chat_history_view

app_name = 'chatgpt'
urlpatterns = [

    path('', views.index, name='index'),
    path('chat', views.chat, name='chat'),
    path('chating', views.chating, name='chating'), 
    path('new_chat/', views.new_chat, name='new_chat'),
    path('reset', views.reset, name='reset'),
    path('signup', views.signup_view, name='signup'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('chathistory/', chat_history_view, name='chat_history'),
]
