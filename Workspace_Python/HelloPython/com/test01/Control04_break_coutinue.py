
# 1 ~ 10
i = 1
while i <= 10:
    if i > 5:
        break
    print(i, end=' ')
    i += 1
print()

# 1 ~ 10 사이에서 짝수만 출력하자
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i, end=' ')
        
        
        
        
        