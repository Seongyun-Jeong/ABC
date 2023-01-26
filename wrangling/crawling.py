from bs4 import BeautifulSoup
import requests
import argparse

url = "https://comic.naver.com/webtoon/weekday"
# print("Target url:", url)

# Call HTML from url
contents = []
raw = requests.get(url)
raw_html = BeautifulSoup(raw.text, "html.parser")
cartoonsBox = raw_html.find('div', attrs={"class": "list_area daily_all"})

# Get all "a" tag and "title" class contents from HTML
webtoons = (cartoonsBox.find_all('a', class_='title'))
for i in webtoons:
    print(i)
