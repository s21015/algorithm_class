data = [
    "miku","nganomei","asidamana","sudamasaki","nagasawamasami(担任)",
    "tanakakei","hosinogen","gakkii","satouken","abehirosi",
    "murotuyosi","ikura","tyanmina","aiko","matumotohitoshi(校長)",
    "devi(教頭)","ikutaerika","hiroyuki","yamadatayuki","imadamio",
    "yamauti","kitamuratakumi","hikorohi-"
]
print(data, "元のデータ")

for i in range(len(data)):
    m = i
    for j in range(i+1, len(data)):
        if data[j] < data[m]:
            m = j
    data[i], data[m] = data[m], data[i]

print(data, "ソート後のデータ")