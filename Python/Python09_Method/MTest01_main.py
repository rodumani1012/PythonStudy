# -*- coding: utf-8 -*-
# python 인코딩 방법. 맨위에 -*- coding: encoding -*- 써주면 됨.

''' 
https://dojang.io/mod/page/view.php?id=2448
    '__name__' 은 모듈의 이름이 저장되는 변수이다. 스크립트 파일이 메인 프로그램으로 사용되는지 모듈로 사용되는지 구분하기 위한 용도이다.
import로 모듈을 가져왔을 때 '__name__'에는 모듈의 이름이 들어간다.
    하지만 파이썬 인터프리터로 스크립트 파일을 직접 실행했을 때는 '__name__'변수에 모듈의 이름이 아니라 '__main__'이 들어간다.
즉, '__main__'은 프로그램의 시작점(entry point) 이라는 뜻이다.
    '__name__' 변수를 통해 현재 스크립트 파일이 시작점인지 모듈인지 판단한다.
프로그램의 시작점일 경우에만 코드를 실행하고, 모듈로 가져올 경우 __main__을 실행하지 않고 method를 호출하는 용도로 사용한다.
'''

def func01():
    print('함수 1 입니다.')

def func02():
    return '함수 2 입니다.'

def func03():
    return {1:'a', 2:'b'}


if __name__ == '__main__':
    print('프로그램이 시작되면 가장 먼저 호출됨!!')
    # main (프로그램의 주 진입점)

    func01()
    print(func02())
    print('func03 키값 :', func03().keys())
    print('func03 키값 리스트 :', list(func03().keys()))