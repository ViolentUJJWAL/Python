from playsound import playsound

ui=int(input("n0...."))

# 1

i = 1
while i <= ui:
    g = 1
    while g <= ui-1:
        print("   ", end='')
        g = g + 1
    j = 1
    while j <= i:
        print("*  ", end='')
        j = j + 1
    i = i + 1
    print()
    playsound("C:\\Users\\UJJWAL\\Music\\Ding_Sound_Effect___No_copyright(128k).mp3")

# 2
print()
i1 = 1
while i1 <= ui:
    s = 1
    while s <= ui - i1:
        print("   ", end='')
        s = s + 1
    j1 = 1
    while j1 <= i1:
        print("*  ", end='')
        j1 = j1 + 1
    i1 = i1 + 1
    print()
    playsound("C:\\Users\\UJJWAL\\Music\\Ding_Sound_Effect___No_copyright(128k).mp3")

# 3
print()
tu=int(input("triangle last line star no..."))
i2 = 1
while i2 <= tu:
    s1 = 1
    while s1 <= tu - i2:
        print("   ", end='')
        s1 = s1 + 2
    j2 = 1
    while j2 <= i2:
        print("*  ", end='')
        j2 = j2 + 1
    i2 = i2 + 2
    print()
    playsound("C:\\Users\\UJJWAL\\Music\\Ding_Sound_Effect___No_copyright(128k).mp3")

# 4
print()
ri = ui
while ri > 0:
    rg = 1
    while rg <= ui-1:
        print("   ", end='')
        rg = rg + 1
    rj = 1
    while rj <= ri:
         print("*  ", end='')
         rj = rj + 1
    ri = ri - 1
    print()
    playsound("C:\\Users\\UJJWAL\\Music\\Ding_Sound_Effect___No_copyright(128k).mp3")

# 5
print()
ri1 = ui
while ri1 > 0:
    rs = 1
    while rs <= ui - ri1:
        print("   ", end='')
        rs = rs + 1
    rj1 = 1
    while rj1 <= ri1:
        print("*  ", end='')
        rj1 = rj1 + 1
    ri1 = ri1 - 1
    print()
    playsound("C:\\Users\\UJJWAL\\Music\\Ding_Sound_Effect___No_copyright(128k).mp3")

# 6
print()
ri2 = tu
while ri2 > 0:
    rs1 = 1
    while rs1 <= tu - ri2:
        print("   ", end='')
        rs1 = rs1 + 2
    rj2 = 1
    while rj2 <= ri2:
        print("*  ", end='')
        rj2 = rj2 + 1
    ri2 = ri2 - 2
    print()
    playsound("C:\\Users\\UJJWAL\\Music\\Ding_Sound_Effect___No_copyright(128k).mp3")
