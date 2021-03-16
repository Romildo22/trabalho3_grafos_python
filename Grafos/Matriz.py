import csv

def lerCSV(caminho):
    matriz = []
    with open(caminho) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_reader.__next__()
        for row in csv_reader:
            matriz = matriz + [row[1:]]
   
    matriz = [[int(j) for j in i] for i in matriz]
    return matriz

def calcularGraus(matriz):
    graus = []
    for v in range(len(matriz)):
        graus.append(0)
        for a in range(len(matriz[v])):
            if(matriz[v][a] == 1):
                graus[v] += 1
    return graus


def TeoremaOre(matriz, graus):
    graus = calcularGraus(matriz)
    if(len(matriz) < 3):
        return False

    for v1 in range(len(graus)-1):

        for v2 in range(v1+1, len(matriz[v1])):
            if(graus[v1] + graus[v2] < len(matriz)):
                return False
    return True


def bondyAndChvatal(matriz, graus):
    if(len(matriz)<3):
        return False
    matrizAux = matriz.copy()
    for v1 in range(len(graus)-1):
        for v2 in range(v1+1, len(matriz[v1])):
            if(matrizAux[v1][v2] == 0):
                if(graus[v1] + graus[v2] >= len(matriz)):
                    matrizAux[v1][v2] = 1
                    matrizAux[v2][v1] = 1
                else:
                    return False
    return True


def checarTeorema(teorema, resultado):
    print("Teorema: " + teorema + "\nResultado: " + str(resultado) + "\n------------------------------------------------------------------------------------------------------")
 

def TeoremaDirac(matriz, graus):

    if(len(matriz) < 3):
        return False

    for g in range(len(graus)):
        if(graus[g] < len(matriz)/2):
            return False
    return True


def checarGrafos(caminho):
    matriz = lerCSV(caminho)
    print("Matriz:" + str(matriz) + "\n")
    grausMatriz = calcularGraus(matriz)
    checarTeorema("Ore", TeoremaOre(matriz, grausMatriz))
    checarTeorema("Bondy And Chvatal", bondyAndChvatal(matriz, grausMatriz))
    checarTeorema("Dirac", TeoremaDirac(matriz, grausMatriz))
   

#------------------------  Checagem dos Grafos -------------------------------------
print("")
print("Grafo 01 :")
checarGrafos(r"C:\Users\Aptare Developer 02\Desktop\unifor\Grafos\Trabalho3\Grafos\Grafo01.csv")
print("Grafo 02 :")
checarGrafos(r"C:\Users\Aptare Developer 02\Desktop\unifor\Grafos\Trabalho3\Grafos\Grafo02.csv")
print("Grafo 03 :")
checarGrafos(r"C:\Users\Aptare Developer 02\Desktop\unifor\Grafos\Trabalho3\Grafos\Grafo03.csv")
print("Grafo 04 :")
checarGrafos(r"C:\Users\Aptare Developer 02\Desktop\unifor\Grafos\Trabalho3\Grafos\Grafo04.csv")