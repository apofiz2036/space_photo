import requests

import general_functions as gf


def fetch_spacex_launch(id_flight='latest'):
    url = 'https://api.spacexdata.com/v5/launches/'
    response = requests.get(f'{url}{id_flight}')
    response.raise_for_status()
    launches = response.json()['links']['flickr']['original']

    for image_number, photo_url in enumerate(launches):
        gf.save_image(image_number, photo_url, name_photo='spacex')
