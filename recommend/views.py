import json
import telegram
from django.shortcuts import render
from django.http import HttpResponse
from .tasks import LoadData
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

bot = telegram.Bot(token=settings.TELEGRAM_TOKEN)

def index(request):
    return HttpResponse("여행 추천 서비스")

@csrf_exempt
def Service(request):
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