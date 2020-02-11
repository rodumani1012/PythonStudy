# -*- coding: utf-8 -*-

# pip install BeautifulSoup4 (웹크롤링 라이브러리)
from bs4 import BeautifulSoup # 긁어온걸 파싱해주는 역할
import urllib.request # 긁어오는 역할
'''
    requests 모듈과 urllib 모듈은 굉장히 비슷한 역할을 합니다.
    하지만 많은 사람들이 python에서는 requests 모듈을 사용하고 있습니다.
    그렇다면 차이점에 대해서 알아보겠습니다.
    1. 데이터를 보낼때 requests는 딕셔너리 형태, urllib는 인코딩하여 바이너리 형태로 전송합니다.
    2. requests는 요청 메소드(get, post)를 명시하지만 urllib는 데이터의 여부에 따라 get과 post 요청을 구분합니다.
    3. 없는 페이지 요청시 requests는 에러를 띄우지 않지만 urllib는 에러를 띄웁니다.
'''

# 응답된 데이터가 resp에 담겨있음.
resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.nhn')
# print(resp)

# resp 파싱하기.
soup = BeautifulSoup(resp, 'html.parser')
print(soup)

# dl 태그에서 클래스명이 lst_dsc인 것 찾아오기
movieList = soup.findAll('dl', {'class','lst_dsc'})