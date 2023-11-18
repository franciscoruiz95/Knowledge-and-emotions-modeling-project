import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import joblib

# Load the DataSet
data = pd.read_csv('../../../DataSet.csv')
# Load the saved model
HMMmodel = joblib.load('TrainedHMM.joblib')

emotions_num = {
        0:  'Neutral' ,
        1:  'Happy'   ,
        2:  'Sad'     ,
        3:  'Surprise',
        4:  'Fear'    ,
        5:  'Disgust' ,
        6:  'Anger'   ,
        7:  'Contempt'
    }

def predict_next(seq):
    seq = np.array(seq)
    return HMMmodel.predict(seq)

def mun_to_emotion_name(emotion_id):
    return emotions_num[emotion_id]

def graph(emotions, predic_emotions, values):
    # Crear una lista de números para representar el tiempo o el índice de las emociones
    tiempo = list(range(1, len(emotions) + 1))

    # Graficar las emociones reales y predichas
    plt.plot(tiempo, emotions, label='Emociones reales')
    plt.plot(tiempo, predic_emotions, label=f'Emociones predichas\n\n score:{HMMmodel.score(values)}')

    # Añadir etiquetas y leyenda
    plt.xlabel('----')
    plt.ylabel('Emociones')
    plt.legend()

    # Mostrar la gráfica
    plt.show()

def main():
    # Create a list of sequences to test on
    predict_data = data[['CategoryId', 'Output', 'EmotionId']].values

    emotions = data['EmotionId']
    # Iterate through each sequence and print out the predicted next emotion
    predict_next_emotion = predict_next(predict_data)

    for emotion_id, emotion_predic_id in zip(emotions, predict_next_emotion):
        print(f"\t{emotion_id}:{mun_to_emotion_name(emotion_id)}\t\t-->\t{emotion_predic_id}:{mun_to_emotion_name(emotion_predic_id)}")

    graph(emotions, predict_next_emotion, predict_data)

if __name__ == "__main__":
    main()
