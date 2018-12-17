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
    
