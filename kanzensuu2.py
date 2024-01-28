def perfect(n):
    s = 0
    for waru in range(1, n):
        if (n % waru == 0):
            s += waru
    if (s == n):
        return n
    else:
        return 0

for i in range(下限, 上限＋１):
    re = perfect(i)
    if (re > 0):
        print(re)