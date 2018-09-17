import random


def adFunc(theTuple):
    #print(theTuple)
    listAD = list(theTuple)
    d1 = random.randint(0,6)
    d2 = random.randint(0,5)
    del listAD[d1]
    del listAD[d2]
    #print(theTuple)
    #print(listAD)
    return listAD

adtup = ('blue','cheese','Carrigtwohill','Dolly Parton','ABBA','Basketball','Cork')
lll = adFunc(adtup)

print(adtup)
print(lll)
