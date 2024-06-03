import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from solucion import funcion_entrada

funcion_entrada("input_prueba_3.txt")