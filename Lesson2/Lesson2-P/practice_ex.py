# （１）１０×１０　→　９×９
# （２）最後だけ「/」を表示
# （３）ループごとにP[]素数の個数

p = [True]*81
p[0] = False
p[1] = False
n = 2

def hyou():
    s = ""
    for i in range(81):
        if p[i] == True:
            s += "{:2d}, ".format(i)
        else:
            s += "/, "
        if i%10 == 9:
            s += "\n"
    print(s)

def furui():
    global n
    for i in range(n+n, 81, n):
        p[i] = False
    count = p.count(True)
    print(n, "の倍数を篩い落としました。")
    print(count, "個の素数があります。")
    while n<81:
        n += 1
        if p[n] == True:
            break

while n<10:
    furui()

hyou()