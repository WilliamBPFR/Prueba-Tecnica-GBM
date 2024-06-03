import os
import sys

def calcular_camino_mas_corto(numero_buscar: int, n: int) -> int:
    # Se inicializan las variables para el ciclo
    camino_mas_corto = 0
    numero_secuencia_actual = 0
    n -=1

    '''
    La aproximacion que he seguido para resolver el problema es mas logica: calculo el camino mas largo 
    sin dar ni un paso atras, luego voy dando un paso atras y luego voy hacia adelante, si el camino es mas corto, 
    entonces sustituyo ese camino por el camino mas corto actual. Si el camino es mas largo, entonces termino el ciclo.

    Cada paso atras por el que empiezo se cuenta, por eso el valor absoluto de n, para que no haya problemas con la cantidad de pasos que he dado.
    '''
    camino_mas_corto = abs(n)
    paso_secuencia = abs(n)
    numero_secuencia_actual = n


    while numero_secuencia_actual != numero_buscar:
        paso_secuencia += 1
        camino_mas_corto += 1
        if numero_secuencia_actual < numero_buscar:
            numero_secuencia_actual += paso_secuencia
        elif numero_secuencia_actual > numero_buscar:
            numero_secuencia_actual -= 1

    return camino_mas_corto

def funcion_entrada(archivo_input: str = "input.txt"):
    # Se verifica si el archivo existe en la ruta actual, si no se agrega la ruta del archivo por defecto, input.txt
    if not os.path.exists(archivo_input):
        sys.path.append(os.path.dirname(os.path.dirname(__file__)))
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    arreglo_numeros_buscar = []

    # Se abre el archivo y se leen las lineas
    with open(archivo_input, "r") as texto:
        arreglo_numeros_buscar = [int(linea) for linea in texto.readlines()]

    # Se verifica si el numero de casos esta entre 1 y 1000
    if arreglo_numeros_buscar[0] > 1000 or arreglo_numeros_buscar[0] < 1:
        print("EL numero de casos (primera linea del input), debe ser menor o igual a 1000 y mayor o igual a 1")
        return

    # Se recorre el arreglo de numeros a buscar
    for numero_calcular in arreglo_numeros_buscar[1:]:

        # Se verifica si el numero a calcular esta entre 1 y 106
        if numero_calcular > 106 or numero_calcular < 1:
            print(f"Error con numero {numero_calcular}. El numero debe ser mayor o igual que 1 y menor o igual que 106")

        else:
            # Se inicializan las variables para el ciclo    
            camino_corto_confirmado = False
            iteracion = 1
            camino_mas_corto_actual = 0
            
            # Se calcula el camino mas corto
            while camino_corto_confirmado == False:
                camino_mas_corto = calcular_camino_mas_corto(numero_calcular, iteracion)            

                if camino_mas_corto_actual == 0:
                    camino_mas_corto_actual = camino_mas_corto
                elif camino_mas_corto_actual > camino_mas_corto:
                    camino_mas_corto_actual = camino_mas_corto
                else:
                    camino_corto_confirmado = True

                iteracion -= 1
                
            print(f"El camino mas corto para {numero_calcular} es: ", camino_mas_corto_actual)

if __name__ == "__main__":
    funcion_entrada()