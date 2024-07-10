import time

# ------------------------------------------------------------------------

elemento= 0
menu = 0
linha = 0
numero = 0
pesquisa = 0
list_cidade = []
list_orgaos = []

# -----------------------------------------------------------------
menu_inicial = """
                        Menu
        
    Nesse programa você poderá realizar uma matrix
    para canditos à emprego em agência do governo.
        
    Exemplo:
                __________________________________________________
               | Vitoria | Serra | Vila Velha | Cariacica | Viana |          
         FAPES |         |       |            |           |       |
         PCES  |         |       |            |           |       |
         PMES  |         |       |            |           |       |
         IASES |         |       |            |           |       |
         IPAJM |         |       |            |           |       |
               ---------------------------------------------------- 
                 
"""
menu_comands = """

    Agora você pode executar os seguintes comandos para navegar:

        1 - Pesquisar dentro da Matriz
        2 - Alterar dados na Matriz.
        3 - Mostrar a Matriz.
          
        4 - Para finalizar o programa.

            """
menu_pesquisa = """

    Digite qual tipo de pesquisa irá realizar:

        1 - Pesquisar um valor
        2 - Pesquisar uma linha
        3 - Pesquisar uma Coluna
        
"""
invalido = """

              Comando Inválido!!!
    Por favor digito só o que é permitido
"""



# 
def FuctionprintMatriz(matriz, elemento, list_orgaos, list_cidade):
    print(f"{'':10}", end="")
    for elemento in list_cidade:
        print(f"{elemento:<15}", end ="")
    print()
    print()
    for i in range(tamanho):
        print(f"{list_orgaos[i]:<10}", end = "")
        for j  in range(tamanho):
            print(f"{matriz[i][j]:<15}", end= "")
        print()
        print()
    print()
    print("{ Juliano De Andrade, Petherson Sacramento, Julia Soares Gomes Paiva. }")

# 
def Fuctionpesquisa(menu_pesquisa, matriz, elemento, list_orgaos, list_cidade):
        print(menu_pesquisa)
        pesquisa = int(input("Digite qual tipo de pesquisar irá realizar: "))

        
        if pesquisa == 1:
            FuctionprintMatriz(matriz, elemento, list_orgaos, list_cidade)
            time.sleep(1)
            valor_procurado = int(input("Digite o valor que deseja pesquisar na matriz: "))
            encontrado = False
            for orgaos, linha in enumerate(matriz):
                for cidades, elemento in enumerate(linha):
                    if elemento == valor_procurado:
                        print(f"Valor encontrado na posição ({orgaos}, {cidades})")
                        time.sleep(1)
                        encontrado = True

            if encontrado == False:
                print("Valor não encontrado na matriz.") 
                time.sleep(0.5)

        
        elif pesquisa == 2:
            FuctionprintMatriz(matriz, elemento, list_orgaos, list_cidade)
            time.sleep(1)
            linha_procurada = int(input("Digite a linha que está procurando: "))
            encontrado = False
            for orgaos, linha in enumerate(matriz):
                if orgaos == linha_procurada:
                    print(f"Valores na linha {linha}")
                    time.sleep(1)
                    encontrado = True
                    
            if encontrado == False:
                print("Linha não encontrada na matriz.") 
                time.sleep(0.5)

    
        elif pesquisa == 3:
            FuctionprintMatriz(matriz, elemento, list_orgaos, list_cidade)
            time.sleep(1)
            coluna_procurada = int(input("Digite o índice da coluna que está procurando: "))
            if 0 <= coluna_procurada < tamanho:
                print(f"Valores na coluna {list_cidade[coluna_procurada]}: ", end="")
                for linha in matriz:
                    print(f"{linha[coluna_procurada]:<15}", end="")
                print()
            else:
                print("Coluna não encontrada na matriz.")
                time.sleep(0.5)

# 
def FunctionalterarDados(orgaos, cidades):
    orgaos = int(input("Digite a linha do elemento que deseja alterar: "))
    cidades = int(input("Digite a coluna do elemento que deseja alterar: "))
    if 0 <= orgaos < 3 and 0 <= cidades < 3:
        novo_valor = int(input(f"Digite o novo valor para a posição ({orgaos}, {cidades}): "))
        matriz[orgaos][cidades] = novo_valor
        print("Valor alterado com sucesso.")
        FuctionprintMatriz(matriz, elemento, list_orgaos, list_cidade)
        time.sleep(1)
    else:
        print("Índice fora dos limites da matriz.")    

# ---------------------------------
for z in range(1):
    print(menu_inicial)
    time.sleep(0.5)
    
    tamanho = int(input("Digite o tamanho da matriz desejada: "))
    matriz = []

    for z in range(tamanho):
        nome_orgaos = str(input("Digite os orgãos públicos: "))
        list_orgaos.append(nome_orgaos)

    for z in range(tamanho):
        nome_cidades = str(input("Digite quais cidades: "))
        list_cidade.append(nome_cidades)

    for orgaos in range(tamanho):    
        linha = []
        for cidades in range(tamanho):
            numero = int(input(f"Digite o número para armazenar {orgaos}, {cidades}: "))
            linha.append(numero)
        matriz.append(linha)
    print("A sua matriz ficou assim:")
    print()
    FuctionprintMatriz(matriz, elemento, list_orgaos, list_cidade)
    time.sleep(2)

# -------------------------------------------------------------------
while menu != 4:

    print(menu_comands)
    menu = int(input("Digite o comando: "))

    # -----------------------------------------------------
    if menu == 1:
        Fuctionpesquisa(menu_pesquisa, matriz, elemento, list_orgaos, list_cidade)

    # -------------------------------------------------
    elif menu == 2:
        FuctionprintMatriz(matriz, elemento, list_orgaos, list_cidade)
        time.sleep(1)
        FunctionalterarDados(orgaos, cidades)

    # --------------------------------------------------------------
    elif menu == 3:
        FuctionprintMatriz(matriz, elemento, list_orgaos, list_cidade)
        time.sleep(1)
    
    #  -----------------------------------------------------------
    elif menu == 4:
        print("Obrigado por utilizar o nosso código '-'")
        print()
        FuctionprintMatriz(matriz, elemento, list_orgaos, list_cidade)

    # -------------------------------------------------------------           
    else:
        print(invalido)
        time.sleep(2)
        print(menu_comands)

#-----------------------------------------------------------------------------------