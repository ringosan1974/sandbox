# num = int(input())
for i in range(1, 20):
    s = 0
    for waru in range(1, i):
        if (i % waru == 0):
            s += waru
    if (s == i):
        print(f"{i}: yes")
    else:
        print(f"{i}: no")