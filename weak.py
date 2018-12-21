#Aqui começa a Etapa 1

import math
import matplotlib.pyplot as plt

def evoluir_populacao_cenouras(Pce, Rce, Pcemax, Mce, Pco):
    """Calcula o crescimento de Cenouras
    Requires: Pce,Rce,Pcemax,Mce,Pco que sejam inteiros e onde Pcemax não pode ser zero
    Ensures: O número de cenouras depois de um mês
    """
    PceAfter = Pce + Rce * Pce * (1 - (Pce / Pcemax)) - (Mce * Pco)
    return round(PceAfter)

#Aqui começa a Etapa 2
def evoluir_populacao_coelhos(Pco, Pce, Mce, Pcomax, Mco, Plo):
    """Calcula o aumento da população de coelhos
    Requires: Pco,Pce,Mce,Pcomax,Mco,Plo que sejam inteiros onde Mce, Pco e Pcomax não podem ser igual a zero
    Ensures: O número de coelhos depois de um mês
    """
    Nco = Pce / (Mce * Pco)
    PcoAfter = Pco + Nco * (1 - (Pco / Pcomax)) - (Mco * Plo)
    return round(PcoAfter)

#Aqui começa a Etapa 3
def evoluir_populacao_lobos(Plo, Pco, Mco, Plomax, Mlo):
    """Calcula o aumento da população de lobos
    Requires: Pco,Mlo,Plomax,Mco,Plo que sejam inteiros onde Mco, Plo e Plomax não podem ser igual a zero
    Ensures: O número de lobos depois de um mês
    """
    Nlo = Pco / (Mco * Plo)
    PloAfter = Plo + Nlo * (1 - (Plo / Plomax)) - (Mlo * Plo)
    return round(PloAfter)


#Aqui começa a Etapa 4
def simular_populacoes(num_meses, param, t):
    """ Calcula o número Cenouras Coelhos e Lobos após Um número de meses inserido pelo utilizador
    Requires: num_meses que deve ser um inteiro positivo, e um dicionário que contem as variáveis necessárias p'ra as fun~es utilizadas p'ra calcular o número de seres vivos
    Ensures: A string com o número de meses e os respectivos números de cada espéciede ser vivo.E depois 3 listas em que cada lista contem a quantidade em cada mês de cada espécie de ser vivo, as listas são respectivamente de Cenouras, Coelhos e Lobos.
    """
    Rce = int(param["Rce"])
    PceMax = int(param["Pcemax"])
    Mce = int(param["Mce"])
    PcoMax = int(param["Pcomax"])
    Mco = int(param["Mco"])
    PloMax = int(param["Plomax"])
    Mlo = int(param["Mlo"])

    listaPce = []
    listaPco = []
    listaPlo = []

    if t == 0:
        print('Mês {} : {} cenouras, {} coelhos, {} lobos'.format(0, param["Pce0"], param["Pco0"], param["Plo0"]))

    for It in range(0, t + num_meses + 1):
        PopCe = param.get("Pce" + str(It), None)
        PopCo = param.get("Pco" + str(It), None)
        PopLo = param.get("Plo" + str(It), None)
        if PopCe == None or PopCo == None or PopLo == None:
            # Cria dados para mes = It
            AntPopCe = int(param["Pce" + str(It - 1)])
            AntPopCo = int(param["Pco" + str(It - 1)])
            AntPopLo = int(param["Plo" + str(It - 1)])
            PopCe = evoluir_populacao_cenouras(AntPopCe, Rce, PceMax, Mce, AntPopCo)
            PopCo = evoluir_populacao_coelhos(AntPopCo, AntPopCe, Mce, PcoMax, Mco, AntPopLo)
            PopLo = evoluir_populacao_lobos(AntPopLo, AntPopCo, Mco, PloMax, Mlo)
            param["Pce" + str(It)] = PopCe
            param["Pco" + str(It)] = PopCo
            param["Plo" + str(It)] = PopLo
            print('Mês {} : {} cenouras, {} coelhos, {} lobos'.format(It, PopCe, PopCo, PopLo))
        listaPce.append(int(PopCe))
        listaPco.append(int(PopCo))
        listaPlo.append(int(PopLo))

    return listaPce, listaPco, listaPlo

#Aqui começa a Etapa 5
def menu():
    """Através do input que pede ao utilizador simula o crescimento da população ou mostra um gráfico de uma espécie que o utilizador escolhe
    Requires: A função não requer quaisquer parâmetros
    Ensures: Calcula o número de cada espécie apôs um número específico de meses introduzido pelo utilizador ou constroí um gráfico com a evolução do ser vivo escolhido pelo utilizador do mês zero até ao mês introduzido pelo utilizador
    """
    print('(s)imular, (d)esenhar gráfico')
    Resposta = input()
    Resposta = Resposta.lower()
    if Resposta == 's':
        return simular()
    elif Resposta == 'd':
        return draw()
    elif Resposta == 'q':
        return Resposta
    else:
        print('Caracter inválido!')
        return menu()

#Aqui começa a Etapa 6
def obter_parametros(nome_ficheiro):
    """Constroí um dicionário com as variáveis que estão apresentadas no ficheiro (nome_ficheiro)
    Requires: O ficheiro (nome_ficheiro) que contem as variáveis necessárias à função simular_populacoes (num_meses,param)
    Ensures:Um dicionário com o nome das variáveis como chave e como valor a quantidade numérica da respectiva variável que tem como chave
    """
    ficheiro = open(nome_ficheiro, 'r')
    parametros = {}
    nome = []
    valor = []
    for linha in ficheiro:
        n,v = linha.split('=')
        nome.append(n.strip())
        valor.append(eval(v.strip()))
    for i in range(0, len(nome)):
        parametros.update({nome[i]:valor[i]})
    return parametros

#Aqui começa a Etapa 7
def simulador(nome_ficheiro):
    """Simula o crescimento das espécies de seres vivos do ecosistema
    Requires: Um ficheiro (nome_ficheiro) com as variáveis necessárias p'ra simular cada espécie
    Ensures: Uma string com o mês e o número de cada ser vivo p'ra cada espécie e em cada mês
    """
    parametros = obter_parametros(nome_ficheiro)
    mesAtual = 0
    Op = menu()
    while Op != 'q':
        if Op == 'c':
            grafico_populacao(mesAtual, parametros, 0)
        elif Op == 'r':
            grafico_populacao(mesAtual, parametros, 1)
        elif Op == 'w':
            grafico_populacao(mesAtual, parametros, 2)
        elif Op.isdigit():
            simular_populacoes(int(Op), parametros, mesAtual)
            mesAtual += int(Op)
        Op = menu()
    listasGuardar = simular_populacoes(mesAtual, parametros, 0)
    gravar_resultado_simulacao('resultados.csv', listasGuardar[0], listasGuardar[1], listasGuardar[2])
    print('Simulador Terminado')

def simular():
    print('Quantos meses pretende simular?')
    sims = input()
    sims = sims.lower()
    if sims == 'q' or (sims.isdigit() and int(sims) > 0):
        return sims
    elif sims == 'a':
        return menu()
    else:
        print('Caracter inválido!')
        return simular()

def draw():
    print('Qual a população que deseja representar?')
    print('C -> cenouras, R -> coelhos, W -> lobos')
    resposta = input()
    resposta = resposta.lower()
    if resposta == 'q' or resposta == 'c' or resposta == 'r' or resposta == 'w':
        return resposta
    elif resposta == 'a':
        return menu()
    else:
        print('Caracter inválido!')
        return draw()

def grafico_populacao(meses, parametros, pop_indice):
    lista = simular_populacoes(meses, parametros, 0)[pop_indice]
    descricao = 'Número de '
    color = ''
    if pop_indice == 0:
        descricao += "Cenouras"
        color = 'orange'
    elif pop_indice == 1:
        descricao += "Coelhos"
        color = 'c'
    elif pop_indice == 2:
        descricao += "Lobos"
        color = 'b'

    plt.plot(lista, linestyle='-', marker='o', color = color)
    plt.xlabel('Número de Meses')
    plt.ylabel(descricao)
    plt.title('Simulação de Ecossistema')
    plt.show()

#Aqui começa a Etapa 9
def gravar_resultado_simulacao(nome_ficheiro, lista_pop_cenouras, lista_pop_coelhos, lista_pop_lobos):
    """Grava os resultados do número de cada ser vivo em cada mês num formato(.csv)
    Requires:Um ficheiro (nome_ficheiro), uma lista com o número de cenouras em cada mês em que é efectuado a simulação(lista_pop_cenouras),uma lista com o número de coelhos em cada mês em que é efectuado a simulação(lista_pop_coelhos),uma lista com o número de lobos em cada mês em que é efectuado a simulação(lista_pop_lobos)
    Ensures: Um ficheiro .csv com cada mês e o respectivo número de cada ser vivo
    """
    ResFich = open(nome_ficheiro, 'w')
    for mes in range(0, len(lista_pop_lobos)):
        ResFich.write('{};{};{};{}\n'.format(mes, lista_pop_cenouras[mes], lista_pop_coelhos[mes], lista_pop_lobos[mes]))

simulador("configuracao.txt")
