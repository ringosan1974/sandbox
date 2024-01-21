nq = [int(i) for i in input().split()]
n = nq[0]
q = nq[1]

s = input()

li = [0] * q
ri = [0] * q
for i in range(q):
    lr = [int(x) for x in input().split()]
    li[i] = lr[0]
    ri[i] = lr[1]

p = [0] * q

for i in range(q):
    for j in range(li[i]-1, ri[i]-1):
        if s[j] == s[j+1]:
            p[i] += 1

ans = " ".join([str(i) for i in p])
print(ans)