import requests
from bs4 import BeautifulSoup
import pprint
from modules.ztm_scraping_functions import create_custom_hackernews


URL = 'https://news.ycombinator.com/news'
PARSER_MODE = 'html.parser'
TOTAL_PAGES = 5
links = []
subtext = []

for i in range(TOTAL_PAGES + 1):
  res = requests.get(f'{URL}?p={i}')
  soup = BeautifulSoup(res.text, PARSER_MODE)
  links += soup.select('.titlelink')
  subtext += soup.select('.subtext')

hn = create_custom_hackernews(links, subtext)
pprint.pprint(hn)


'EOF'
