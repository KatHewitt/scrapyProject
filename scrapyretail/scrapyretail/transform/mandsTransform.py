import pandas as pd

df = pd.read_csv("/Users/kathrynhewitt/PycharmProjects/ScrapyRetail/scrapyretail/mands.csv")

amountList = df["amount"].tolist()
newAmounts = []
for a in amountList:
    if "p" in a:
        n1 = float(a.split("p")[0])/100
        newAmounts.append(n1)
    elif "£" in a:
        n1 = a.split("£")[1]
        newAmounts.append(n1)
    else:
        n1 = a
        newAmounts.append(n1)
df['newAmount'] = newAmounts

priceList = df["price"].tolist()
newPrices = []
for a in priceList:
    if "p" in a:
        n1 = float(a.split("p")[0])/100
        newPrices.append(n1)
    elif "£" in a:
        n1 = a.split("£")[1]
        newPrices.append(n1)
    else:
        n1 = a
        newPrices.append(n1)
df['newPrice'] = newPrices

weightList = df["weight"].tolist()
newWeights = []
for a in weightList:
    if "ml" in a:
        n1 = (float(a.split("ml")[0]))/1000
        newWeights.append(n1)
    elif a.endswith("kg"):
        n1 = a.split("kg")[0]
        newWeights.append(n1)
    elif a.endswith("g"):
        n1 = (float(a.split("g")[0]))/1000
        newWeights.append(n1)
    elif a.endswith("L"):
        n1 = a.split("L")[0]
        newWeights.append(n1)
    elif a.endswith("per pack"):
        n1 = a.split("per pack")[0]
        newWeights.append(n1)
    else:
        newWeights.append(a)
df['newWeight'] = newWeights

del df['amount']
del df['price']
del df['weight']

df.to_csv("newMandsData.csv")