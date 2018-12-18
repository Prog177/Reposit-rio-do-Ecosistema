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

ficheiro = open('configuracao.txt', 'r')
