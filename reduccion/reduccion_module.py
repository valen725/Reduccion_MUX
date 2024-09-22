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
        # Número total de combinaciones (2^n)
        total_combinaciones = 2 ** self.num_bits
        tabla = []

        # Generar todas las combinaciones posibles
        for i in range(total_combinaciones):
            combinacion_binaria = self.decimal_a_binario(i)  # Obtener combinación en binario
            es_minterm = 1 if i in self.minterms else 0  # Verificar si es minterm (1) o no (0)
            fila = list(combinacion_binaria) + [es_minterm]  # Agregar la combinación con su valor
            tabla.append(fila)
        
        return tabla, self.num_bits

    def asignar_variable_control(self, numeroVariables):
        # Asigna la variable de control por defecto (A) o selecciona la que cambia menos
        # En este caso, tomamos por defecto la 'A', pero puedes extender esta lógica si lo necesitas.
        variable_control = 'A'
        print(f"\nLa variable de control asignada es: {variable_control}")
        
        # Calcular el número de variables selectoras
        variables_selectoras = numeroVariables - 1  # Fórmula s = n - 1
        return variables_selectoras
    
    def recalcular_entradas(self, variables_selectoras):
        # Recalcula el número de entradas a partir de las variables selectoras
        numero_entradas = 2 ** variables_selectoras
        return numero_entradas