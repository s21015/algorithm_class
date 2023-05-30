colour = ["赤","橙","黃","緑","青","藍","紫"]

def nomal():
    for i in range(7):
        print(colour[i], end="→")

def reverse():
    for i in range(6, -1, -1):
        print(colour[i], end="→")

nomal()
print("\n")
reverse()