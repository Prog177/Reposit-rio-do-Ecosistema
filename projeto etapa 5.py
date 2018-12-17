def menu():
    print("Quantos meses pretende simular?")
    Output=""
    while type(Months)!=int and Months!="q" and Months!="Q":
        print("Caracter inválido!")
        menu()
    if type(Months)==int:
        Output=menu()
    return menu()
    
