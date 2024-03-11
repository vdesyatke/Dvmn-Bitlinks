import requests
import os
from dotenv import load_dotenv
import argparse


def main():
    load_dotenv()
    token = os.environ.get('BITLY_TOKEN')
    parser = create_parser()
    url = parser.parse_args().url

    if is_bitlink(url, token):
        try:
            clicks_count = count_clicks(token, url)
            print(f'Count of clicks is {clicks_count}')
        except requests.exceptions.HTTPError as err:
            print(f'You have entered incorrect url, details: {err}')
    else:
        try:
            print(shorten_link(token, url))
        except requests.exceptions.HTTPError as err:
            print(f'You have entered incorrect url, details: {err}')


def create_parser():
    description = '''This program accepts one required positional argument, url.\n
    If this url is a bitlink, the program returns a count of clicks on this bitlink.\n
    If the url is not a bitlink, the program returns a bitlink for the submitted url.'''
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('url', help='Please submit a url')
    return parser


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
