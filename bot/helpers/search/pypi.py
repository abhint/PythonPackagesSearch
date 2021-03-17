import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}


def default_pip():
    URL = 'https://pypi.org/'
    page = requests.get(URL, headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    package_name = []
    name = []
    version = []
    description = []
    link = []
    # package name
    for i in soup.find_all(attrs={'package-snippet__name'}):
        name.append(i.string)

    # package version
    for i in soup.find_all(attrs={'package-snippet__version'}):
        version.append(i.string)

    # package description
    for i in soup.find_all(attrs={'package-snippet__description'}):
        description.append(i.string)

    # inserting package name and version
    for i in range(len(name)):
        package_name.append(f'{name[i]} {version[i]}')

    # package link
    for i in soup.find_all(attrs={'package-snippet'}):
        link.append(f"https://pypi.org{i.get('href')}")

    return package_name, description, link


def pip_search(query):
    URL = f"https://pypi.org/search/?o=&q={query}&page=1"
    page = requests.get(URL, headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    package_name = []
    name = []
    version = []
    description = []
    link = []
    # package name
    for i in soup.find_all(attrs={'package-snippet__name'}):
        name.append(i.string)

    # package version
    for j in soup.find_all(attrs={'package-snippet__version'}):
        version.append(j.string)

    # package description
    for x in soup.find_all(attrs={'package-snippet__description'}):
        description.append(x.string)

    # Insertign Package Name & Version
    for i in range(len(name)):
        package_name.append(f"{name[i]} {version[i]}")

    # package link
    for i in soup.find_all(attrs={'package-snippet'}):
        link.append(f"https://pypi.org{i.get('href')}")

    return package_name , description, link
