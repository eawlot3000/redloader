import requests
from bs4 import BeautifulSoup as bs

#mean = input('sub url input')
user = 'https://www.reddit.com/r/Roleplaybuddy/' 

r = requests.get(user)
html = bs(r.content, 'html.parser')
ret = []
for link in html.find_all('img'):
  print(link)
  #print(link.get('src'))
'''
for link in html.find_all('img'):
  link = link.get('href')
  if 'preview' and 'jpg' in link:
    ret += [link]
print(ret)

'''
