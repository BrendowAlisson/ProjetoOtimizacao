import pandas as pd
import numpy as np
from random import randint
from copy import deepcopy

def ponto_proximo_da_origem(dicionarioOrigem):
    pontoProximo = min(dicionarioOrigem, key=dicOrigem.get)
    distanciaPontoProximo = dicionarioOrigem[pontoProximo]
    return (pontoProximo, distanciaPontoProximo)

def ponto_origem(dicionarioOrigem, pontoProximo):
    distanciaPontoProximo = dicionarioOrigem[pontoProximo]
    return (pontoProximo, distanciaPontoProximo)

def checar(distanciaArmazenada, pontoEscolhido):
    if distanciaArmazenada[pontoEscolhido] != 0:
        return True
    else:
        return False

def escolher_os_cincos_pontos_proximos(pontoQueEstamos, dados, dicionarioDados, inicio, fim):
    colunaDataPontoAtual = dados.iloc[dicionarioDados[pontoQueEstamos]].values
    indicesDaColuna = colunaDataPontoAtual.argsort()[inicio:fim]
    pontosComOsMenoresNumeros = np.delete(dados.columns[indicesDaColuna].values, [0])
    distanciaCincoPontos = np.delete(colunaDataPontoAtual[indicesDaColuna], [0])
    return (pontosComOsMenoresNumeros, distanciaCincoPontos)

def preenchido(pontoQueEstamos, dados, dicionarioDados, cincoPontos, vezes):
    global check
    global armazenaDistancia
    if vezes == 0:
        inicio = 0
        fim = 6
        (cincoPontos, distanciaCincoPontos) = escolher_os_cincos_pontos_proximos(pontoQueEstamos, dados, dicionarioDados, inicio, fim)
    elif vezes == 1:
        inicio = 5
        fim = 11
        (cincoPontos, distanciaCincoPontos) = escolher_os_cincos_pontos_proximos(pontoQueEstamos, dados, dicionarioDados, inicio, fim)
    elif vezes == 2:
        inicio = 10
        fim = 16
        (cincoPontos, distanciaCincoPontos) = escolher_os_cincos_pontos_proximos(pontoQueEstamos, dados, dicionarioDados, inicio, fim)
    elif vezes == 3:
        inicio = 15
        fim = 21
        (cincoPontos, distanciaCincoPontos) = escolher_os_cincos_pontos_proximos(pontoQueEstamos, dados, dicionarioDados, inicio, fim)
    elif vezes == 4:
        inicio = 20
        fim = 26
        (cincoPontos, distanciaCincoPontos) = escolher_os_cincos_pontos_proximos(pontoQueEstamos, dados, dicionarioDados, inicio, fim)
    for i in range(0, len(cincoPontos)):
        if armazenaDistancia[cincoPontos[i]] == 0:
            check = False
            return escolher_os_cincos_pontos_proximos(pontoQueEstamos, dados, dicionarioDados, inicio, fim)
    check = True
    return escolher_os_cincos_pontos_proximos(pontoQueEstamos, dados, dicionarioDados, inicio, fim)

def aleatorio(cincoPontosProximos, distanciaCincoPontos):
    global armazenaDistancia
    global dicData
    global data
    global proximoPonto
    global check
    vezes = 0
    while check == True:
        (cincoPontosProximos, distanciaCincoPontos) = preenchido(proximoPonto, data, dicData, cincoPontosProximos, vezes)
        vezes += 1
    if vezes == 4:
        numeroRand = randint(0, 3)
    else:
        numeroRand = randint(0, 4)
    pontoEscolhido = cincoPontosProximos[numeroRand]
    boolean = checar(armazenaDistancia, pontoEscolhido)
    check = True
    while boolean == True:
        if vezes == 4:
            numeroRand = randint(0, 3)
        else:
            numeroRand = randint(0, 4)
        pontoEscolhido = cincoPontosProximos[numeroRand]
        boolean = checar(armazenaDistancia, pontoEscolhido)
    distanciaDoPonto = distanciaCincoPontos[numeroRand]
    return (pontoEscolhido, distanciaDoPonto)

def colocar_distancia_para_chegar_na_usina(dicionarioDistancia, posicao):
    for i in range(0, len(armazenaDistancia)):
        if posicao["M" + str(i + 1)] == 20:
            dicionarioDistancia["Fim"] = dicFinal["M" + str(i + 1)]

def transformar_dic_em_list(dic):
    listaPos = []
    listaPonto = []
    dicAoContrario = dict((v, k) for k, v in dic.items())
    for i in range(1, len(dic) + 1):
        listaPos.append(dic[dicAoContrario[i]])
        listaPonto.append(dicAoContrario[i])
    return (listaPos, listaPonto)

def preencher_os_pontos_com_as_distancias(pontoQueEstamos, pontoQueQueremosIr, dados, dicionarioDados):
    global armazenaDistanciaPermutada
    global listaPermuta
    global dicFinal
    colunaDataPontoAtual = dados.iloc[dicionarioDados[pontoQueEstamos]].values
    distanciaParaOProxPonto = colunaDataPontoAtual[dicionarioDados[pontoQueQueremosIr]]
    armazenaDistanciaPermutada[pontoQueQueremosIr] = distanciaParaOProxPonto
    if pontoQueQueremosIr == listaPermuta[-1]:
        armazenaDistanciaPermutada["Fim"] = dicFinal[listaPermuta[-1]]
    return (distanciaParaOProxPonto)

def permutar(lista, a, b):
    listaPermutada = deepcopy(lista)
    listaPermutada[a], listaPermutada[b] = lista[b], lista[a]
    return listaPermutada

data = pd.read_csv("matriz.csv")
armazenaDistancia = dict.fromkeys(data.columns.tolist(), 0)
posicao = dict.fromkeys(data.columns.tolist(), 0)

dicData = {"M1": 0, "M2": 1, "M3": 2, "M4": 3, "M5": 4, "M6": 5, "M7": 6, "M8": 7, "M9": 8, "M10": 9,
           "M11": 10, "M12": 11, "M13": 12, "M14": 13, "M15": 14, "M16": 15, "M17": 16, "M18": 17,
           "M19": 18, "M20": 19}

dicOrigem = {"M1": 984.180, "M2": 1133.929, "M3": 634.414, "M4": 629.034, "M5": 867.820, "M6": 932.652, "M7": 1179.434,
             "M8": 1277.749, "M9": 1619.607, "M10": 1058.680,
             "M11": 271.348, "M12": 971.221, "M13": 344.874, "M14": 975.426, "M15": 2124.251, "M16": 2268.745,
             "M17": 1407.517, "M18": 4479.968,
             "M19": 1457.086, "M20": 4940.225}

dicFinal = {"M1": 709.053, "M2": 795.094, "M3": 583.383, "M4": 827.610, "M5": 954.354, "M6": 829.788, "M7": 834.539,
            "M8": 1493.951, "M9": 1701.872, "M10": 1117.537,
            "M11": 278.729, "M12": 766.355, "M13": 135.925, "M14": 844.6326, "M15": 1790.829, "M16": 1944.488,
            "M17": 1508.520, "M18": 4699.647,
            "M19": 1660.655, "M20": 5292.406}

check = True
(primeiroPonto, distanciaPrimeiroPonto) = ponto_proximo_da_origem(dicOrigem)
posicao[primeiroPonto] = 1
armazenaDistancia[primeiroPonto] = distanciaPrimeiroPonto
proximoPonto = primeiroPonto
(cincoPontos, distanciaDosCincoPontos) = escolher_os_cincos_pontos_proximos(proximoPonto, data, dicData, 0, 6)
(proximoPonto, distanciaProximoPonto) = aleatorio(cincoPontos, distanciaDosCincoPontos)
posicao[proximoPonto] = 2
armazenaDistancia[proximoPonto] = distanciaProximoPonto

for i in range(0, 18):
    (cincoPontos, distanciaDosCincoPontos) = escolher_os_cincos_pontos_proximos(proximoPonto, data, dicData, 0, 6)
    (proximoPonto, distanciaProximoPonto) = aleatorio(cincoPontos, distanciaDosCincoPontos)
    posicao[proximoPonto] = i + 3
    armazenaDistancia[proximoPonto] = distanciaProximoPonto

armazenaDistanciaPermutada = deepcopy(armazenaDistancia)
colocar_distancia_para_chegar_na_usina(armazenaDistancia, posicao)
distanciaTotal = sum(armazenaDistancia.values())
(listaPosicaoOriginal, listaPontoOriginal) = transformar_dic_em_list(posicao)
best = listaPontoOriginal
distanciaBest = distanciaTotal
contagem = 0

for j in range(1, len(best)-1):
    for k in range(2, len(best)):
        listaPermuta = permutar(best, j, k)
        for i in range(0, len(listaPermuta) - 1):
            preencher_os_pontos_com_as_distancias(listaPermuta[i], listaPermuta[i + 1], data, dicData)
        distanciaTotalPermutada = sum(armazenaDistanciaPermutada.values())
        if distanciaTotalPermutada < distanciaBest :
            best = listaPermuta
            distanciaBest = distanciaTotalPermutada
            k = 0
            contagem = 0
        else:
            contagem += 1
    if contagem == 100:
        break