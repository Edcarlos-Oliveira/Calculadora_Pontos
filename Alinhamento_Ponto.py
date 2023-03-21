print('*'*6, '\033[32mAlinhamento de Pontos com Regra Sarrus\033[m','*'*6)
print()

# Listas de X, res_m e Y:
eixo_x = list()             # Os os valores de X
eixo_y = list()             # Recebe os valores de Y
res_m = list()              # Resultado da multiplicação das diagonais

# Função para coleta dos dados:
while True:
    def x_y ():
        for cx in range(1,4):
            vl_x = int(input(f'Digite o {cx}º valor de \033[33mX\033[m: '))          
            eixo_x.append(vl_x)
        for cy in range(1,4):
            vl_y = int(input(f'Digite o {cy}º valor de \033[35mY\033[m: '))
            eixo_y.append(vl_y) 

    # Função para Multiplicação e Resultado das diagonais:
    def mult_Result ():
        i = 1

        # Multiplicação Diagonal Principal:
        dP = [eixo_x[0] * eixo_y[1], eixo_y[0] * eixo_x[2], eixo_x[1] * eixo_y[2]*i]
        res_m.append(dP) # Adiciona o resultado na lista

        # Multiplicação Diagonal Secundária:
        dS = [eixo_x[2] * eixo_y[1], eixo_x[1] * eixo_y[0], eixo_x[0] * eixo_y[2]*i]
        res_m.append(dS) # Adiciona o resultado na lista
        total = sum(dP) - sum(dS)

        if total == 0:
            print(f'Os pontos \033[34mESTÃO ALINHADOS\033[m, o resultado foi: \033[34m{total}\033[m')
        else:
            print(f'Os pontos \033[31mNÃO ESTÃO ALINHADOS\033[m o resultado foi: \033[31m{total}\033[m')
    
    # Programa Principal
    x_y ()
    mult_Result()

    # Escolhendo continuar ou não com tratamento de erros:
    while True:    
        try:
            op = str(input('Quer continuar \033[32m[S/N]\033[m? ')).strip().upper()
            if op in 'SN':
                break
            print('\033[31mERRO!\033[m Escolha apenas S ou N.')
        except IndexError:
            print('\033[31mERRO!\033[m Escolha apenas S ou N.')
    if op == 'N':
        print('\033[36mFinalizado com Sucesso!\033[m')
        break