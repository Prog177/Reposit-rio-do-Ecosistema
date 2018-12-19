#Aqui começa a Etapa 1
#####
#####


#Pce0=50000
#Rce=1
#Pcemax=100000
#Mce = 5
#Pco0 = 50
#Pcomax = 1000
#Mco = 2
#Plo0 = 5
#Plomax = 100
#Mlo = 0.0005
q="q"
Q="Q"
Eco={"Pce0": 50000, "Rce": 1, "Pcemax": 100000, "Mce": 5, "Pco0":50,"Pcomax":1000,"Mco": 2,"Plo0":5,"Plomax":100,"Mlo":0.0005}
def evoluir_populacao_cenouras (Pce,Rce,Pcemax,Mce,Pco):
    Pce=int(Pce)
    Rce=int(Rce)
    Pcemax=int(Pcemax)
    Mce=int(Mce)
    Pco=int(Pco)
    PceAfter=Pce+((Rce*Pce)*(1-(Pce/Pcemax)))-(Mce*Pco)
    return round(PceAfter)
#Aqui começa a Etapa 2

def evoluir_populacao_coelhos (Pco,Pce,Mce,Pcomax,Mco,Plo):
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
    Iteration=0
    Month=0
    MonthFor=0
    EcosystemPython=open( 'Ecosystem.txt','w')  #Os ficheiros vão são ser utilizados mais à frente noutra etapa, muito provavelmente.
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

#Aqui começa a Etapa 5
import math
import matplotlib.pyplot as plt


def menu():
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
    parametros = {}
    nome = []
    valor = []
    for linha in nome_ficheiro:
        n,v = linha.split('=')
        nome.append(n)
        valor.append(eval(v))
    for i in range(0, len(nome)):
        parametros.update({nome[i]:valor[i]})
    return parametros
#Aqui começa a Etapa 7
def simulador(nome_ficheiro):
    FileConfig=open(nome_ficheiro,'r')
    DicEco = obter_parametros(FileConfig)
    FileConfig.close()


    FuntionX=menu()
    FinalAnswer=simular_populacoes(FuntionX,DicEco)
    return FinalAnswer

#Aqui começa a Etapa 8
#Aqui começa a Etapa 9
def gravar_resultado_simulacao(nome_ficheiro, lista_pop_cenouras, lista_pop_coelhos, lista_pop_lobos):
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

