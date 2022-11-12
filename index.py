from pytube import YouTube
import requests
from bs4 import BeautifulSoup

# YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
# yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
# yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
browser.get('https://music.youtube.com/watch?v=fgXXwUsr2Ng&list=RDAMVMfgXXwUsr2Ng')
action = ActionChains(browser)

elem = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "contents"))
    )

# list_elems = browser.find_elements(By.TAG_NAME,"ytmusic-player-queue-item")
# list_elems = [x for x in list_elems if x.text != '']
# for elem in range(len(list_elems)):
#     list_elems = browser.find_elements(By.TAG_NAME,"ytmusic-player-queue-item")
#     list_elems = [x for x in list_elems if x.text != '']
#     list_elems[elem].find_element(By.ID,"play-button").click()
#     print(browser.current_url)
while True:
    yt = YouTube(browser.current_url.split("&")[0].replace("music.",""))
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download("./musics")
    body = browser.find_element(By.TAG_NAME,'body')
    body.send_keys(Keys.SHIFT +  "n")
    elem = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "contents"))
    )
    