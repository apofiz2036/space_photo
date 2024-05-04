import requests
import argparse
import general_functions as gf


def fetch_spacex_launch(id_flight='latest'):
    url = 'https://api.spacexdata.com/v5/launches/'
    response = requests.get(f'{url}{id_flight}')
    response.raise_for_status()
    launches = response.json()['links']['flickr']['original']

    for image_number, photo_url in enumerate(launches):
        gf.save_image(image_number, photo_url, name_photo='spacex')


parser = argparse.ArgumentParser(
    description='Находит и сохраняет фотографию с запусков SpaceX '
)

if __name__ == '__main__':
    parser.add_argument(
        '-i',
        '--id',
        default='latest',
        help='ID запуска SpaceX (по умолчанию последний запуск)'
    )

    args = parser.parse_args()

    fetch_spacex_launch(args.id)
