# set (집합) {}
# java에서 set은 순서 X, 중복 X

# list는 [], set은 {}, tuple은 () 로 출력된다.

# 생성자를 사용해서
a=set(['1','2','3'])
print('생성자 :',a)

# 생성자에 iterable한 객체를 넣으면 중복을 제외한다.
b=set('hellopython')
print('iterable :', b)

# {}로 생성하기
c={'a','b','c','d','hello'}
print('{}로 생성 : ',c)

d={'hello'}
print('d :',d)

# 추가
d.add('world')
print('d+ :',d)

# 합집합(union, |) / 교집합(intersection, &)
print('합집합 :',c.union(d))
print('교집합 :',c.intersection(d))
print('| :',c|d)
print('& :',c&d)
