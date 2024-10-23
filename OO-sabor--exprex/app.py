from modelos.restaurante import Restaurante
from modelos.cadapio.bebida import Bebida
from modelos.cadapio.prato import Prato

restauranta_praca = Restaurante('Praca', 'gourmet')
bebida_suco = Bebida('Suco de melcancia', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Pao frances', 2.0, 'O melhor pao da cidade')
prato_paozinho.aplicar_desconto()
restauranta_praca.adicionar_no_cardapio(bebida_suco)
restauranta_praca.adicionar_no_cardapio(prato_paozinho)

def main():
    restauranta_praca.exibir_cardapio

if __name__ == '__main__':
    main()