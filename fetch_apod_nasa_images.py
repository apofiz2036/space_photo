import requests
import os

import general_functions as gf


nasa_token = os.environ['NASA_TOKEN']


def nasa_photo():
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': nasa_token, 'count': 5}  # Исправить кол-во фото
    response = requests.get(url, params=payload)
    response.raise_for_status()
    data = [i['url'] for i in response.json()]
    for image_number, photo_url in enumerate(data):
        gf.save_image(
            image_number, photo_url,
            name_photo='apod_nasa', file=gf.file_extension(photo_url)
        )
