# -*- coding: utf-8 -*-
# https://systemtrade.tistory.com/345

# pip install requests
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

tag = input('찾고자 하는 태그를 입력하세요 :')
print('찾을 태그 :', tag)
url = 'https://www.instagram.com/explore/tags/' + tag
resp = requests.get(url)
print('요청에 대한 http 상태코드 :', resp)
soup = BeautifulSoup(resp.text, 'html.parser')
# print('파싱한 html 소스 :', soup) # 출력양이 많아서 주석처리함.
print(soup.find('div',{'class','KL4Bh'})) # class가 KL4Bh인 div태그를 찾음.

'''
instagram은 페이지가 response된 후에 다시 내부적으로 request하여 다른 데이터를 가져오기 때문에
우리가 원하는 데이터를 가져오지 못했다. 따라서 None이 출력되었다.
다음 장에서 출력하는 방법을 알아보자.
'''
