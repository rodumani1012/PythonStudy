# -*- coding:UTF-8 -*-

# pip install selenium
'''
크롬 메뉴 -> 도움말 -> Chrome 정보 -> 버전 확인하기
http://chromedriver.chromium.org/downloads 
페이지 이동 후 버전에 맞는 
https://chromedriver.storage.googleapis.com/index.html?path=75.0.3770.140/
에서     chromedriver_win32.zip     다운로드하고 Work 폴더에 넣기!
'''

from bs4 import  BeautifulSoup
from selenium import webdriver

tag = input('search tag : ')
url = 'https://www.instagram.com/explore/tags/'+tag

# 크롬 자동으로 켜지는거 막기(chrome_options=options 추가하기)
options = webdriver.ChromeOptions()
options.add_argument('headless') # 창 안뜨게해주는거
options.add_argument('disable-gpu') # 창뜨는 가속도 없애기

driver = webdriver.Chrome('c:/Work/chromedriver.exe', options=options)
driver.implicitly_wait(3) # 요청 후 3초동안 기다리기
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

driver.quit()

instaImages = soup.find_all('div', {'class','KL4Bh'})

for instaImg in instaImages:
    img = instaImg.find('img')
    print(img.get('src'))






