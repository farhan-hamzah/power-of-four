n = int(input())
i = 0
j = 4
b = False
for i in range(n):
    j = j**i
    i +=1
    if j == n:
        b = True
        j = 4
    else:
        j = 4
print(b)

