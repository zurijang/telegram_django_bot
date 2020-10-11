import json
import telegram
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from .tasks import LoadData
from .models import Data


# Create your views here.

bot = telegram.Bot(token=settings.TELEGRAM_TOKEN)

def index(request):
    return HttpResponse("여행 추천 서비스")


@csrf_exempt
def service2(request):
    json_string = request.body
    telegram_update = json.loads(json_string)

    received_text = telegram_update["message"]["text"]
    reply_text = ''

    try:
        state, province, type1 = received_text.split(',')
    except ValueError:
        reply_text = "Please input state, province, type1."
    else:
        qs = Data.objects.all()\
            .annotate(score = F('rank') * 1.55 + F('search_count') * 0.025)\
            .filter(state=state, province=province, type1=type1)\
            .order_by('-score')
        place_name_list = qs[:5].values_list('name', flat=True)
        reply_text = '\n'.join(place_name_list)

    chat_id = telegram_update["message"]["chat"]["id"]
    bot.sendMessage(chat_id=chat_id, text=text)

    return HttpResponse("ok")


@csrf_exempt  # CSRF 체킹을 하지 말라.
# @require_POST # Decorator (장식자)
def Service(request):
    # TODO: request.method == 'POST' 검사
    # TODO: request.method['HTTP_REFERER']를 통한 Telegram에 의한 요청인지 검사

    json_string = request.body
    telegram_update = json.loads(json_string)

    received_text = telegram_update["message"]["text"]
    text_to_list = received_text.split(',')
    text = ""
    if len(text_to_list)==3:
        recommend_data = LoadData(text_to_list[0], text_to_list[1], text_to_list[2])[0:5]
        row_list = []
        for index, row in recommend_data.iterrows():
            my_list = [row.검색지명, row.링크]
            row_list.append(my_list)
        
        for row in row_list:
            text += '이름 : ' + row[0] + ', 카카오맵 : ' + row[1] + "\n"
        # text = 'Wow'

    else:
        text = "Please input state, province, type1."

    chat_id = telegram_update["message"]["chat"]["id"]
    bot.sendMessage(chat_id=chat_id, text=text)

    return HttpResponse("ok")