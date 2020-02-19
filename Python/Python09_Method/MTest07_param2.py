# -*- coding: utf-8 -*-

# 인자를 여러개 받아보자.
'''
    파라미터를 몇개 받을지 모르는 경우 사용하며
    * 은 튜플 형태('a','b','c',..)로 전달한다.
    ** 은 파라미터 명을 같이 보내며, 딕셔너리 형태(키=맵,키=맵,...)로 전달된다.
'''
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

print('\n\n')

# 응용하기
def test(a,b,c):
    print(a, b, c)

p = ['a', 'b', 'c']
test(p)
test(*p)

p2 = {'c' : '1', 'a' : '2', 'b' : '3'}
test(p2)
test(**p2)

