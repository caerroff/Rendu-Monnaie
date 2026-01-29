systeme = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
solution = []
etape = 0
max = 101
i = 59.73
print("-------ON TESTE ",i,"-------")
etapeEnCours = 1
reste = i 
k = 0
x = 0
while reste != 0: 
    if systeme[x] > reste:
        x +=1
    elif systeme[x] <= reste:
        print("étape n° ", etapeEnCours)
        print("reste ",reste," monnaie : ",systeme[x])
        reste -= systeme[x]
        reste = round(reste,2)
        solution.append(systeme[x])
        print("il reste à reste : ",reste)
        etape +=1
        etapeEnCours +=1
        
print("-------FINI-------")
print("Etapes : ",etape)
print("Solution : ",solution)