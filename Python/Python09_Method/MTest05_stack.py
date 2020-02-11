# -*- coding: utf-8 -*-

# 계속해서 누적됨
def f(a, L = []):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# 누적되지 않게 함
def g(b, K = None) :
    if K is None:
        K = []
    K.append(b)
    return K

print(g(1))
print(g(2))
print(g(3))