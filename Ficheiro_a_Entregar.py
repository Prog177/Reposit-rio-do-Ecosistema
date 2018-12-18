#Aqui começa a Etapa 1
#####
#####


#Pce0=50000
#Rce=1
#Pcemax=10000
#Mce = 5
#Pco0 = 50
#Pcomax = 1000
#Mco = 2
#Plo0 = 5
#Plomax = 100
#Mlo = 0.0005
q="q"
Q="Q"
Eco={0: 50000, 1: 1, 2: 100000, 3: 5, 4:50,5:1000,6: 2,7:5,8:100,9:0.0005}
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
    if Iteration==0:
        EcosystemPython.write(('Mês '+str(Iteration)+' : '+str(50000) +' cenouras,'+str(50)+' coelhos,'+str(5)+' lobos')+('\n'))
        Iteration+=10
        Month+=1
    for Iteration in range(0,num_meses) and not Iteration==0:
        CenourasIntermidiate=evoluir_populacao_cenouras (param[Iteration+0],param[1],param[2],param[3],param[Iteration+4])
        CoelhosIntermidiate=evoluir_populacao_coelhos (param[Iteration+4],param[Iteration+0],param[3],param[5],param[6],param[Iteration+7])
        LobosIntermidiate=evoluir_populacao_lobos (param[Iteration+7],param[Iteration+4],param[6],param[8],param[9])
        param[Iteration] = str(CenourasIntermidiate)
        param[Iteration+4] = str(CoelhosIntermidiate)
        param[Iteration+7] = str(LobosIntermidiate)
        EcosystemPython.write(('Mês '+str(Month)+' : '+str(Pce0) +' cenouras,'+str(Pco0)+' coelhos,'+str(Plo0)+' lobos')+('\n'))
        Iteration+=10
        Month+=1
    for Iteration2 in range(0,Iteration,3):
        FinalReturn+=('Mês '+str(MonthFor)+' : '+str(param[Iteration2])+' cenouras,'+str(param[Iteration2+1])+' coelhos,'+str(param[Iteration2+2])+' lobos')+('\n')
        MonthFor+=1
    EcosystemPython.close()    
    return FinalReturn

#Aqui começa a Etapa 5
def menu():
    print("Quantos meses pretende simular?")
    Months=eval(input())
    Output=""
    if type(Months)!=int and Months!="q" and Months!="Q":
        print("Caracter inválido!")
        menu()
    elif type(Months)==int:
        Output=Months
    elif  Months=="q" or Months=="Q":
        Output="Simulador Terminado."
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
    

    #DicEco=obter_parametros(nome_ficheiro)
    InternalFile.close()
    print(DicEco)

    FuntionX=menu()
    FinalAnswer=simular_populacoes(FuntionX,DicEco)
    return FinalAnswer
print(simulador('configuracao.txt'))

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


