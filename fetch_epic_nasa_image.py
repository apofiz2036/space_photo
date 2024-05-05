import requests
import os
import argparse
import general_functions as gf
from dotenv import load_dotenv


def get_nasa_epic_photo(url_api, url_archive):
    payload = {'api_key': nasa_token}
    response = requests.get(url_api, params=payload)
    response.raise_for_status()
    epic_photos = response.json()
    photos = []

    for photo in epic_photos:
        image = photo['image']
        date = photo['date'].split()[0]
        image_date = (image, date)
        photos.append(image_date)

    name_file = []
    year = []
    month = []
    day = []

    for photo in photos:
        name_file.append(photo[0])
        year.append(photo[1].split('-')[0])
        month.append(photo[1].split('-')[1])
        day.append(photo[1].split('-')[2])

    image_download_urls = []

    for number in range(args.count):
        payload = {'api_key': nasa_token}
        response = requests.get(
            f'{url_archive}/{year[number]}/{month[number]}/{day[number]}/png/{name_file[number]}.png',
            params=payload
        )
        image_download_urls.append(response.url)

    for image_number, photo_url in enumerate(image_download_urls):
        gf.save_image(
            image_number,
            photo_url,
            name_photo='epic_nasa',
            file='png'
        )


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']

    url_api = 'https://api.nasa.gov/EPIC/api/natural/images'
    url_archive = 'https://api.nasa.gov/EPIC/archive/natural'

    parser = argparse.ArgumentParser(
        description='Находит и сохраняет EPIC фото с сайта API NASA'
    )

    parser.add_argument(
        '-c',
        '--count',
        type=int,
        default=10,
        help='Количество загружаемых изображений, по умолчанию 10'
    )

    args = parser.parse_args()

    get_nasa_epic_photo(url_api, url_archive)
