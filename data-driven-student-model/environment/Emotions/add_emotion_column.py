import numpy as np
import pandas as pd
import pprint
import os
from emotions_values import emotions

# Ruta del DataSet
data_path = '../../../DataSet.csv'

# Cargar el dataset
data = pd.read_csv(data_path)

# Covertir a valores numericos las emociones
emotions_num = {
    'Neutral' :   0,
    'Happy'   :   1,
    'Sad'     :   2,
    'Surprise':   3,
    'Fear'    :   4,
    'Disgust' :   5,
    'Anger'   :   6,
    'Contempt':   7
}

emotions_data = [emotions_num[emotion] for emotion in emotions]
print(emotions_data, len(emotions))

# Agregar al DataSet la colmna 'Emotion' y 'EmotionId'
data.loc[:, 'Emotion'] = emotions
data.loc[:, 'EmotionId'] = emotions_data

# Guardar el dataset modificado con la nueva columna
data.to_csv(data_path, index=False)
pprint.pprint(data)
