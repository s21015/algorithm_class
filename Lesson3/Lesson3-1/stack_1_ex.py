# 最初に2冊加える
# 次に1冊とりだす
# 最後に3冊加える

MAX = 5
stack = [0]*MAX
sp = 0
def push(d):
    global sp
    if sp < MAX:
        stack[sp] = d
        sp += 1
        print("本", d, "を追加しました")
    else:
        print("これ以上本を入れられません")

def pop():
    global sp
    if sp > 0:
        sp -= 1
        return stack[sp]
    else:
        print("取り出す本が存在しません")
        return None

def main():
    for i in range(2):
        push(i)
    for i in range(1):
        d = pop()
        print("取り出した本", d)
    for i in range(3):
        push(i)

main()