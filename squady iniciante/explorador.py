# Desafio: A Aventura do Explorador

## Quantidade de entradas
quantidade_passos = int(input())

## Fitro inicial para formatação da saída
if quantidade_passos > 0:
    ## Gerar informação
    for i in range(1,quantidade_passos+1):
        if i == 1: ## Singular do texto de saida
            print(f'Explorador: {i} passo')
        else: ## Plural do texto de saida
            print(f'Explorador: {i} passos')
else:
    print("Nenhum passo dado na floresta.")

    