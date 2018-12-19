#Aqui começa a Etapa 1

q="q"
Q="Q"
Eco={"Pce0": 50000, "Rce": 1, "Pcemax": 100000, "Mce": 5, "Pco0":50,"Pcomax":1000,"Mco": 2,"Plo0":5,"Plomax":100,"Mlo":0.0005}
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
def simular_populacoes (num_meses,param):
    """ Calcula o número Cenouras Coelhos e Lobos após Um número de meses inserido pelo utilizador
    Requires: num_meses que deve ser um inteiro positivo, e um dicionário que contem as variáveis necessárias p'ra as fun~es utilizadas p'ra calcular o número de seres vivos
    Ensures: A string com o número de meses e os respectivos números de cada espéciede ser vivo.E depois 3 listas em que cada lista contem a quantidade em cada mês de cada espécie de ser vivo, as listas são respectivamente de Cenouras, Coelhos e Lobos.
    """
    Iteration=0
    Month=0
    MonthFor=0
    FinalReturn=""
    FileConfig = open('configuracao.txt','r')
    AlternateListCen=[]
    AlternateListCo=[]
    AlternateListLo=[]

    for Iteration in range(0,num_meses+1):
        
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

    for Iteration2 in range(0,num_meses+1):
        if Iteration2==0:
            FinalReturn += ('Mês '+str(MonthFor)+' : '+str(param["Pce0"])+' cenouras,'+str(param["Pco0"])+' coelhos,'+str(param["Pco0"])+' lobos')+("\n")
            MonthFor+=1

        else:
            FinalReturn += ('Mês '+str(MonthFor)+' : '+str(param["Pce0"+str(Iteration2)])+' cenouras,'+str(param["Pco0"+str(Iteration2)])+' coelhos,'+str(param["Plo0"+str(Iteration2)])+' lobos')+("\n")
            MonthFor+=1
        
    return FinalReturn, AlternateListCen, AlternateListCo, AlternateListLo

#Aqui começa a Etapa 5 e Etapa 8
import math
import matplotlib.pyplot as plt


def menu():
    """Através do input que pede ao utilizador simula o crescimento da população ou mostra um gráfico de uma espécie que o utilizador escolhe
    Requires: A função não requer quaisquer parâmetros
    Ensures: Calcula o número de cada espécie apôs um número específico de meses introduzido pelo utilizador ou constroí um gráfico com a evolução do ser vivo escolhido pelo utilizador do mês zero até ao mês introduzido pelo utilizador
    """
    Months = []
    print('(s)imular, (d)esenhar gráfico')
    Resposta = input()
    Resposta = Resposta.lower()
    if Resposta == 's':
        print("Quantos meses pretende simular?")
        Months.append(eval(input()))
        Output = ""
        if type(Months[-1])!= int and Months[-1] != "q":
            print("Caracter inválido!")
            menu()
        elif type(Months[-1])==int:
            Output = Months[-1]
        elif  Months[-1] == "q":
            Output = "Simulador Terminado."
    elif  Resposta == "q":
        Output = "Simulador Terminado."
    if Resposta == 'd':
        nao_necessario, cenouras, coelhos, lobos = simulador(Months[-1])
        plt.plot(cenouras, color = 'g')
        plt.plot(coelhos, color = 'orange')
        plt.plot(lobos, color = 'b')
        plt.xlabel('Número de Meses')
        plt.ylabel('Número de Seres Vivos')
        plt.title('Evolução das Populações')
        plt.show()
    return Output

    
#Aqui começa a Etapa 6
def obter_parametros(nome_ficheiro):
    """Constroí um dicionário com as variáveis que estão apresentadas no ficheiro (nome_ficheiro)
    Requires: O ficheiro (nome_ficheiro) que contem as variáveis necessárias à função simular_populacoes (num_meses,param)
    Ensures:Um dicionário com o nome das variáveis como chave e como valor a quantidade numérica da respectiva variável que tem como chave
    """
    parametros = {}
    nome = []
    valor = []
    for linha in nome_ficheiro:
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
    FileConfig=open(nome_ficheiro,'r')
    DicEco = obter_parametros(FileConfig)
    FileConfig.close()
    FuntionX=menu()
    FinalAnswer=simular_populacoes(FuntionX,DicEco)
    return FinalAnswer

#Aqui começa a Etapa 9
def gravar_resultado_simulacao(nome_ficheiro, lista_pop_cenouras, lista_pop_coelhos, lista_pop_lobos):
    """Grava os resultados do número de cada ser vivo em cada mês num formato(.csv)
    Requires:Um ficheiro (nome_ficheiro)uma lista com o número de cenouras em cada mês em que é efectuado a simulação(lista_pop_cenouras),uma lista com o número de coelhos em cada mês em que é efectuado a simulação(lista_pop_coelhos),uma lista com o número de lobos em cada mês em que é efectuado a simulação(lista_pop_lobos)
    Ensures: Um ficheiro .csv com cada mês e o respectivo número de cada ser vivo
    """
    resultados = open('resultados.csv', 'a+')
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

