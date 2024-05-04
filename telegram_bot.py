import os
import telegram
import random
import time
import argparse
from dotenv import load_dotenv

load_dotenv()
telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
telegram_bot = telegram.Bot(token=telegram_bot_token)


parser = argparse.ArgumentParser(
    description='Отправляет изображения из папки "image" в телеграмм'
)

parser.add_argument(
    '-t',
    '--telegram_timer',
    type=int,
    default=14400,
    help='Через сколько секунд отправлять сообщение'
)
args = parser.parse_args()


def send_image(telegram_timer):
    for photo in os.walk('images'):
        files_list = photo[2]

    random.shuffle(files_list)

    while True:
        for photo in files_list:
            time.sleep(telegram_timer)
            telegram_bot.send_document(
                chat_id='@space_photo_Apofiz',
                document=open(f'images\\{photo}', 'rb')
            )


if __name__ == '__main__':
    send_image(args.telegram_timer)
