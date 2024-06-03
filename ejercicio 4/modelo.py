from tensorflow.keras.models import load_model
import numpy as np
class ModeloClasificador:
    def __init__(self, nombre_modelo):
        self.modelo_cargado = load_model(nombre_modelo)
        self.labels = ["low","medium","high"]
    
    def predecir_clase_cliente(self, id_cliente):
        prediccion = self.modelo_cargado.predict(np.array([id_cliente]))
        predicted_class = np.argmax(prediccion, axis=1)
        print(f"El cliente es de tipo {self.labels[predicted_class[0]]}")
