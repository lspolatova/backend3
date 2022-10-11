from django.urls import path

from chats.views import chat_list, chat_page, chat_create, home_page

urlpatterns = [
    path('', chat_list, name='chat_list'),
    path('page/', chat_page, name='chat_page'),
    path('create/', chat_create, name='chat_create'),
    path('home/', home_page, name='home_page'),
]
