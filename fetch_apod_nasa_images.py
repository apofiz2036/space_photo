import requests
import os
import argparse
import general_functions as gf
from dotenv import load_dotenv


def get_nasa_photo(nasa_token, count):
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': nasa_token, 'count': count}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    image_urls = [i['url'] for i in response.json()]
    for image_number, photo_url in enumerate(image_urls):
        gf.save_image(
            image_number, photo_url,
            name_photo='apod_nasa', file=gf.get_file_extension(photo_url)
        )


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']

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

    get_nasa_photo(nasa_token, args.count)
