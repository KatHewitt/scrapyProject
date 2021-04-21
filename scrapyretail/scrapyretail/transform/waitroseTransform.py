import pandas as pd

df = pd.read_csv("/Users/kathrynhewitt/PycharmProjects/ScrapyRetail/scrapyretail/waitrose.csv")
df.amount.str.replace('[\(\)]', '')
df['newAmount'] = df.amount.str.replace('[\(\)]', '')

amountList = df["newAmount"].tolist()

finalAmount = []
for a in amountList:
    if "p" in a:
        n1 = a.split("p")[0]
        n2 = float(n1)
        n3 = n2/100
        finalAmount.append(n3)
    elif "£" in a:
        n1 = a.split("£")[1]
        n2 = n1.split("/")[0]
        finalAmount.append(n2)
    else:
        finalAmount.append(a)
df['finalAmount'] = finalAmount

weightList = df["weight"].tolist()

finalWeight = []
for i in weightList:
    if "ml" in i:
        m1 = (float(i.split("ml")[0]))/1000
        finalWeight.append(m1)
    elif "litre" in i:
        m1 = i.split("litre")[0]
        finalWeight.append(m1)
    elif "each" in i:
        m1 = 1
        finalWeight.append(m1)
    elif "minimum" in i:
        m1 = i.split("minimum")[1]
        finalWeight.append(m1)
    elif i.endswith("kg") and i.startswith("Typical weight"):
        m1 = i.split("Typical weight")[1]
        m2 = m1.split("kg")[0]
        finalWeight.append(m2)
    elif i.endswith("kg"):
        m1 = i.split("kg")[0]
        finalWeight.append(m1)
    elif i.endswith("g") and i.startswith("drained"):
        m1 = i.split("x")[1]
        m2 = (float(m1.split("g")[0]))/1000
        finalWeight.append(m2)
    elif i.endswith("g") and i.startswith("Typical weight"):
        m1 = i.split("Typical weight")[1]
        m2 = (float(m1.split("g")[0]))/1000
        finalWeight.append(m2)
    elif i.endswith("g") and "4x400g" in i:
        m1 = 4
        finalWeight.append(m1)
    elif i.endswith("g"):
        m1 = (float(i.split("g")[0]))/1000
        finalWeight.append(m1)
    elif i.startswith("min") and i.endswith("s"):
        m1 = i.split("min")[1]
        m2 = m1.split("s")[0]
        finalWeight.append(m2)
    elif i.endswith("s"):
        m1 = i.split("s")[0]
        finalWeight.append(m1)
    elif i.startswith("min"):
        m1 = i.split("min")[1]
        finalWeight.append(m1)
    else:
        print('NO')
df['finalWeight'] = finalWeight

del df['amount']
del df['weight']
del df['newAmount']

df.to_csv("newWaitroseData.csv")