# -*- coding: utf-8 -*-
# https://systemtrade.tistory.com/345

# pip install selenium
'''
크롬 메뉴 -> 도움말 -> Chrome 정보 -> 버전 확인하기
http://chromedriver.chromium.org/downloads
페이지 이동 후 버전에 맞는 드라이버로 다운 받기.
압축을 풀어서 작업할 폴더에 넣기(Selenium 객체를 생성할 때 이 경로를 지정해줘야 한다.
그래야만 python이 chromedriver를 통해 크롬 브라우저를 조작할 수 있다.)
'''

from bs4 import BeautifulSoup as bs
from selenium import webdriver as wd

tag = input('찾고자 하는 태그를 입력하세요 :')
url = 'https://www.instagram.com/explore/tags/'+tag

# 크롬 자동으로 켜지는거 막기(chrome_options=options 추가하기)
options = wd.ChromeOptions()
options.add_argument('headless') # 창 안뜨게 해주는 옵션.
options.add_argument('disalbe-gpu') # 창뜨는 가속도 없애기.

driver = wd.Chrome('C:/choi/Utils/chromedriver.exe', options=options)
driver.implicitly_wait(3) # 요청 후 3초동안 기다리기
driver.get(url)

soup = bs(driver.page_source, 'html.parser')

# driver.close() # close() : 현재 selenium webdriver가 활성화 되있는 화면만 종료함.
driver.quit() 
''' quit() : 모든 webdriver(쉽게말해 창)를 종료하고 세션을 안전하게 종료함.
quit()을 사용하지 않으면 webdriver 세션이 완벽하게 종료되지 않아 메모리 누수가 발생할 수 있음.
하나의 webdriver가 열려있다면 close()와 quit() 모두 같은 작업을 수행하지만
2개 이상의 webdriver가 열려있다면 close()와 quit()은 다르게 작동한다. '''

instaImages = soup.find_all('div', {'class','KL4Bh'})

for instaImg in instaImages:
    img = instaImg.find('img')
    print(img.get('src'))

