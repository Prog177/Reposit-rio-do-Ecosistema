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

    for Iteration in range(0,(num_meses*10),10):
        
        if Iteration==0:
            Month+=1
            AlternateListCen.append(50000)
            AlternateListCo.append(50)
            AlternateListLo.append(5)

        else:
            print(Iteration)
            print(param)
            CenourasIntermidiate=evoluir_populacao_cenouras (param["Pce0"+str(Iteration)],param["Rce"],param["Pcemax"],param["Mce"],param["Pco0"+str(Iteration)])
            CoelhosIntermidiate=evoluir_populacao_coelhos (param["Pco0"+str(Iteration)],param["Pce0"+str(Iteration)],param["Mce"],param["Pcomax"],param["Mco"],param["Plo0"+str(Iteration)])
            LobosIntermidiate=evoluir_populacao_lobos (param["Plo0"+str(Iteration)],param["Pco0"+str(Iteration)],param["Mco"],param["Plomax"],param["Mlo"])
            param[Pce0+Iteration] = int(CenourasIntermidiate)
            param[Rce+Iteration] = param[1]
            param[Pcemax+Iteration] = param[2]
            param[Mce+Iteration] = param[3]
            param[Pco0+Iteration] = str(CoelhosIntermidiate)
            param[Pcomax+Iteration] = param[5]
            param[Mco+Iteration] = param[6]
            param[Plo0+Iteration] = str(LobosIntermidiate)
            param[Plo0max+Iteration] = param[8]
            param[Mlo+Iteration] = param[9]
            AlternateListCen.append(CenourasIntermidiate)
            AlternateListCo.append(CoelhosIntermidiate)
            AlternateListLo.append(LobosIntermidiate)
            EcosystemPython.write(('Mês '+str(Month)+' : '+str(param[Iteration]) +' cenouras,'+str(param[Iteration+4])+' coelhos,'+str(param[Iteration+7])+' lobos')+('\n'))
            Month+=1

    for Iteration2 in range(0,(num_meses*10),10):
        FinalReturn += ('Mês '+str(MonthFor)+' : '+str(param[Pce0+Iteration2])+' cenouras,'+str(param[Pco0+Iteration2])+' coelhos,'+str(param[Pco0+Iteration2])+' lobos')+('\n')
        MonthFor+=1
        
    return FinalReturn, AlternateListCen, AlternateListCo, AlternateListLo
print(simular_populacoes (Months,Eco))

