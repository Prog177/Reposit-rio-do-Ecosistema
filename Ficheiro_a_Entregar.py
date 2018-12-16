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
Months=eval(input())
Eco={0:50000,1:50,2:5}#Esta parte do Dicionário pode não ser utilizado na etapa 4 mas pode ser útil a posteriori
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
    Pce0=50000
    Rce=1
    Pcemax=100000
    Mce=5
    Pco0=50
    Pcomax=1000
    Mco=2
    Plo0=5
    Plomax=100
    Mlo=0.0005
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
print(simular_populacoes (Months,Eco))

#Aqui começa a Etapa 5
#Aqui começa a Etapa 6
#Aqui começa a Etapa 7
def simulador(nome_ficheiro):
    InternalFile=open('nome_ficheiro','w') 
    if type(Months)==int:
        EscapeGoat=simular_populacoes(Months,Eco) #Existe algo problema com o Ficheiro
        InternalFile.writelines(EscapeGoat)
        InternalFile.close()
        InternalFile=open('nome_ficheiro','r')
        FinalAnswer=InternalFile.read()
        InternalFile.close()
    elif Months=="q" or Months=="Q":
        FinalAnswer="Simulador Terminado."
    elif type(Months)!=int and not Months=="q" and not Months=="Q":
        FinalAnswer="Caracter inválido!"

    return FinalAnswer
print(simulador('Ecosystem.txt'))
#Aqui começa a Etapa 8
#Aqui começa a Etapa 9
