import os
import telegram
import random
import time
import argparse
from dotenv import load_dotenv


def send_image(telegram_timer, id):
    for photo in os.walk('images'):
        files_list = photo[2]

    random.shuffle(files_list)

    while True:
        for photo in files_list:
            time.sleep(telegram_timer)
            with open(f'images\\{photo}', 'rb'):
                telegram_bot.send_document(
                    chat_id=id,
                    document=open(f'images\\{photo}', 'rb')
                )


if __name__ == '__main__':
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

    parser.add_argument(
        '--id',
        type=str,
        default='@space_photo_Apofiz',
        help='Id чата, по умолчанию "@space_photo_Apofiz"'
    )

    args = parser.parse_args()

    send_image(args.telegram_timer, args.id)
