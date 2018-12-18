import math
import matplotlib.pyplot as plt


def menu():
    Months = []
    print('(s)imular, (d)esenhar gráfico')
    Resposta = input('')
    Resposta = Resposta.lower('')
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

