from tabulate import tabulate

class Reduccion:
    def __init__(self, minterms):
        self.minterms = minterms
        self.num_bits = len(bin(max(minterms))) - 2  # Determina los bits necesarios

    def decimal_a_binario(self, numero):
        # Convierte un número decimal a binario con un número fijo de bits
        return format(numero, f'0{self.num_bits}b')

    def calcular_variables(self, lista_minterminos):
        numero_mayor = max(lista_minterminos)
        numero_variables = len(bin(numero_mayor)) - 2
        return numero_variables