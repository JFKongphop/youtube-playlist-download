from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from pytube import Playlist, YouTube
import time

playlistUrl = ""
playlist = Playlist(playlistUrl)
videoUrls = playlist.video_urls

for url in videoUrls:
    target = webdriver.Chrome(ChromeDriverManager().install())
    target.get("https://tomp3.cc/enz8n9h")
    # target.set_window_size(100,600)
    target.find_element("id", "k__input").send_keys(url)
    target.find_element("id", "btn-start").click()

    try :
        locationWait = EC.presence_of_element_located((By.ID, "btn-convert"))
        convertButton = WebDriverWait(target, 10).until(locationWait)
        convertButton.click()
        time.sleep(2)

        locationDownload = EC.presence_of_element_located((By.ID, "asuccess"))
        downloadButton = WebDriverWait(target, 10).until(locationDownload)
        downloadButton.click()
        time.sleep(2)

        print(f"Successfully download {YouTube(url).title}")
    except :
        print(f"Cannot download {YouTube(url).title}")

    target.quit()
