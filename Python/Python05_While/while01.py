print('< 테스트 1 >')
i = 1
while i <= 10:
    print(i)
    i += 1 # i++이 아님!
print()

# 1부터 10까지 합
sum = 0
count = 1
while count <= 10:
    sum += count
    count += 1
    if count == 5:
        break
    else:
        print('sum =', sum)
        print('count =', count)

print('sum =', sum)
print('count =', count)