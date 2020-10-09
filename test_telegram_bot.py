import telegram
from telegram_django_bot import settings

bot = telegram.Bot(token=settings.TELEGRAM_TOKEN)
bot.set_webhook('https://9dad9fef93ae.ngrok.io/recommend/Service/')

# for update in bot.getUpdates(): 
#     print(update.message)