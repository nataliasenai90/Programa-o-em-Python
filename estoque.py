# dicionarios
estoque = {

    'livros' : {
        'livro 1': 10.0,
        'livro 2': 20.55, 
        'livro 3': 50.6
        },

    'tablets': {
        'tablet 1': 500.5, 
        'tablet 2': 250.5, 
        'tablet 3': 470.3
        },

    'fones': {
        'fone 1': 126.5, 
        'fone 2': 450.0, 
        'fone 3': 155.6
        }
        
}

carrinho = []
total = []

sec = input(f'Escolha uma seção\n{estoque.keys()}: ')
prod = input(f'Escolha o produto\n{estoque[sec]}: ')
print('Adicionar ao carrinho: 🛒🛒', prod)
carrinho.append(prod)
total.append(estoque[sec][prod])

sec = input(f'Escolha uma seção\n{estoque.keys()}: ')
prod = input(f'Escolha o produto\n{estoque[sec]}: ')
print('Adicionar ao carrinho: 🛒🛒', prod)
carrinho.append(prod)
total.append(estoque[sec][prod])


soma  = sum(total)
print('R$', soma)
print(carrinho)
lista = ['', '1. PIX', '2. Crédito', '3. Débito']
pag =  int(input(f'Escolha a forma de pagamento:\n{lista}: '))
print('Sua forma de pagamento é', lista[pag])
print('Obrigada! Volte Sempre!')

input('Digite enter para sair... ')