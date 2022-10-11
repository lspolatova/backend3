from django.http import JsonResponse
from django.shortcuts import render
from error import error_not_get, error_not_post

chat = {'0': "chat0",
        '1': "chat1"}


@error_not_get
def chat_list(request):
    return JsonResponse(chat)


@error_not_get
def chat_page(request):
    chat_id = request.GET.get('id')
    return JsonResponse({chat_id: chat[chat_id]})


@error_not_post
def chat_create(request):
    chat_id = request.POST.get('id')
    chat[chat_id] = "chat" + chat_id
    return JsonResponse({chat_id: chat[chat_id]})


@error_not_get
def home_page(request):
    return render(request, 'home.html')
