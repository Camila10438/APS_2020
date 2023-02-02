# imports
import coordenadas as cd # importa um o .py com coordenadas dos pontos de reciclagem
import textos as tx
import math # importa uma biblioteca matemática
import os

# ini de variáveis
menu = 0
option = 0

# def de funções
def printlin(txt):
    print('\n' * os.get_terminal_size().lines)
    print(txt)

def AbsoluteDistance(a, b):
    res = abs(math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2))
    return res

def AbsoluteConvertedDistance(a, b):
    difa = abs(a[0]-b[0])
    difb = abs(a[1]-b[1])
    res = abs(math.sqrt(difa**2 + difb**2))
    res = res * 111.118
    return res

def PointsOfMaterial(mat): # calcula a distancia cartesiana entre as coordenadas atuais digitadas pelo usuário e todas as coordenadas dos pontos de coleta e retorna a menor distância
    res = []
    for i in range(len(cd.material)):
        if mat in cd.material[i] or mat == '':
            res.append([cd.nome[i],cd.endereco[i]])
    return res

def NearestPoint(lat, lon, mat): # calcula a distancia cartesiana entre as coordenadas atuais digitadas pelo usuário e todas as coordenadas dos pontos de coleta e retorna a menor distância
    res = ['.','.',0]
    res[2] = 1000000000
    for i in range(len(cd.material)):
        hdist = AbsoluteDistance([cd.latitude[i],cd.longitude[i]], [lat, lon])
        if (mat in cd.material[i] or mat == '') and hdist < res[2]:
            res = [cd.nome[i],cd.endereco[i],hdist]
    res.pop(2)
    return res

def AllPointsInRange(lat, lon, mat, alc): # calcula a distancia cartesiana entre as coordenadas atuais digitadas pelo usuário e todas as coordenadas dos pontos de coleta e retorna a menor distância
    res = []
    for i in range(len(cd.material)):
        hdist = AbsoluteConvertedDistance([cd.latitude[i],cd.longitude[i]], [lat, lon])
        if (mat in cd.material[i] or mat == '') and hdist <= alc:
            res.append([cd.nome[i],cd.endereco[i]])
    return res

# setup


# programa principal
while menu >= 0:
    if menu == 0:
        printlin(tx.menu[1])
        option = input(tx.menu[0])
        if option == '':
            menu = -1
        elif option == '1':
            menu = 1
        elif option == '2':
            menu = 2
        elif option == '3':
            menu = 3
        else:
            pass

    elif menu == 1:
        printlin('')
        printlin('')
        printlin('Aqui estão diversas informações a sua disposição:\n')
        info = -1
        for i in [tx.histMetal,tx.histPapel,tx.histVidro,tx.histOrganico,tx.histPlastico,tx.histEletronico]:
            info += 1
            print('• ' + str(['Metal','Papel','Vidro','Orgânico','Plastico','Eletronico'][info]) + '-' * 20)
            for k in i:
                print(k)
            print('\n')
        option = input(tx.novidades[2])
        menu = 0

    elif menu == 2:
        printlin(tx.novidades[0])
        print(tx.novidades[1])
        input(tx.novidades[2])
        menu = 0

    elif menu == 3:
        printlin(tx.pontosColeta[1])
        option = input(tx.pontosColeta[0])
        if option != '':
            print(tx.pontosColeta[3])
        if option == '':
            menu = -1
        elif option == '1':
            opt1 = input(tx.pontosColeta[2])
            for k in PointsOfMaterial(opt1):
                print('-----\nNome: {0}\nEndereço: {1}'.format(k[0], k[1]))
            input('\n')
        elif option == '2':
            opt1 = input(tx.pontosColeta[2])
            opt2 = float(input('digite sua latitude: '))
            opt3 = float(input('digite sua longitude: '))
            opt = NearestPoint(opt2, opt3, opt1)
            print('-----\nO ponto de coleta mais próximo de você é o {0} que fica no endereço {1}.'.format(opt[0],opt[1]))
            input('\n')
        elif option == '3':
            opt1 = input(tx.pontosColeta[2])
            opt2 = float(input('digite sua latitude: '))
            opt3 = float(input('digite sua longitude: '))
            opt4 = float(input('digite o raio de busca (em KM): '))
            for k in AllPointsInRange(opt2, opt3, opt1, opt4):
                print('-----\nNome: {0}\nEndereço: {1}'.format(k[0], k[1]))
            input('\n')
        elif option == 'menu':
            menu = 0
        else:
            print('Opção Inválida...')
            pass

# finalização
