# Dvmn-Bitlinks
This program accepts one required positional argument, url.  
If this url is a bitlink, the program returns a count of clicks on this bitlink.  
If the url is not a bitlink, the program returns a bitlink for the submitted url.  
[About bit.ly service](https://bitly.com/pages/about).

## Installation
0. You need python interpreter installed on your PС. The project is tested on Python 3.10.
1. Clone the project to your PC, details [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
2. Install, run and activate your virtual environment, details [here](https://docs.python-guide.org/dev/virtualenvs/).
3. To install the dependencies, simply run ```pip install -r requirements.txt```.
4. Generate your bit.ly token [here](https://app.bitly.com/settings/api/)
5. In the root directory of the project create a new file named `.env` with an environment variable `BITLY_TOKEN={your_token_here}`.

## Examples of use
```python
>>>  python main.py bit.ly/3ULPH5U
Count of clicks is 5
```
```python
>>> python main.py https://www.yandex.ru
https://bit.ly/3ULPH5U
```
```python
>>> python main.py -h            
usage: main.py [-h] url

This program accepts one required positional argument, url. If this url is a bitlink, the program returns a count of clicks on this bitlink. If the     
url is not a bitlink, the program returns a bitlink for the submitted url.

positional arguments:
  url         Please enter a url

optional arguments:
  -h, --help  show this help message and exit
```

## License
This software is licensed under the MIT License - see the [LICENSE](https://github.com/vdesyatke/Dvmn-Weather/blob/master/LICENSE) file for details
