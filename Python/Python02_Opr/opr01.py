# 산술연산
a = 13
b = 4

print('13 + 4 =',a+b)
print('13 - 4 =',a-b)
print('13 * 4 =',a*b)
print('13 / 4 =',a/b)
# 몫
print('13 // 4 =',a//b)
# 나머지
print('13 % 4 =',a%b)
print()

# 제곱
print('5^2 =', 5**2)

# 비교 연산
a, b = 4, 5  # 이렇게 값을 넣을 수도 있다.

print('4 == 5   =>', a==b)
print('4 != 5   =>', a!=b)
print('4 > 5   =>', a>b)
print('4 >= 5   =>',a>=b)
print('4 < 5   =>', a<b)
print('4 <= 5   =>', a<=b)
print('4 is 5   =>', a is b)
print('4 is not 5   =>', a is not b)
print()

print('참&거짓   =>', True and False)
print('참|참   =>', True or True)
print('!참   =>', not True)
print()

# 범위연산
list01 = list(range(100)) # 0 ~ 99 까지
print('range(100)   =>',list01)
print()

print('5번째 인덱스 :',list01[5])
print('[start : end-1]  =>',list01[5:11]) # [start : end-1] 까지 가져옴
print('[start : end-1 : step]   =>',list01[1:21:2]) # step 만큼 증가하면서 가져옴
print()

str01 = 'Hello, World!'
print(str01)
print(str01[1])
print(str01[7:12])
print(str01[7:12]*2)
print()

# 거꾸로 출력하기
print('거꾸로 출력하기')
print(str01[::-1])

# 멤버 연산
list02 = [1,2,3,4,5]
print('list02안에 0이 있는가?', 0 in list02)
print('list02안에 3이 없는가?', 3 in list02)
print('list02안에 6이 없는가?', 6 in list02)