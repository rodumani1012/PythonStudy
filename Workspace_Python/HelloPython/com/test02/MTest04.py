# -*- coding:UTF-8 -*- 

def mySum(x, y):
    return x + y

if __name__ == '__main__':
    a = mySum(1, 2)
    print(a)
    
    b = lambda x, y : x + y
    print(b(1, 2))