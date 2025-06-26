def pesquisa_binária(lista, x):
    posição_baixo = 0
    posição_alto = len(lista) - 1
    while posição_baixo <= posição_alto:
        meio = posição_alto - (posição_alto - posição_baixo) // 2
        chute = lista[meio]
        if chute == x:
            print(f'O item {x} é o {meio + 1}º item da lista (índice {meio}).')
            return True
        elif chute > x:
            posição_alto = meio - 1
        elif chute < x:
            posição_baixo = meio + 1
    print(f'O item {x} não está na lista.')
    return False     

exemplo_lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
pesquisa_binária(exemplo_lista, 80)