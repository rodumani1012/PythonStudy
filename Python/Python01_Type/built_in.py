# int() : 정수
print('True 값 :',int(True))
print('False 값 :',int(False))
print('타입 :', type(int('10')), int('10'))
print('타입 :', type(int(20.5)), int(20.5))
print()

# 2, 8, 16 진수
print('2진수 10101 :', int('10101', 2))
print('8진수 77 :', int('77', 8))
print('16진수 ff :', int('ff', 16))
print()

# float() : 실수
print(float('3'))
print(float(3))
print()

# complex() : 복소수
print(7j)
print(type(7j))
print(1 + 7.65j)
a = 1 + 7.65j
print()

# 실수 / 허수
print(a)
print('a의 실수 :',a.real)
print('a의 허수 :',a.imag)
print()

# str() : 문자열로 바꿔줌
print(str(3))
print(str(3)+'?')
print()

# repr() : '문자열' 객체
print(repr('Hello, World!'))
print(str('Hello, World!'))