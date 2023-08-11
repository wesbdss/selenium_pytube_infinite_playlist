from pytube import YouTube
import requests
import os,sys
from bs4 import BeautifulSoup
import shutil

# YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
# yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
# yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')

browser = webdriver.Chrome(chrome_options=chrome_options)
def main(first_url = None, limit=200):
    
    browser.get(first_url)
    action = ActionChains(browser)

    _ = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "contents"))
        )

    # list_elems = browser.find_elements(By.TAG_NAME,"ytmusic-player-queue-item")
    # list_elems = [x for x in list_elems if x.text != '']
    # for elem in range(len(list_elems)):
    #     list_elems = browser.find_elements(By.TAG_NAME,"ytmusic-player-queue-item")
    #     list_elems = [x for x in list_elems if x.text != '']
    #     list_elems[elem].find_element(By.ID,"play-button").click()
    #     print(browser.current_url)
    body = browser.find_element(By.TAG_NAME,'body')
    body.send_keys("m")
    yt = YouTube(browser.current_url.split("&")[0].replace("music.",""))
    paste_name=yt.title
    while True:
        yt = YouTube(browser.current_url.split("&")[0].replace("music.",""))
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').first().download("./musics")
        try:
            os.mkdir("./musics/"+paste_name)
        except Exception as e:
            pass
        if(yt.title+".mp4" in os.listdir("./musics")):
            
            shutil.move("./musics/"+yt.title+".mp4","./musics/"+paste_name+"/"+yt.title+".mp4")
        body.send_keys(Keys.SHIFT +  "n")
        elem = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "contents"))
        )
        print("quantidade de musicas: ",len(os.listdir("./musics/"+paste_name)))
        if len(os.listdir("./musics/"+paste_name)) >= limit:
            break

if "__main__" == __name__:
    main(first_url=sys.argv[1],limit = int(sys.argv[2]))