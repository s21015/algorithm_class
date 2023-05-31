import random
n = 8
data = [0]*n
for i in range(n):
    data[i] = random.randint(1, 99)

def quick_sort(left, right):
    i = left
    j = right
    p = data[(left+right)//2]
    print("p=",p)
    while True:
        while data[i] < p:
            i += 1
        while data[j] > p:
            j -= 1
        if i >= j:
            break
        data[i], data[j] = data[j], data[i],
        print(data)
        i += 1
        j -= 1
        print("left=", left)
        print("right=", right)
    if left < i-1:
        quick_sort(left, i-1)
    if right > j+1:
        quick_sort(j+1, right)

print(data, "元のデータ")
quick_sort(0, n-1)
print(data, "ソート後のデータ")