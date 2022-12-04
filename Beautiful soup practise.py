import requests
import bs4

resours = requests.get('https://en.wikipedia.org/wiki/RMS_Queen_Mary')
soup = bs4.BeautifulSoup(resours.text, 'lxml')
#  print(soup)
# for item in soup.select('.toctext'):
#     print(item.text)
    
# print(soup.select('.thumbimage'))
build_ship = soup.select('.thumbimage')[1]
link = requests.get('https:' + build_ship['src'])
print(link.content)
image = open('build.ship.jpg', 'wb')
image.write(link.content)
image.close()