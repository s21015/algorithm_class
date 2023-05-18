MAX = 6
que = [0]*MAX
head = 0
tail = 0

def enqueue(d):
    global tail
    nt = (tail+1)%MAX

    if nt == head:
        print('これ以上データを入れられません')
    else:
        que[tail] = d
        tail = nt
        print(f'データ {d} を追加しました')

def dequeue():
    global head
    if head == tail:
        print('取り出すデータが存在しません')
        return None
    else:
        d = que[head]
        que[head] = 0
        head = (head + 1)%MAX
        print(f'取り出したデータ: {d}')
        return d

def get_queue(tail, head):
    i = head
    q = []
    while i%MAX != tail:
        q.append(que[i])
        i = (i+1)%MAX
    return q

n = 1
while True:
    s = input('命令を入力: ')
    if s == 'e':
        enqueue(n)
        n += 1
        queue = get_queue(tail, head)
        print(f'que:{que}, n:{n}, tail:{tail}, head:{head}, queue:{queue}')
    elif s == 'd':
        dequeue()
        queue = get_queue(tail, head)
        print(f'que:{que}, n:{n}, tail:{tail}, head:{head}, queue:{queue}')