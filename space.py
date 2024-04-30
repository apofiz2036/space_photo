import requests
import urllib.parse
import os
from os.path import splitext
from pathlib import Path

nasa_token = os.environ['NASA_TOKEN']


def save_image(image_number, photo_url, name_photo, file='jpg'):
    Path('images').mkdir(parents=True, exist_ok=True)
    filename = Path(f'images/{name_photo}_{image_number}.{file}')     #aghzfhaefetj
    image_number += 1
    response = requests.get(photo_url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_launch():
    url = 'https://api.spacexdata.com/v5/launches/'
    id_flight = '5eb87d47ffd86e000604b38a'
    response = requests.get(f'{url}{id_flight}')
    response.raise_for_status()
    launches = response.json()['links']['flickr']['original']

    for image_number, photo_url in enumerate(launches):
        save_image(image_number, photo_url, name_photo='spacex')


def nasa_photo():
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': nasa_token, 'count': 30}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    data = [i['url'] for i in response.json()]                    
    for image_number, photo_url in enumerate(data):
        save_image(image_number, photo_url, name_photo='apod_nasa', file=file_extension(photo_url))


def nasa_epic_photo():
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {'api_key': nasa_token}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    data = response.json()
    list_photo = []

    for photo in data:
        image = photo['image']
        date = photo['date'].split()[0]
        t = (image, date)
        list_photo.append(t)

    name_file = []
    year = []
    month = []
    day = []

    for photo in list_photo:
        name_file.append(photo[0])
        year.append(photo[1].split('-')[0])
        month.append(photo[1].split('-')[1])
        day.append(photo[1].split('-')[2])

    data = [] 

    for number in range(5):
        url = 'https://api.nasa.gov/EPIC/archive/natural'
        payload = {'api_key': nasa_token}
        response = requests.get(f'{url}/{year[number]}/{month[number]}/{day[number]}/png/{name_file[number]}.png', params=payload)
        data.append(response.url)

    for image_number, photo_url in enumerate(data):
        save_image(image_number, photo_url, name_photo='epic_nasa', file='png')

def file_extension(url_photo):
    part_of_link = urllib.parse.urlsplit(urllib.parse.unquote(url_photo))[2]
    filename = splitext(part_of_link)[1]
    return filename[1:]

nasa_photo()