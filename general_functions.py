import requests
import urllib.parse
from os.path import splitext
from pathlib import Path


def save_image(image_number, photo_url, name_photo, file='jpg'):
    Path('images').mkdir(parents=True, exist_ok=True)
    filename = Path(f'images/{name_photo}_{image_number}.{file}')
    image_number += 1
    response = requests.get(photo_url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def file_extension(url_photo):
    part_of_link = urllib.parse.urlsplit(urllib.parse.unquote(url_photo))[2]
    filename = splitext(part_of_link)[1]
    return filename[1:]