import requests
from bs4 import BeautifulSoup


URL = 'https://pypi.org/'
header = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
page = requests.get(URL, header)
soup = BeautifulSoup(page.content, 'html.parser')
package_name = []
name = []
version = []
description = []
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
    package_name.append(f'{name[i]} {version[i]} \n{description[i]}')

for i in soup.find_all(attrs={'package-snippet'}):
    print(i.get('href'))