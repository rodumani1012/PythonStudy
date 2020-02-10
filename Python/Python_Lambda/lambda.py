# Lambda(람다)

# var hap = function(a, b) {return a+b} 와 같은 식
hap = lambda a, b : a + b   # lambda 파라미터 : 실행할 내용
print('합 :', hap(1,2))

gob = lambda a, b : a * b
print('타입 :',type(gob))
print('곱 :', gob(3,4))

hap = lambda a,b,c : a+b+c
print('합 :', hap(1,2,3))

min = lambda x, y : x if x < y else y # x < y가 true면 x 출력, 아니면 y 출력
print('최소값1 :', min(4,5))
print('최소값2 :', min(5,4))

print()
# 함수 바로 실행
min = (lambda x,y : x if x < y else y)(10, 20)
print('바로 실행1 :', min)

max = (lambda x,y : x if x > y else y)(10, 20)
print('바로 실행2 :', max)


'''
    함수 안에 함수 형태
    function(x) {
        return function(y) {
            return x + y
        }
    }
'''
a = lambda x : (lambda newx : x + newx)
b = a(10) # 'b = lambda newx : 10 + newx' 인 상태.
c = b(20) # 'c = 10 + 20' 인 상태.
print('함수 안에 함수 :',c)
print('함수in함수 바로실행 :', a(10)(20))
print()

# 5의 배수 출력하기
d = lambda x : bool(x % 5) # 나머지가 0 이외 일때 true, 0이면 false 리턴
five = [i for i in range(1, 100) if not d(i)] # 나머지가 0일때만 five[]에 넣어주자.
                                # if not false : false가 아니면. 즉, true이면
print('5의 배수 출력하기1 :',five)
print()

# 파이썬에서 null은 None 이다.
e = lambda x : x if(x % 5 != 0) else None # 나머지가 0이 아니면 x값, false면(5의 배수) None값 리턴
res = [i for i in range(1, 100) if not e(i)] # None이 아니면
print('5의 배수 출력하기2 :',res)
print()

mylist = [(1, 'one', 6), (2, 'two', 7), (3, 'three', 8), (4,'four',9)]
print(mylist)
# 스펠링 순으로 정렬하기
# 방법 1
# print(sorted(mylist, key=lambda mylist : mylist[1]))
# 방법 2
# mylist.sort(key=lambda mylist : mylist[1])
print(mylist)

