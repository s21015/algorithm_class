# data = [
#     "miku","nganomei","asidamana","sudamasaki","nagasawamasami(担任)",
#     "tanakakei","hosinogen","gakkii","satouken","abehirosi",
#     "murotuyosi","ikura","tyanmina","aiko","matumotohitoshi(校長)",
#     "devi(教頭)","ikutaerika","hiroyuki","yamadatayuki","imadamio",
#     "yamauti","kitamuratakumi","hikorohi-"
# ]
data = [
    "みく","ながのめい","あしだまな","すだまさき",
    "たなかけい","ほしのげん","がっきー","さとうけん","あべひろし",
    "むろつよし","いくら","ちゃんみな","あいこ",
    "いくたえりか","ひろゆき","やまだたかゆき","いまだみお",
    "やまうち","きたむらたくみ","ひころひー"
]
print(data, "元のデータ")

for i in range(len(data)):
    m = i
    for j in range(i+1, len(data)):
        if data[j] < data[m]:
            m = j
    data[i], data[m] = data[m], data[i]

print(data[0],data[1],data[2],data[3],data[4])
print(data[5],data[6],data[7],data[8],data[9])
print(data[10],data[11],data[12],data[13],data[14])
print(data[15],data[16],data[17],data[18],data[19])