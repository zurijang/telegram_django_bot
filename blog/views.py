import json
import telegram
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render, resolve_url
from .tasks import get_zum_realtime_keywords
from .models import Post

# Create your views here.

bot = telegram.Bot(token=settings.TELEGRAM_TOKEN)


def index(request):
    return HttpResponse("hello django")


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post,})


@csrf_exempt
def webhook(request):
    json_string = request.body
    telegram_update = json.loads(json_string)

    received_text = telegram_update["message"]["text"]

    if received_text == "실검":
        keyword_list = get_zum_realtime_keywords()  # list -> str
        # 1안 : Django 템플릿 엔진을 활용해서 문자열 생성
        # 2안
        text = "\n".join(keyword_list)

    elif received_text == "내역":
        # text_list = []
        # text = '\n'.join(post.title for post in Post.objects.all())
        # 2안
        # for post in Post.objects.all():
        #     post.title
        #     resolve_url(post)
        #     raw_text = ''
        text = ""
        for post in Post.objects.all():
            post_url = request.build_absolute_uri(resolve_url(post))
            text += f"""{post.title}
{post_url}
"""
    else:
        text = "ECHO)" + received_text

    chat_id = telegram_update["message"]["chat"]["id"]
    bot.sendMessage(chat_id=chat_id, text=text)

    return HttpResponse("ok")
