# -*- coding: utf-8 -*-

# 필수 인자와 선택적 인자를 학습해보자.
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

'''주석을 풀어가며 결과를 확인해보세요.'''
# parrot(1000)
# parrot(voltage=1000)
# parrot(voltage=100000, action='VOOOOOM')
# parrot(action='VOOOOOM', voltage=100000) # 인자 순서에 구애받지 않는다.
# parrot('a million', 'bereft of life', 'jump') # 명시하지 않으면 인자 순서대로 들어간다.
# parrot('a thousand', state='pushing up the daisies')

'''에러가 나는 함수 호출'''
# parrot() # 필수 인자가 없어서.
# parrot(voltage=5.0, 'dead') # dead 값이 어떤 인자 값인지 명시해주지 않아서.
# parrot(110, voltage=220) # voltage 인자에 값을 여러개 넣어줘서.
# parrot(actor='John Cleese') # actor라는 인자는 없기 때문에.

