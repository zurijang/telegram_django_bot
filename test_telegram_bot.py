import telegram
from telegram_django_bot import settings

bot = telegram.Bot(token=settings.TELEGRAM_TOKEN)
bot.set_webhook('https://319c3bdce557.ngrok.io/recommend/Service/')

# for update in bot.getUpdates(): 
#     print(update.message)