text = "I'm learning Python. It' interesting!"
pattern = "Python"
tn = len(text)
pn = len(pattern)
flg = False
p = 0

while p <= tn-pn:
    c = 0
    for i in range(pn):
        if text[p+i] != pattern[i]:
            brak
            c += 1
            