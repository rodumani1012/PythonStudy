# -*- coding: utf-8 -*-

def mySum(x, y):
    return x + y

if __name__ == '__main__':
    # a = mySum(3,4)
    # print(a)
    
    # b = lambda x, y : x + y
    # print(b(2,6))

    print(mySum(3, 4))
    print((lambda x, y : x + y)(2,6))