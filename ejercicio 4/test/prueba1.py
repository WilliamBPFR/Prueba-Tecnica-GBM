import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from modelo import ModeloClasificador

clase_modelo = ModeloClasificador('ejercicio 4/customer_classification_model.h5')
cliente = [0.01, -0.01, 0.1]  
clase_modelo.predecir_clase_cliente(cliente)