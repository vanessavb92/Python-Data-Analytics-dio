capacidade_atual, aumento_percentual = map(int, input().split())

# TODO: Calcule a nova capacidade do disco de Mithril
new_capacity = capacidade_atual + capacidade_atual*aumento_percentual/100

# TODO: Imprima a nova capacidade
print(f'{new_capacity:.0f}')
ALTERNATIVA B
capacidade_atual, aumento_percentual = map(int, input().split())
# TODO: Calcule a nova capacidade do disco de Mithril
# TODO: Imprima a nova capacidade
print('%d' %(capacidade_atual + capacidade_atual*aumento_percentual/100))