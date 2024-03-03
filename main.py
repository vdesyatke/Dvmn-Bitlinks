import requests
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    token = os.environ.get('BITLY_TOKEN')
    url = input('Введите ссылку: ')
    if is_bitlink(url, token):
        try:
            clicks_count = count_clicks(token, url)
            print(f'Количество кликов {clicks_count}')
        except requests.exceptions.HTTPError as err:
            print(f'Введена неверная ссылка, подробности: {err}')
    else:
        try:
            print(shorten_link(token, url))
        except requests.exceptions.HTTPError as err:
            print(f'Введена неверная ссылка, подробности: {err}')


def shorten_link(token, url):
    headers = {'Authorization': f'Bearer {token}'}
    payload = {'long_url': url}
    bitly_url = 'https://api-ssl.bitly.com/v4/shorten'
    response = requests.post(bitly_url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token, url):
    counter_url = f'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(counter_url, headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(url, token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{url}',
        headers=headers,
    )
    return response.ok


if __name__ == '__main__':
    main()
