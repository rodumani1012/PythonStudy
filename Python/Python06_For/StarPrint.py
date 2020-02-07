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

