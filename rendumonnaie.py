systeme = []
for x in range(2,-1,-1): 
    systeme += 5 * (10**x),2 * (10**x),1 * (10**x) # ? * (10**x)
print(systeme)
etape = 0
max = 101
for i in range(1,max):
    print("-------ON TESTE ",i,"-------")
    etapeEnCours = 1
    payer = i 
    k = 0
    x = 0
    while payer != 0: 
        if systeme[x] > payer:
            x +=1
        elif systeme[x] <= payer:
            print("étape n° ", etapeEnCours)
            print("reste ",payer," monnaie : ",systeme[x])
            payer -= systeme[x]
            etape +=1
            etapeEnCours +=1
        

print(etape)
moyenneEtape = etape / max
print(moyenneEtape)