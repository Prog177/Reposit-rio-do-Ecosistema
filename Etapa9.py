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
