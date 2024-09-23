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
        # Calcular el número de variables selectoras para la reduccion
        variables_selectoras = numeroVariables - 1  # Fórmula s = n - 1
        return variables_selectoras,variable_control
    
    def recalcular_entradas(self, variables_selectoras):
        # Recalcula el número de entradas a partir de las variables selectoras
        numero_entradas = pow(2,variables_selectoras)
        return numero_entradas
    
    def generar_tabla_mux(self, numero_entradas):
        print("TABLA MUX")
        # Genera combinaciones en formato decimal para A' y A
        combinaciones = list(range(2 ** numero_entradas))
        mitad = len(combinaciones) // 2  # Dividimos en dos mitades

        # Ajustamos la cantidad de combinaciones para mostrar solo las necesarias
        fila_A_negada = combinaciones[:mitad]  # A'
        fila_A = combinaciones[mitad:mitad + len(fila_A_negada)]  # A, solo tomamos las necesarias

        # Crear la tabla final con las combinaciones decimales
        tabla = [
            ["A'"] + fila_A_negada,  # Fila de A'
            ["A"] + fila_A  # Fila de A
        ]

        # Nombres de las columnas (I0, I1, I2, etc.)
        columnas = [f'I{i}' for i in range(len(fila_A_negada))]

        return tabla, columnas
    
    def marcar_minterms(self, fila, minterms):
        # Marcamos los minterms en una fila con '1' si es minterm, '0' si no lo es
        return [1 if valor in minterms else 0 for valor in fila]

    def generar_tabla_mux_binarios(self, numero_entradas):
        print("TABLA MUX CON MINTERMINOS MARCADOS")
        # Genera combinaciones en formato decimal para A' y A
        combinaciones = list(range(2 ** numero_entradas))
        mitad = len(combinaciones) // 2  # Dividimos en dos mitades

        fila_A_negada = combinaciones[:mitad]  # A'
        fila_A = combinaciones[mitad:mitad + len(fila_A_negada)]  # A

        # Marcar los minterms en A' y A
        fila_A_negada_marcada = self.marcar_minterms(fila_A_negada, self.minterms)
        fila_A_marcada = self.marcar_minterms(fila_A, self.minterms)

        # Crear la tabla marcada con los minterms
        tabla_marcada = [
            ["A'"] + fila_A_negada_marcada,  # Fila con minterms marcados en A'
            ["A"] + fila_A_marcada  # Fila con minterms marcados en A
        ]

        # Nombres de las columnas (I0, I1, I2, etc.)
        columnas = [f'I{i}' for i in range(len(fila_A_negada))]

        return tabla_marcada, columnas, fila_A_negada_marcada, fila_A_marcada

    def comparar_columnas(self, fila_A_negada, fila_A):
        resultado = []
        for i in range(len(fila_A_negada)):
            if fila_A_negada[i] == 1 and fila_A[i] == 1:
                # Si ambos son minterms
                resultado.append(1)
            elif fila_A_negada[i] == 1:
                # Si solo A' tiene el minterm
                resultado.append("A'")
            elif fila_A[i] == 1:
                # Si solo A tiene el minterm
                resultado.append("A")
            else:
                # Ningún minterm
                resultado.append(0)
        return resultado