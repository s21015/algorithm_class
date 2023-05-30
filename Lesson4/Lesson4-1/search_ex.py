data = [
    ["佐藤", "000-0000-0000"],
    ["鈴木", "111-1111-1111"],
    ["高橋", "222-2222-2222"],
    ["田中", "333-3333-3333"],
    [None]
]
n = len(data)
s = input("検索する相手の名字は？")
i = 0
while data[i][0] != None and data[i][0] != s:
    i += 1
    if data[i][0] != None:
        print("その名は登録されていません")
        num = input("電話番号を追加してくださいください")
        data.append([s, num])
        break
print(data[-1][0]+"さんの番号は"+data[-1][1]+"です")