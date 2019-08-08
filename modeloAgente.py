"""
Instituto Tecnológico de Costa Rica
Escuela de compiutación
Curso: Inteligencia Artificial
Profesor: Esteban Arias Méndez
Estudiantes:
Camila Víquez Alpízar 2014152891
Fabricio Alvarado Esquivel 2016089643
"""

def readTxtFile():
    matrix = []
    with open("text.txt") as fp:
        line = fp.readline()
        while line:
            word = line.split()
            matrix.append(word)
            line = fp.readline()
    print(matrix)


readTxtFile()

def printMatrix(row, column):
    result = []
    for i in range(row):
        result.append([0]*column)

    for i in result:
        print (i)

    
