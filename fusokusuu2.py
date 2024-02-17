def deficient(taisyo):
    taisyo: int
    waru: int
    kei: int=0

    for waru in range(1, taisyo + 1):
        if taisyo % waru == 0:
            kei = kei + waru
            
    if kei < taisyo * 2:
        return taisyo
    else:
        return 0
    
kazu: int
hai = []
for kazu in range(1, 101):
    if deficient(kazu) > 0:
        hai.append(deficient(kazu))

print(hai)