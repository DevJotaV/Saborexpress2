#Exercicio1
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_pizza = Restaurante()
restaurante_praca.categoria = 'Italiana'
#Exercicio2
restaurante_praca.nome = 'Bistro'
#Exercicio3
if restaurante_praca.ativo == False:
    print('está desativado')
else:
    print('esta ativado')


#Exercicio4
categoria = Restaurante.categoria
#Exercicio5
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
#Exercicio6
restaurante_pizza.ativo = True
#Exercicio7
print(vars(restaurante_praca))