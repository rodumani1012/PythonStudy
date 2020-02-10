# -*- coding: utf-8 -*-

# import math as test      # math module에 있는 모든 것을 임포트하여 test라는 변수로 사용하겠다.
from math import pi # math module 안에 있는 pi만 임포트

# 반지름이 3인 원의 넓이(π×r^2)를 구하는 함수를 만들자.
def circle(x):
    # return test.pi*x**2
    return pi*x**2

if __name__ == '__main__':
    area = circle(3)
    print(area)

