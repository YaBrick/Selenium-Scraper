from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

from bs4 import BeautifulSoup
import json

link = ''

#driver = webdriver.Chrome()


options = Options()
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

driver_service = Service()
driver = webdriver.Chrome(service=driver_service, options=options)
driver.get(link)

body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(20):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

page_html = driver.page_source

with open('page.html', 'w', encoding='utf-8') as file:
    file.write(page_html)
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

h3_tags = soup.find_all('h1')

data = {
    "h3": [tag.get_text() for tag in h3_tags],
}

with open('data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print("Данные успешно записаны в data.json")
