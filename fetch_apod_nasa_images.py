import requests
import os
import argparse
import general_functions as gf
from dotenv import load_dotenv


def nasa_photo():
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': nasa_token, 'count': args.count}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    data = [i['url'] for i in response.json()]
    for image_number, photo_url in enumerate(data):
        gf.save_image(
            image_number, photo_url,
            name_photo='apod_nasa', file=gf.file_extension(photo_url)
        )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Находит и сохраняет фото дня с сайта API NASA'
    )

    parser.add_argument(
        '-c',
        '--count',
        type=int,
        default=30,
        help='Количество загружаемых изображений, по умолчанию 30'
    )

    args = parser.parse_args()

    nasa_photo()
