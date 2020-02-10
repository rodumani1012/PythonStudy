# dictionary
# 순서 : X, 중복: key(X), value(O)
# java의 map과 비슷함

# 생성자를 사용해서
dict01 = dict()
print('생성자 :',dict01)
dict01[1] = 1 # key, value
dict01[2] = 2 # key, value
print('key, value :',dict01)

dict02 = {}
dict02['one'] = 'This is One!'
dict02['two'] = 'This is One!'
dict02[3] = 3
dict02[3] = 'This is Three!'
print('중복 테스트 :',dict02)

# key를 가지고 value를 출력해보자
print('dict01 :', dict01)
print('key 1 :',dict01.get(1))
print('dict02 :', dict02)
print('key one :',dict02.get('one'))

# key 따로 value 따로 가져오기.
print('dict01 keys :',dict01.keys())
print('dict02 values :',dict02.values())
print('리스트안에 dict값 출력 :',list(dict02.values())[2])