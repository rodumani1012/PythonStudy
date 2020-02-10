# list []

# 생성자를 사용해서
a=list()
print(a)
a.append(1)
print(a)
a[0]='a'
print(a)

# []를 사용해서
b=[1,2,3,4,5]
print(b)
print("b[0]+b[4] =",b[0]+b[4]) # 1+5
b.reverse()
print("리버스 b =>", b)
c=[3,2,5,1,4]
print("정렬 전 :", c)
c.sort()
print("정렬 후 :", c)

# 배열에 배열을 넣을 수 있다.
d=[1,2,3,4,5,b]
print(d)

# 다른 타입도 넣을 수 있다.
e=['a','b','c',[1,2,3]]
print(e)

# list 더하기
print(d+e)
