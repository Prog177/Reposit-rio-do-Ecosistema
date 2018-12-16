#Aqui começa a Etapa 4
def simular_populacoes (num_meses,param):
    Iteration=0
    Month=0
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
        Iteration+=4
        Month+=1
    while Iteration<=num_meses and not Iteration==0:
        CenourasIntermidiate=evoluir_populacao_cenouras (Pce0,Rce,Pcemax,Mce,Pco0)
        CoelhosIntermidiate=evoluir_populacao_coelhos (Pco0,Pce0,Mce,Pcomax,Mco,Plo0)
        LobosIntermidiate=evoluir_populacao_lobos (Plo0,Pco0,Mco,Plomax,Mlo)
        Pce0=CenourasIntermidiate
        Pco0=CoelhosIntermidiate
        Plo0=LobosIntermidiate
        param[Iteration] = CenourasIntermidiate
        param[Iteration+1] = CenourasIntermidiate
        param[Iteration+2] = CenourasIntermidiate
        EcosystemPython.write(('Mês '+str(Month)+' : '+str(Pce0) +' cenouras,'+str(Pco0)+' coelhos,'+str(Plo0)+' lobos')+('\n'))
        Iteration+=3
        Month+=1
    for Iteration2 in param:
        param[Iteration2]
        FinalReturn+=param[Iteration2]+"\n"
    EcosystemPython.close()    
    return FinalReturn
print(simular_populacoes (Months,Eco))

