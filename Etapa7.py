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
