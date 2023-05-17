# 待ち時間に入る時に、待ち時間を表示（人数×15分）
# 待ちに入る→3人
# 待ちから出る→2人
# 待ちに入る→1人

MAX = 6
que = [0]*MAX
head = 0
tail = 0

def enqueue(d):
    global tail
    nt = (tail+1)%MAX
    if nt == head:
        print("これ以上データを入れられません")
    else:
        que[tail] = d
        tail = nt
        # print("データ", d, "を追加しました")

def dequeue():
    global head
    if head == tail:
        print("取り出すデータが存在しません")
        return None
    else:
        d = que[head]
        head = (head+1)%MAX
        return d

def main():
    n = 0
    for i in range(3):
        n = (i+1)*15
        enqueue(i)
        print("待ち時間：", n)
    for i in range(1,3):
        d = dequeue()
        n = n-15
        print(d,"が待ちから出ました")
    for i in range(1):
        enqueue(i)
        print("待ち時間：", n+15)

main()