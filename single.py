import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.reddit.com/r/ShouChongTV/comments/xzo1an/%E3%81%82%E3%81%84/'
r = requests.get(url)
html = bs(r.content, 'html.parser')
ret = []
for link in html.find_all('a'):
  link = link.get('href')
  #ret += [link.get('href')]
print(ret)
