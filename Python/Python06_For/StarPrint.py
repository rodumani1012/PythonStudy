'''
1
*
**
***
****
*****

2
*****
****
***
**
*

3
    *
   **
  ***
 ****
*****

4
*****
 ****
  ***
   **
    *

5
    *
   ***
  *****
 *******
*********
'''

print('1')
for i in range(1,6):
    print('*'*i)

print('2')
for i in range(5,0,-1):
    print('*'*i)
# 방법 2
for i in range(5):
    for j in range(5, i, -1):
        print('*', end='')
    print()

print('3')
for i in range(5,0,-1):
    print(' '*(i-1) + '*'*(6-i))
# 방법 2
for i in range(5):
    for j in range(5):
        if j < 4-i:
            print(' ', end='')
        else:
            print('*', end='')
    print()

print('4')
for i in range(0,5):
    print(' '*i + '*'*(5-i))
# for i in range(5,0,-1):
#     print(' '*(5-i) + '*'*i)

print('5')
for i in range(0, 5):
    print(' '*(4-i) + '*'*(i*2+1))

print('6')
for i in range(5):
    for j in range(i):
        print(' ', end='')
    for k in range(9-2*i):
        print('*', end='')
    print()
for i in range(4):
    for j in range(3-i):
        print(' ', end='')
    for k in range(3+2*i):
        print('*', end='')
    print()

# pip install numpy
# pip install matplotlib
