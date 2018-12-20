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
        if FuntionX == 'fechar':
            print('Simulador Terminado.')
            exit()
        if FuntionX[-2] == 's':
            if FuntionX[-1] == 'q':
                if t != 0:
                    nao_necessario, cenouras, coelhos, lobos = simular_populacoes(t-1, obter_parametros('configuracao.txt'))
                    gravar_resultado_simulacao('resultados.csv', cenouras, coelhos, lobos)
                    print('Simulador Terminado.')
                    exit()
                if t == 0:
                    nao_necessario, cenouras, coelhos, lobos = simular_populacoes(0, obter_parametros('configuracao.txt'))
                    gravar_resultado_simulacao('resultados.csv', cenouras, coelhos, lobos)
                    print('Simulador Terminado.')
                    exit()
            else:
                FinalAnswer, cenouras, coelhos, lobos = simular_populacoes(FuntionX[-1],DicEco)
                print(FinalAnswer)
                t = len(cenouras)
                FuntionX = menu()
        if FuntionX[-2] == 'd':
            if t == 0:
                nao_necessario, cenouras, coelhos, lobos = simular_populacoes(0, obter_parametros('configuracao.txt'))
            if t != 0:
                nao_necessario, cenouras, coelhos, lobos = simular_populacoes(t-1, obter_parametros('configuracao.txt'))
                print(cenouras)
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
                    nao_necessario, cenouras, coelhos, lobos = simular_populacoes(t-1, obter_parametros('configuracao.txt'))
                    gravar_resultado_simulacao('resultados.csv', cenouras, coelhos, lobos)
                    print('Simulador Terminado.')
                    exit()
                if t == 0:
                    nao_necessario, cenouras, coelhos, lobos = simular_populacoes(0, obter_parametros('configuracao.txt'))
                    gravar_resultado_simulacao('resultados.csv', cenouras, coelhos, lobos)
                    print('Simulador Terminado.')
                    exit()
        if FuntionX[-1] == 'q':
            if t != 0:
                nao_necessario, cenouras, coelhos, lobos = simular_populacoes(t-1, obter_parametros('configuracao.txt'))
                gravar_resultado_simulacao('resultados.csv', cenouras, coelhos, lobos)
                print('Simulador Terminado.')
                exit()
            if t == 0:
                nao_necessario, cenouras, coelhos, lobos = simular_populacoes(0, obter_parametros('configuracao.txt'))
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

