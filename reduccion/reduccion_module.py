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
    
    def crear_tabla_verdad(self):
        print("Esta es la tabla de verdad")

    def asignar_variable_control(self, numeroVariables):
        # Asigna la variable de control por defecto (A) o selecciona la que cambia menos
        # En este caso, tomamos por defecto la 'A', pero puedes extender esta lógica si lo necesitas.
        variable_control = 'A'
        print(f"\nLa variable de control asignada es: {variable_control}")
        
        # Calcular el número de variables selectoras
        variables_selectoras = numeroVariables - 1  # Fórmula s = n - 1
        return variables_selectoras