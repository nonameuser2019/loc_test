import requests
from bs4 import BeautifulSoup


url = 'https://www.dtcdecode.com/Acura'

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response
    print(f'Error status code is {response.status_code}')


def parser(response):
    soup = BeautifulSoup(response.content, 'html.parser')
    code_list = soup.find('ul', class_='ulCode').find_all('li')
    for link in code_list:
        print(link.find('a')['href'])


if __name__ == '__main__':
    parser(get_html(url))