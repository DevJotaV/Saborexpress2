from exercicios.carro import Carro

carro1 = Carro('Toyota', 'Corolla', 'Branco')
carro2 = Carro('Chevrolet', 'Onix', 'Azul')
carro3 = Carro('Honda', 'Civic', 'Preto')

print(f"Carro 1: {carro1._marca} {carro1._modelo}, Cor: {carro1._cor}")
print(f"Carro 2: {carro2._marca} {carro2._modelo}, Cor: {carro2._cor}")
print(f"Carro 3: {carro3._marca} {carro3._modelo}, Cor: {carro3._cor}")
