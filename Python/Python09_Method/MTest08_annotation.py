# -*- coding: utf-8 -*-

'''
 annotation 은 작성된 코드를 볼 때 명시적으로 해석을 돕기 위해 사용한다.
 메타데이터 정보로 사용되며 사용하는 방식은 아래와 같다.

 파라미터에는 '변수명 : 설명, 변수명 : 설명, ...' 식으로 쓰고
 함수의 return 값에 대해서는 '-> 설명' 으로 쓸 수 있다.
 '__annotations__' 는 딕셔너리로 저장된다.
'''

def func(ham: str, eggs: str = 'eggs') -> str:
    print('어노테이션 :', func.__annotations__)
    print('아규먼트 :', ham, eggs)
    return ham + ' and ' + eggs

func('스팸')

