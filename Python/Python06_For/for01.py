'''
for 변수 in 자료형(순서):
    명령문1
else:
    명령문2

※ 명령문 2는 반복이 완료된 후 수행된다.

range(start, stop, step)
start부터 stop전까지 step만큼 건너뛰며 sequence 생성
'''


subject = ['java', 'db', 'ui', 'web', 'spring', 'python']

# for i in subject:
#     print('과목명 :', i)
for i in range(len(subject)):
    print('과목명' + str(i+1),':', subject[i])
print()

for i in range(1, 100):
    print(i, end=' ')
print()

# sep : value와 value 사이의 구분자
# end : 동작 후 할 행동
for i in range(1, 11):
    print(i,'',sep=', ', end='')
print()

print('\n구구단')
for i in range(2, 10):
    print('< ' + str(i) + '단 >')
    for j in range(1, 10):
        # print(i,' * ', j, ' = ', i*j)
        # print(str(i)+' * '+str(j)+' = '+str(i*j))
        # print(str(i), '*', str(j), '=', str(i*j))
        print(i, j, sep=' X ', end=' = ' + str(i*j) + '\n')

print()

# 거꾸로 출력하기
for i in range(10, 0, -1):
    print(i, end=' ')