import os
import sys

def buscar_ganadores(num_pilotos: int, num_grand_prix: int,arreglo_solucion: list):
    # Se obtiene el arreglo de las posiciones de los pilotos en cada carrera y el arreglo de los puntos por carrera
    arreglo_posiciones_carreras = arreglo_solucion[0:num_grand_prix]
    arreglo_distribucion_puntos = arreglo_solucion[num_grand_prix+1:len(arreglo_solucion)]

    # Se crea un diccionario con los puntos de cada piloto, en el cual almacenaremos al piloto y los puntos que saca por cada sistema de puntos
    diccionario_puntos = {indice+1: 0 for indice in range(num_pilotos)}

    # Se recorre el arreglo de los diferentes sistemas de puntos
    for sistema_puntos in arreglo_distribucion_puntos:

        # Se obtiene el numero de posiciones ganadoras y los puntos por posicion
        puntos = [int(punto) for punto in sistema_puntos.split()[1:]]
        cant_posiciones_prix = int(sistema_puntos[0])

        if cant_posiciones_prix > num_pilotos:
            print("Los sistemas de puntos no pueden tener mas posiciones ganadoras que pilotos en la carrera")
        else:

            numero_posiciones_ganadoras = int(sistema_puntos.split()[0])

            # Se recorre el arreglo de las posiciones de los pilotos en cada carrera
            for carrera in arreglo_posiciones_carreras:
                # Se convierte el arreglo de posiciones en un arreglo de enteros
                carrera = [int(posicion) for posicion in carrera.split()]

                # Se recorre el arreglo de las posiciones de los pilotos en cada carrera
                for i in range(num_pilotos):
                    # Se verifica si la posicion del piloto en la carrera es menor o igual al numero de posiciones ganadoras
                    if carrera[i] <= numero_posiciones_ganadoras:
                        # Se le suman los puntos al piloto segun los puntos de su posicion
                        diccionario_puntos[i+1] += puntos[carrera[i]-1]

            # se obtiene el piloto o los pilotos con el maximo puntaje, se imprimen y se reinician los puntos de los pilotos
            ganadores = [clave for clave, valor in diccionario_puntos.items() if valor == max(diccionario_puntos.values())]
            print(" ".join([str(ganador) for ganador in ganadores]))
            diccionario_puntos = {indice+1: 0 for indice in range(num_pilotos)}


def funcion_entrada(nombre_archivo: str = "input.txt"):
    # Se verifica si el archivo existe en la ruta actual, si no se agrega la ruta del archivo por defecto, input.txt
    if not os.path.exists(nombre_archivo):
        sys.path.append(os.path.dirname(os.path.dirname(__file__)))
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Se abre el archivo y se leen las lineas
    with open(nombre_archivo,"r") as texto:
        # Se eliminan los saltos de linea, se guardan en una listay se declaran las variables iniciales para el ciclo
        datos = texto.readlines()
        datos = [dato.strip() for dato in datos]
        terminacion = True
        fila = 0
        num_pilotos = 0
        num_grand_prix = 0

        while(terminacion):
            # Se verifica si la fila actual es diferente de "0 0" para continuar con la ejecucion
            if datos[fila] != "0 0":
                # Se obtienen los valores de la fila #1, que es la cantidad de pilotos y carreras y se convierten a enteros
                num_grand_prix, num_pilotos = datos[fila].split()
                num_pilotos = int(num_pilotos)
                num_grand_prix = int(num_grand_prix)

                if num_grand_prix > 100 or num_grand_prix < 1:
                    print("El numero de Grand Prix debe estar entre 1 y 100. Verifique todos los casos")
                    break

                if num_pilotos > 100 or num_pilotos < 1:
                    print("El numero de pilotos debe estar entre 1 y 100. Verifique todos los casos")
                    break

                '''
                Como sabemos, pueden haber varios casos en un solo archivo asi que despues de obtener los pilotos y
                los numero de prix, lo que queda es una linea con el numero de score systems y despues los score systems.
                Obtenemos el numero de score systems una fila despues del numero de grans prix (datos[fila+1+num_grand_prix])
                Luego, ponemos todos los score system en un solo array.
                '''
                num_score_points = int(datos[fila+1+num_grand_prix])
                score_system_array = datos[fila+1:fila+1+num_grand_prix+num_score_points+1]
                
                # Invocamos la función para buscar e imprimir los ganadores.
                buscar_ganadores(num_pilotos,num_grand_prix,score_system_array) #se pone uno de mas porque el rango no toma el ultimo valor

                # Luego de impreso los ganadores, se actualiza la fila para continuar con el siguiente caso
                fila = fila+1+num_grand_prix+num_score_points +1
            else:
                terminacion = False

if __name__ == "__main__":
    funcion_entrada() #Si quiere ejecutar otro archivo distinto a input.txt, paselo como parametro aqui en esta funcion
    