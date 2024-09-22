from tabulate import tabulate

class Reduccion:
    def __init__(self, minterms):
        self.minterms = minterms
        self.num_bits = len(bin(max(minterms))) - 2  # Determina los bits necesarios

    def decimal_a_binario(self, numero):
        # Convierte un número decimal a binario con un número fijo de bits
        return format(numero, f'0{self.num_bits}b')

    def generar_tabla_binarios(self):
        # Genera la tabla con minitérminos decimales y su representación en binario
        tabla = [[minterm, self.decimal_a_binario(minterm)] for minterm in self.minterms]
        return tabulate(tabla, headers=["Decimal", "Binario"], tablefmt="grid")

    def mostrar_tabla(self):
        # Imprime la tabla de binarios
        print(self.generar_tabla_binarios())
