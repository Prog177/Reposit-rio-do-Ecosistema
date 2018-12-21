#Aqui começa a Etapa 1

import math
import matplotlib.pyplot as plt

def evoluir_populacao_cenouras (Pce,Rce,Pcemax,Mce,Pco):
    """Calcula o crescimento de Cenouras
    Requires: Pce,Rce,Pcemax,Mce,Pco que sejam inteiros e onde Pcemax não pode ser zero
    Ensures: O número de cenouras depois de um mês
    """
    Pce=int(Pce)
    Rce=int(Rce)
    Pcemax=int(Pcemax)
    Mce=int(Mce)
    Pco=int(Pco)
    PceAfter=Pce+((Rce*Pce)*(1-(Pce/Pcemax)))-(Mce*Pco)
    return round(PceAfter)

#Aqui começa a Etapa 2
def evoluir_populacao_coelhos (Pco,Pce,Mce,Pcomax,Mco,Plo):
    """Calcula o aumento da população de coelhos
    Requires: Pco,Pce,Mce,Pcomax,Mco,Plo que sejam inteiros onde Mce, Pco e Pcomax não podem ser igual a zero
    Ensures: O número de coelhos depois de um mês
    """
    Pco=int(Pco)
    Pce=int(Pce)
    Mce=int(Mce)
    Pcomax=int(Pcomax)
    Mco=int(Mco)
    Plo=int(Plo)
    Nco=(Pce/(Mce*Pco))
    PcoAfter=Pco+Nco*(1-(Pco/Pcomax))-(Mco*Plo)
    return round(PcoAfter)

#Aqui começa a Etapa 3
def evoluir_populacao_lobos (Plo,Pco,Mco,Plomax,Mlo):
    """Calcula o aumento da população de lobos
    Requires: Pco,Mlo,Plomax,Mco,Plo que sejam inteiros onde Mco, Plo e Plomax não podem ser igual a zero
    Ensures: O número de lobos depois de um mês
    """
    Mlo=float(Mlo)
    Plo=int(Plo)
    Pco=int(Pco)
    Mco=int(Mco)
    Plomax=int(Plomax)
    Nlo=(Pco/(Mco*Plo))
    PloAfter=Plo+Nlo*(1-(Plo/Plomax))-(Mlo*Plo)
    return round(PloAfter)

#Aqui começa a Etapa 4
def simular_populacoes (num_meses, param, t):
    """ Calcula o número Cenouras Coelhos e Lobos após Um número de meses inserido pelo utilizador
    Requires: num_meses que deve ser um inteiro positivo, e um dicionário que contem as variáveis necessárias p'ra as fun~es utilizadas p'ra calcular o número de seres vivos
    Ensures: A string com o número de meses e os respectivos números de cada espéciede ser vivo.E depois 3 listas em que cada lista contem a quantidade em cada mês de cada espécie de ser vivo, as listas são respectivamente de Cenouras, Coelhos e Lobos.
    """
    a=[0]
    Month=0
    FinalReturn=""
    AlternateListCen=[]
    AlternateListCo=[]
    AlternateListLo=[]
    if t != 0 and num_meses == 0:
        for Iteration in range(0, int(num_meses) + int(t)+1):        
            if Iteration==0:
                Month+=1
                AlternateListCen.append(50000)
                AlternateListCo.append(50)
                AlternateListLo.append(5)
                param["Pce0"+str(Iteration)] = param["Pce0"]
                param["Rce"+str(Iteration)] = param["Rce"]
                param["Pcemax"+str(Iteration)] = param["Pcemax"]
                param["Mce"+str(Iteration)] = param["Mce"]
                param["Pco0"+str(Iteration)] = param["Pco0"]
                param["Pcomax"+str(Iteration)] = param["Pcomax"]
                param["Mco"+str(Iteration)] = param["Mco"]
                param["Plo0"+str(Iteration)] = param["Plo0"]
                param["Plomax"+str(Iteration)] = param["Plomax"]
                param["Mlo"+str(Iteration)] = param["Mlo"]
            else:
                Iteration-=1
                CenourasIntermidiate=evoluir_populacao_cenouras (param["Pce0"+str(Iteration)],param["Rce"],param["Pcemax"],param["Mce"],param["Pco0"+str(Iteration)])
                CoelhosIntermidiate=evoluir_populacao_coelhos (param["Pco0"+str(Iteration)],param["Pce0"+str(Iteration)],param["Mce"],param["Pcomax"],param["Mco"],param["Plo0"+str(Iteration)])
                LobosIntermidiate=evoluir_populacao_lobos (param["Plo0"+str(Iteration)],param["Pco0"+str(Iteration)],param["Mco"],param["Plomax"],param["Mlo"])
                Iteration+=1
                param["Pce0"+str(Iteration)] = int(CenourasIntermidiate)
                param["Rce"+str(Iteration)] = param["Rce"]
                param["Pcemax"+str(Iteration)] = param["Pcemax"]
                param["Mce"+str(Iteration)] = param["Mce"]
                param["Pco0"+str(Iteration)] = int(CoelhosIntermidiate)
                param["Pcomax"+str(Iteration)] = param["Pcomax"]
                param["Mco"+str(Iteration)] = param["Mco"]
                param["Plo0"+str(Iteration)] = int(LobosIntermidiate)
                param["Plomax"+str(Iteration)] = param["Plomax"]
                param["Mlo"+str(Iteration)] = param["Mlo"]
                AlternateListCen.append(CenourasIntermidiate)
                AlternateListCo.append(CoelhosIntermidiate)
                AlternateListLo.append(LobosIntermidiate)
                Month+=1
        for Iteration2 in range(t, int(num_meses) + int(t)+1):
            if Iteration2==0:
                FinalReturn += ('Mês '+str(Iteration2)+' : '+str(param["Pce0"])+' cenouras,'+str(param["Pco0"])+' coelhos,'+str(param["Pco0"])+' lobos')+('\n')
            else:
                FinalReturn += ('Mês '+str(Iteration2)+' : '+str(param["Pce0"+str(Iteration2)])+' cenouras,'+str(param["Pco0"+str(Iteration2)])+' coelhos,'+str(param["Plo0"+str(Iteration2)])+' lobos')+("\n")
    if t == 0 and num_meses == 0:
        AlternateListCen.append(50000)
        AlternateListCo.append(50)
        AlternateListLo.append(5)
        FinalReturn = ('Mês '+str(0)+' : '+str(param["Pce0"])+' cenouras,'+str(param["Pco0"])+' coelhos,'+str(param["Pco0"])+' lobos')
        a.append(1)
    if num_meses!=0 and t==0 and a[-1] == 0:
        for Iteration in range(0, int(num_meses) + int(t)+1):        
            if Iteration==0:
                Month+=1
                AlternateListCen.append(50000)
                AlternateListCo.append(50)
                AlternateListLo.append(5)
                param["Pce0"+str(Iteration)] = param["Pce0"]
                param["Rce"+str(Iteration)] = param["Rce"]
                param["Pcemax"+str(Iteration)] = param["Pcemax"]
                param["Mce"+str(Iteration)] = param["Mce"]
                param["Pco0"+str(Iteration)] = param["Pco0"]
                param["Pcomax"+str(Iteration)] = param["Pcomax"]
                param["Mco"+str(Iteration)] = param["Mco"]
                param["Plo0"+str(Iteration)] = param["Plo0"]
                param["Plomax"+str(Iteration)] = param["Plomax"]
                param["Mlo"+str(Iteration)] = param["Mlo"]
            else:
                Iteration-=1
                CenourasIntermidiate=evoluir_populacao_cenouras (param["Pce0"+str(Iteration)],param["Rce"],param["Pcemax"],param["Mce"],param["Pco0"+str(Iteration)])
                CoelhosIntermidiate=evoluir_populacao_coelhos (param["Pco0"+str(Iteration)],param["Pce0"+str(Iteration)],param["Mce"],param["Pcomax"],param["Mco"],param["Plo0"+str(Iteration)])
                LobosIntermidiate=evoluir_populacao_lobos (param["Plo0"+str(Iteration)],param["Pco0"+str(Iteration)],param["Mco"],param["Plomax"],param["Mlo"])
                Iteration+=1
                param["Pce0"+str(Iteration)] = int(CenourasIntermidiate)
                param["Rce"+str(Iteration)] = param["Rce"]
                param["Pcemax"+str(Iteration)] = param["Pcemax"]
                param["Mce"+str(Iteration)] = param["Mce"]
                param["Pco0"+str(Iteration)] = int(CoelhosIntermidiate)
                param["Pcomax"+str(Iteration)] = param["Pcomax"]
                param["Mco"+str(Iteration)] = param["Mco"]
                param["Plo0"+str(Iteration)] = int(LobosIntermidiate)
                param["Plomax"+str(Iteration)] = param["Plomax"]
                param["Mlo"+str(Iteration)] = param["Mlo"]
                AlternateListCen.append(CenourasIntermidiate)
                AlternateListCo.append(CoelhosIntermidiate)
                AlternateListLo.append(LobosIntermidiate)
                Month+=1
        for Iteration2 in range(t, int(num_meses) + int(t)+1):
            if Iteration2==0:
                FinalReturn += ('Mês '+str(Iteration2)+' : '+str(param["Pce0"])+' cenouras,'+str(param["Pco0"])+' coelhos,'+str(param["Pco0"])+' lobos')+('\n')
            else:
                FinalReturn += ('Mês '+str(Iteration2)+' : '+str(param["Pce0"+str(Iteration2)])+' cenouras,'+str(param["Pco0"+str(Iteration2)])+' coelhos,'+str(param["Plo0"+str(Iteration2)])+' lobos')+("\n")
    if num_meses!=0 and t==0 and a[-1] != 0:
        for Iteration in range(0, int(num_meses) + int(t)+1):        
            if Iteration==0:
                Month+=1
                AlternateListCen.append(50000)
                AlternateListCo.append(50)
                AlternateListLo.append(5)
                param["Pce0"+str(Iteration)] = param["Pce0"]
                param["Rce"+str(Iteration)] = param["Rce"]
                param["Pcemax"+str(Iteration)] = param["Pcemax"]
                param["Mce"+str(Iteration)] = param["Mce"]
                param["Pco0"+str(Iteration)] = param["Pco0"]
                param["Pcomax"+str(Iteration)] = param["Pcomax"]
                param["Mco"+str(Iteration)] = param["Mco"]
                param["Plo0"+str(Iteration)] = param["Plo0"]
                param["Plomax"+str(Iteration)] = param["Plomax"]
                param["Mlo"+str(Iteration)] = param["Mlo"]
            else:
                Iteration-=1
                CenourasIntermidiate=evoluir_populacao_cenouras (param["Pce0"+str(Iteration)],param["Rce"],param["Pcemax"],param["Mce"],param["Pco0"+str(Iteration)])
                CoelhosIntermidiate=evoluir_populacao_coelhos (param["Pco0"+str(Iteration)],param["Pce0"+str(Iteration)],param["Mce"],param["Pcomax"],param["Mco"],param["Plo0"+str(Iteration)])
                LobosIntermidiate=evoluir_populacao_lobos (param["Plo0"+str(Iteration)],param["Pco0"+str(Iteration)],param["Mco"],param["Plomax"],param["Mlo"])
                Iteration+=1
                param["Pce0"+str(Iteration)] = int(CenourasIntermidiate)
                param["Rce"+str(Iteration)] = param["Rce"]
                param["Pcemax"+str(Iteration)] = param["Pcemax"]
                param["Mce"+str(Iteration)] = param["Mce"]
                param["Pco0"+str(Iteration)] = int(CoelhosIntermidiate)
                param["Pcomax"+str(Iteration)] = param["Pcomax"]
                param["Mco"+str(Iteration)] = param["Mco"]
                param["Plo0"+str(Iteration)] = int(LobosIntermidiate)
                param["Plomax"+str(Iteration)] = param["Plomax"]
                param["Mlo"+str(Iteration)] = param["Mlo"]
                AlternateListCen.append(CenourasIntermidiate)
                AlternateListCo.append(CoelhosIntermidiate)
                AlternateListLo.append(LobosIntermidiate)
                Month+=1
        for Iteration2 in range(t+1, int(num_meses) + int(t)+1):
            if Iteration2==0:
                FinalReturn += ('Mês '+str(Iteration2)+' : '+str(param["Pce0"])+' cenouras,'+str(param["Pco0"])+' coelhos,'+str(param["Pco0"])+' lobos')+('\n')
            else:
                FinalReturn += ('Mês '+str(Iteration2)+' : '+str(param["Pce0"+str(Iteration2)])+' cenouras,'+str(param["Pco0"+str(Iteration2)])+' coelhos,'+str(param["Plo0"+str(Iteration2)])+' lobos')+("\n")
    if num_meses!=0 and t!=0:
        for Iteration in range(0, int(num_meses) + int(t)+1):        
            if Iteration==0:
                Month+=1
                AlternateListCen.append(50000)
                AlternateListCo.append(50)
                AlternateListLo.append(5)
                param["Pce0"+str(Iteration)] = param["Pce0"]
                param["Rce"+str(Iteration)] = param["Rce"]
                param["Pcemax"+str(Iteration)] = param["Pcemax"]
                param["Mce"+str(Iteration)] = param["Mce"]
                param["Pco0"+str(Iteration)] = param["Pco0"]
                param["Pcomax"+str(Iteration)] = param["Pcomax"]
                param["Mco"+str(Iteration)] = param["Mco"]
                param["Plo0"+str(Iteration)] = param["Plo0"]
                param["Plomax"+str(Iteration)] = param["Plomax"]
                param["Mlo"+str(Iteration)] = param["Mlo"]
            else:
                Iteration-=1
                CenourasIntermidiate=evoluir_populacao_cenouras (param["Pce0"+str(Iteration)],param["Rce"],param["Pcemax"],param["Mce"],param["Pco0"+str(Iteration)])
                CoelhosIntermidiate=evoluir_populacao_coelhos (param["Pco0"+str(Iteration)],param["Pce0"+str(Iteration)],param["Mce"],param["Pcomax"],param["Mco"],param["Plo0"+str(Iteration)])
                LobosIntermidiate=evoluir_populacao_lobos (param["Plo0"+str(Iteration)],param["Pco0"+str(Iteration)],param["Mco"],param["Plomax"],param["Mlo"])
                Iteration+=1
                param["Pce0"+str(Iteration)] = int(CenourasIntermidiate)
                param["Rce"+str(Iteration)] = param["Rce"]
                param["Pcemax"+str(Iteration)] = param["Pcemax"]
                param["Mce"+str(Iteration)] = param["Mce"]
                param["Pco0"+str(Iteration)] = int(CoelhosIntermidiate)
                param["Pcomax"+str(Iteration)] = param["Pcomax"]
                param["Mco"+str(Iteration)] = param["Mco"]
                param["Plo0"+str(Iteration)] = int(LobosIntermidiate)
                param["Plomax"+str(Iteration)] = param["Plomax"]
                param["Mlo"+str(Iteration)] = param["Mlo"]
                AlternateListCen.append(CenourasIntermidiate)
                AlternateListCo.append(CoelhosIntermidiate)
                AlternateListLo.append(LobosIntermidiate)
                Month+=1
        for Iteration2 in range(t+1, int(num_meses) + int(t)+1):
            if Iteration2==0:
                FinalReturn += ('Mês '+str(Iteration2)+' : '+str(param["Pce0"])+' cenouras,'+str(param["Pco0"])+' coelhos,'+str(param["Pco0"])+' lobos')+('\n')
            else:
                FinalReturn += ('Mês '+str(Iteration2)+' : '+str(param["Pce0"+str(Iteration2)])+' cenouras,'+str(param["Pco0"+str(Iteration2)])+' coelhos,'+str(param["Plo0"+str(Iteration2)])+' lobos')+("\n")              
    t = int(num_meses) + int(t)
    return FinalReturn, AlternateListCen, AlternateListCo, AlternateListLo, param, t

#Aqui começa a Etapa 5 e Etapa 8
def menu():
    """Através do input que pede ao utilizador simula o crescimento da população ou mostra um gráfico de uma espécie que o utilizador escolhe
    Requires: A função não requer quaisquer parâmetros
    Ensures: Calcula o número de cada espécie apôs um número específico de meses introduzido pelo utilizador ou constroí um gráfico com a evolução do ser vivo escolhido pelo utilizador do mês zero até ao mês introduzido pelo utilizador
    """
    b = [0]
    while b[-1] == 0:
        Resposta = input('O que pretende fazer? (s)imular, (d)esenhar gráfico')
        Resposta = Resposta.lower()
        Months = [0]
        b.append(1)
    while True:
        if Resposta == 's':
            Resposta1 = input('Quantos meses pretende simular?')
            Resposta1 = Resposta1.lower()
            if Resposta1.isdigit():
                Months.append('s')
                Months.append(Resposta1)
                return Months
            else:
                if Resposta1 == 'a':
                    return menu()
                if Resposta1 != "q" and Resposta1 != 'a':
                    print("Caracter inválido!")
                if  Resposta1 == 'q':
                    Months.append('s')
                    Months.append('q')
                    return Months
        elif Resposta == 'a':
            return menu()
        elif Resposta != 's' and Resposta != 'a' and Resposta != 'q' and Resposta != 'd':
            print("Caracter inválido!")
            return menu()
        elif  Resposta == 'q':
            Months.append('q')
            return Months
        elif Resposta == 'd':
            print('Qual a população que deseja representar?')
            Pop = input('C -> cenouras, R -> coelhos, W -> lobos')
            Pop = Pop.lower()
            if Pop == 'q':
                Months.append('d')
                Months.append('q')
                return Months
            if Pop == 'c':
                Months.append('d')
                Months.append('c')
                return Months
            if Pop == 'r':
                Months.append('d')
                Months.append('r')
                return Months
            if Pop == 'w':
                Months.append('d')
                Months.append('w')
                return Months
            if Pop == 'a':
                return menu()
            if Pop != 'q' and Pop != 'c' and Pop != 'r' and Pop != 'w' and Pop != 'a':
                print("Caracter inválido!")
                
    return

#Aqui começa a Etapa 6
def obter_parametros(nome_ficheiro):
    """Constroí um dicionário com as variáveis que estão apresentadas no ficheiro (nome_ficheiro)
    Requires: O ficheiro (nome_ficheiro) que contem as variáveis necessárias à função simular_populacoes (num_meses,param)
    Ensures:Um dicionário com o nome das variáveis como chave e como valor a quantidade numérica da respectiva variável que tem como chave
    """
    ficheiro1 = open(nome_ficheiro, 'r')
    parametros = {}
    nome = []
    valor = []
    for linha in ficheiro1:
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
    x = [0]
    DicEco = obter_parametros(nome_ficheiro)
    while x[-1] == 0:
        FuntionX = menu()
        x.append(1)
        t = 0
    while True:
        if FuntionX[-2] == 's':
            if FuntionX[-1] == 'q':
                if t != 0:
                    try:
                        print(cenouras)
                        nao_necessario, cenouras, coelhos, lobos, param, t = simular_populacoes(int(FuntionX[-3]), DicEco, t)
                        print(cenouras)
                        gravar_resultado_simulacao('resultados.csv', cenouras, coelhos, lobos)
                        print('Simulador Terminado.')
                        exit()
                    except:
                        print(cenouras)
                        nao_necessario, cenouras, coelhos, lobos, param, t = simular_populacoes(int(FuntionX[-1]), DicEco, t)
                        print(cenouras)
                        gravar_resultado_simulacao('resultados.csv', cenouras, coelhos, lobos)
                        print('Simulador Terminado.')
                        exit()
                if t == 0:
                    nao_necessario, cenouras, coelhos, lobos, param, t = simular_populacoes(0, DicEco, 0)
                    gravar_resultado_simulacao('resultados.csv', cenouras, coelhos, lobos)
                    print('Simulador Terminado.')
                    exit()
            else:
                FinalAnswer, cenouras, coelhos, lobos, param, t = simular_populacoes(int(FuntionX[-1]),DicEco, t)
                print(FinalAnswer)
                FuntionX = menu()
        if FuntionX[-2] == 'd':
            if t==0:
                FinalAnswer, cenouras, coelhos, lobos, param, t = simular_populacoes(t,DicEco, t)
                if FuntionX[-1] == 'c':
                    plt.plot(cenouras, linestyle='-', marker='o', color = 'orange')
                    plt.xlabel('Número de Meses')
                    plt.ylabel('Número de Cenouras')
                    plt.title('Simulação de Ecossistema')
                    plt.show()
                    FuntionX = menu()
                if FuntionX[-1] == 'r':
                    plt.plot(coelhos, linestyle='-', marker='o', color = 'c')
                    plt.xlabel('Número de Meses')
                    plt.ylabel('Número de Coelhos')
                    plt.title('Simulação de Ecossistema')
                    plt.show()
                    FuntionX = menu()
                if FuntionX[-1] == 'w':
                    plt.plot(lobos, linestyle='-', marker='o', color = 'b')
                    plt.xlabel('Número de Meses')
                    plt.ylabel('Número de Lobos')
                    plt.title('Simulação de Ecossistema')
                    plt.show()
                    FuntionX = menu()
                if FuntionX[-1] == 'q':
                    if t != 0:
                        try:
                            nao_necessario, cenouras, coelhos, lobos, param, t = simular_populacoes(int(FuntionX[-3]), DicEco, t)
                            gravar_resultado_simulacao('resultados.csv', cenouras, coelhos, lobos)
                            print('Simulador Terminado.')
                            exit()
                        except:
                            print(cenouras)
                            nao_necessario, cenouras, coelhos, lobos, param, t = simular_populacoes(int(FuntionX[-1]), DicEco, t)
                            print(cenouras)
                            gravar_resultado_simulacao('resultados.csv', cenouras, coelhos, lobos)
                            print('Simulador Terminado.')
                            exit()
                    if t == 0:
                        nao_necessario, cenouras, coelhos, lobos, param, t = simular_populacoes(0, DicEco, t)
                        gravar_resultado_simulacao('resultados.csv', cenouras, coelhos, lobos)
                        print('Simulador Terminado.')
                        exit()
            if t!=0:
                if FuntionX[-1] == 'c':
                    plt.plot(cenouras, linestyle='-', marker='o', color = 'orange')
                    plt.xlabel('Número de Meses')
                    plt.ylabel('Número de Cenouras')
                    plt.title('Simulação de Ecossistema')
                    plt.show()
                    FuntionX = menu()
                if FuntionX[-1] == 'r':
                    plt.plot(coelhos, linestyle='-', marker='o', color = 'c')
                    plt.xlabel('Número de Meses')
                    plt.ylabel('Número de Coelhos')
                    plt.title('Simulação de Ecossistema')
                    plt.show()
                    FuntionX = menu()
                if FuntionX[-1] == 'w':
                    plt.plot(lobos, linestyle='-', marker='o', color = 'b')
                    plt.xlabel('Número de Meses')
                    plt.ylabel('Número de Lobos')
                    plt.title('Simulação de Ecossistema')
                    plt.show()
                    FuntionX = menu()
                if FuntionX[-1] == 'q':
                    if t != 0:
                        nao_necessario, cenouras, coelhos, lobos, param, t = simular_populacoes(int(FuntionX[-3]), DicEco, t)
                        gravar_resultado_simulacao('resultados.csv', cenouras, coelhos, lobos)
                        print('Simulador Terminado.')
                        exit()
                    if t == 0:
                        nao_necessario, cenouras, coelhos, lobos, param, t = simular_populacoes(0, DicEco, 0)
                        gravar_resultado_simulacao('resultados.csv', cenouras, coelhos, lobos)
                        print('Simulador Terminado.')
                        exit()
        if FuntionX[-1] == 'q':
            if t != 0:
                try:
                    nao_necessario, cenouras, coelhos, lobos, param, t = simular_populacoes(int(FuntionX[-3]), DicEco, t)
                    gravar_resultado_simulacao('resultados.csv', cenouras, coelhos, lobos)
                    print('Simulador Terminado.')
                    exit()
                except:
                    nao_necessario, cenouras, coelhos, lobos, param, t = simular_populacoes(int(FuntionX[-2]), DicEco, t)
                    gravar_resultado_simulacao('resultados.csv', cenouras, coelhos, lobos)
                    print('Simulador Terminado.')
                    exit()
            if t == 0:
                nao_necessario, cenouras, coelhos, lobos, param, t = simular_populacoes(0, DicEco, t)
                gravar_resultado_simulacao('resultados.csv', cenouras, coelhos, lobos)
                print('Simulador Terminado.')
                exit()
    return

#Aqui começa a Etapa 9
def gravar_resultado_simulacao(nome_ficheiro, lista_pop_cenouras, lista_pop_coelhos, lista_pop_lobos):
    """Grava os resultados do número de cada ser vivo em cada mês num formato(.csv)
    Requires:Um ficheiro (nome_ficheiro), uma lista com o número de cenouras em cada mês em que é efectuado a simulação(lista_pop_cenouras),uma lista com o número de coelhos em cada mês em que é efectuado a simulação(lista_pop_coelhos),uma lista com o número de lobos em cada mês em que é efectuado a simulação(lista_pop_lobos)
    Ensures: Um ficheiro .csv com cada mês e o respectivo número de cada ser vivo
    """
    resultados = open(nome_ficheiro, 'w')
    resultados.write('Mês' + ';')
    resultados.write('Cenouras' + ';')
    resultados.write('Coelhos' + ';')
    resultados.write('Lobos' + '\n')
    for i in range(0, len(lista_pop_cenouras)):
        resultados.write(str(i) + ';')
        resultados.write(str(lista_pop_cenouras[i]) + ';')
        resultados.write(str(lista_pop_coelhos[i]) + ';')
        resultados.write(str(lista_pop_lobos[i]) + '\n')
    return resultados

simulador("configuracao.txt")
