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
Eco={0:50000,1:50,2:5}
def evoluir_populacao_cenouras (Pce,Rce,Pcemax,Mce,Pco):
    PceAfter=Pce+((Rce*Pce)*(1-(Pce/Pcemax)))-(Mce*Pco)
    return round(PceAfter)
#Aqui começa a Etapa 2

def evoluir_populacao_coelhos (Pco,Pce,Mce,Pcomax,Mco,Plo):
    Nco=(Pce/(Mce*Pco))
    PcoAfter=Pco+Nco*(1-(Pco/Pcomax))-(Mco*Plo)
    return round(PcoAfter)
#Aqui começa a Etapa 3
def evoluir_populacao_lobos (Plo,Pco,Mco,Plomax,Mlo):
    Nlo=(Pco/(Mco*Plo))
    PloAfter=Plo+Nlo*(1-(Plo/Plomax))-(Mlo*Plo)
    return round(PloAfter)
#Aqui começa a Etapa 4
#Aqui começa a Etapa 4
def simular_populacoes (num_meses,param):
    Iteration=0
    Month=0
    MonthFor=0
    EcosystemPython=open( 'Ecosystem.txt','w')  #Os ficheiros vão são ser utilizados mais à frente noutra etapa, muito provavelmente.
    FinalReturn=""
    if Iteration==0:
        EcosystemPython.write(('Mês '+str(Iteration)+' : '+str(50000) +' cenouras,'+str(50)+' coelhos,'+str(5)+' lobos')+('\n'))
        Iteration+=3
        Month+=1
    while Iteration<=(num_meses*3) and not Iteration==0:
        CenourasIntermidiate=evoluir_populacao_cenouras (Pce0,Rce,Pcemax,Mce,Pco0)
        CoelhosIntermidiate=evoluir_populacao_coelhos (Pco0,Pce0,Mce,Pcomax,Mco,Plo0)
        LobosIntermidiate=evoluir_populacao_lobos (Plo0,Pco0,Mco,Plomax,Mlo)
        Pce0=CenourasIntermidiate
        Pco0=CoelhosIntermidiate
        Plo0=LobosIntermidiate
        param[Iteration] = str(CenourasIntermidiate)
        param[Iteration+1] = str(CoelhosIntermidiate)
        param[Iteration+2] = str(LobosIntermidiate)
        EcosystemPython.write(('Mês '+str(Month)+' : '+str(Pce0) +' cenouras,'+str(Pco0)+' coelhos,'+str(Plo0)+' lobos')+('\n'))
        Iteration+=3
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
        Output=menu()
    elif  Months=="q" or Months=="Q":
        Output=Months
    return Output
    
#Aqui começa a Etapa 6
#Aqui começa a Etapa 7
def simulador(nome_ficheiro):
    DicEco = {}
    InternalFile=open(nome_ficheiro,'r')
    for Lines in InternalFile:
        palavras = Lines.split("=")        #Altera esta merda toda 
        DicEco[palavras[0]] = float(palavras[1])

    InternalFile.close()
    print(DicEco)

 
    FinalAnswer=simular_populacoes(menu(),Eco)
    return FinalAnswer
print(simulador('configuracao.txt'))

#Aqui começa a Etapa 8
#Aqui começa a Etapa 9

