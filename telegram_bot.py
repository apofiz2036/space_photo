import telegram
import os

telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']

telegram_bot = telegram.Bot(token=telegram_bot_token)

telegram_bot.send_document(
    chat_id='@space_photo_Apofiz',
    document=open('images\\apod_nasa_0.jpg', 'rb')
)
