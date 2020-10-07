import telegram   #텔레그램 모듈을 가져옵니다.
import django.conf from settings

bot = telegram.Bot(token=settings.TELEGRAM_TOKEN)
bot.set_webhook('https://3c74a99fe5a8.ngrok.io/blog/webhook/')

# for update in bot.getUpdates(): 
#     print(update.message)