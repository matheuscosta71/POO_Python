from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('João', 1)
restaurante_praca.receber_avaliacao('Maria', 5)
restaurante_praca.receber_avaliacao('Carlos', 4)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()