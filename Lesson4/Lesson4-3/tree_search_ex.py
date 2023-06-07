LEFT = 0
RIGHT = 1
DATA = 2
node = [
    [1,2,"38.5℃以上の発熱がある？"],
    [3,4,"元気がある？"],
    [5,6,"胸が引い引い？"],
    [None,None,"様子を見る"],
    [None,None,"氷枕で病院"],
    [None,None,"解熱剤で病院"],
    [None,None,"速攻で病院"]
]

def traverse(p):
    print(node[p][DATA])
    s = input()
    if s == 'no':
        print(node[1][DATA])
        s2 = input()
        if s2 == 'yes':
            print(node[3][DATA])
        elif s2 == 'no':
            print(node[4][DATA])
    elif s == 'yes':
        print(node[2][DATA])
        s3 = input()
        if s3 == 'no':
            print(node[5][DATA])
        elif s3 == 'yes':
            print(node[6][DATA])

print("元気ですかー！？")
traverse(0)