n = int(input())
h = [int(x) for x in input().split()]
c = 0

while max(h) != 0:
    print(f"{h} {c}")
    flag = False
    for i in range(len(h)):
        if h[i] <= 1:
            if flag:
                c += 1
                break
        else:
            #水やり操作
            h[i] -= 1
            flag = True
            if i == len(h)-1:
                c += 1
print(c)
