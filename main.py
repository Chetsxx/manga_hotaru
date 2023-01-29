from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import requests
import time

FOLDER = ""
os.makedirs(FOLDER, exist_ok=True)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service("")
driver = webdriver.Chrome(options=options, service=service)
driver.maximize_window()

driver.get("")
driver.refresh()
time.sleep(10)

image = []

for x in range(50):
    time.sleep(2)
    image = driver.find_elements(By.CLASS_NAME, "zao-image")
    next = driver.find_element(By.CSS_SELECTOR, "body")
    next.send_keys(Keys.LEFT)


for x in image:
    url = x.get_attribute("src")
    file = url.split("/")[-1]
    filename = file.split("?")[0]
    print('url:', url)
    print('filename:', filename)
    print('-----')
    full_path = os.path.join(FOLDER, filename)
    print(full_path)

    response = requests.get(url)
    data = response.content
    with open(full_path, "wb") as fh:
        fh.write(response.content)



