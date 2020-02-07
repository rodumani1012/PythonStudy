# tuple : list와 비슷하다.
# list는 [], set은 {}, tuple은 () 로 출력된다.

# 생성자를 사용해서
a=tuple()
print('튜플생성자 :',a)

# ()로 생성
b=(1,2,3)
print('()로 생성 :',b)

# tuple은 값을 변경할 수 없다.
# a.append(1) # 에러 발생
# print(a)

# 리버스나 정렬이 안됨.
# b.reverse() # 에러 발생
# print(b)
# b.sort() # 에러 발생
# print(b)

# tuple 더하기
c=('a','b','c')
print('b =',b)
print('c =',c)
print('b + c =',b+c)

# 중첩
d=('e','f','g',(4,5,6))
print('d =',d)
