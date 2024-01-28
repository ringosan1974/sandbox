def perfect(taisyo):
    kei = 0
    for waru in range(1, taisyo+1):
        if (taisyo % waru == 0):
            kei = kei + waru
    if (kei == taisyo*2):
        return taisyo
    else:
        return 0
    
for kazu in range(1, 10000):
    if (perfect(kazu)>0):
        print(perfect(kazu))