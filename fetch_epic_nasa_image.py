import requests
import os

import general_functions as gf

nasa_token = os.environ['NASA_TOKEN']


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
        response = requests.get(
            f'{url}/{year[number]}/{month[number]}/{day[number]}/png/{name_file[number]}.png',
            params=payload
        )
        data.append(response.url)

    for image_number, photo_url in enumerate(data):
        gf.save_image(
            image_number,
            photo_url,
            name_photo='epic_nasa',
            file='png'
        )
