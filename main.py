# https://www.billboard.com/charts/hot-100/2000-08-12/ # En leri sıralayan site

import requests
from bs4 import BeautifulSoup

# Take year selection
year = input("What year you would like to travel to in YYYY-MM-DD format: ")

URL = f"https://www.billboard.com/charts/hot-100/{year}/"

# Siteden verileri html olarak alma
response = requests.get(URL)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser") # text to html encoding işlemi
sound_tags = soup.select(".o-chart-results-list__item .c-title")
# sound_tags = soup.find_all(name="h3",id="title-of-a-story", class_="c-title")
sound_names = [each.getText().strip() for each in sound_tags] # strip ile sondaki ve baştaki boşluklar kaldırılır


print(sound_names[0:10])



