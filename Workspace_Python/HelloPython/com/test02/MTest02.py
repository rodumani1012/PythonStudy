# -*- coding:UTF-8 -*-

def func01(x, y):
    return x + y

def func02(x, y):
    return x + y, x - y

def func03(x, y):
    print('파라미터로 %d와 %d가 들어왔습니다.' % (x, y))

if __name__ == '__main__':
    a = func01(1,2)
    print(a)
    b, c = func02(3, 4)
    print(b, c)
    func03(b, c)