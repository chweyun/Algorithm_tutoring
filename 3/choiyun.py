n = int(input())
stairs = [0] * (n + 1)
d = [0] * (n + 1)

for i in range(1, n + 1):
    stairs[i] = int(input())
    
if n == 1:
    print(stairs[n])

elif n == 2:
    print(stairs[1] + stairs[2])

else:
    d[1] = stairs[1]
    d[2] = stairs[1] + stairs[2]
    d[3] = max(stairs[2] + stairs[3], stairs[1] + stairs[3])


    for i in range(4, n+1):
        d[i] = max(d[i-3] + stairs[i] + stairs[i-1], d[i-2] + stairs[i])

    print(d)