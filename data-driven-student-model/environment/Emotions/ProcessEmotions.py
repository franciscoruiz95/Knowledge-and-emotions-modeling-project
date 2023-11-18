import cv2
from controller import cvision
import numpy as np
import pandas as pd
from collections import Counter
import pprint
import os

# Ruta del DataSet
data_path = '../../../DataSet.csv'

# Cargar el dataset
data = pd.read_csv(data_path)

# Obtener las claves unicara para cada user
unique_users = data['UserId'].unique()
# Obtener las claves unicas para cada skill
unique_skills = data['CategoryId'].unique()

# Tamaño deseado del frame (ancho, alto)
desired_frame_size = (640, 480)
# Especifica el número de FPS deseado
desired_fps = 5

# Array que guarda la emocion encontrada para cada video
emotions = []

#recorremos todos los archivos para cada User
for studen in unique_users:
    print(f"Student --> {studen}:")
    #recorremos todos los archivos de video para cada skill
    for skill in unique_skills:
        print(f"\tSkill: {skill}")

        # Crear un objeto VideoCapture y leer desde el archivo de entrada
        # Modificar con la ruta relativa de la carpeta videos
        #folder_path = "~/videos/user_"+ str(studen) + "/skill_" + str(skill)
        folder_path = "/home/francisco/Documentos/semestre-B2023/sistemas-computacionales/proyecto/videos/user_"+ str(studen) + "/skill_" + str(skill)

        # Lista todos los archivos en la carpeta
        files_in_folder = sorted(os.listdir(folder_path))
        print(f"\t{files_in_folder}")

        # Recorremos todos los archivos en la carpeta
        for file in files_in_folder:
            # Crear un objeto VideoCapture y leer desde el archivo de entrada
            print("\t" + folder_path + '/' + file)
            cap = cv2.VideoCapture(folder_path + '/' + file)

            # Verificar si la cámara se abrió correctamente
            if not cap.isOpened():
                print("\tError abriendo el flujo de video o archivo")
            
            #Modificar el tamaño y el nro de FPS
            cap.set(cv2.CAP_PROP_FPS, desired_fps)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, desired_frame_size[0])
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, desired_frame_size[1])


            # Obtener el FPS y el tamaño del frame
            fps = cap.get(cv2.CAP_PROP_FPS)
            fps_total = cap.get(cv2.CAP_PROP_FRAME_COUNT)
            frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

            print(f"FPS: {fps}")
            print(f"Tamaño del frame: {frame_size}")
            print(f"FPS total: {fps_total}")

            # Configuración para procesar cada N frames
            group_size = 10
            frame_count = 0

            # Lista para almacenar las emociones más frecuentes por grupo
            emotion_groups = []

            # Bucle hasta que el video se complete
            while cap.isOpened():
                # Capturar frame por frame
                ret, frame = cap.read()

                if ret and frame is not None:
                    # Incrementar el contador de frames
                    frame_count += 1

                    # Procesar solo si se ha acumulado un grupo completo de frames
                    if frame_count % group_size == 0:
                        # Reconocer expresión facial si se detecta una cara
                        fer = cvision.recognize_facial_expression(frame, False, 3, False)
                        list_emotion = fer.list_emotion
                        # Encontrar la emoción más frecuente en el grupo actual
                        if list_emotion is not None:
                            # Imprimir lista de emociones
                            print(f"\t{list_emotion}")
                            # # Encontrar la emoción más frecuente excluyendo 'Neutral'
                            # non_neutral_emotions = [emotion for emotion in list_emotion if emotion != 'Neutral']
                            # if non_neutral_emotions:
                            most_common_emotion = Counter(list_emotion).most_common(1)[0][0]
                            # Almacenar la emoción más frecuente del grupo actual
                            emotion_groups.append(most_common_emotion)

                        # Mostrar el frame actual
                        # cv2.imshow('Frame', frame)

                    # Presiona 'q' para salir del bucle
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        break

                # Romper el bucle si no hay más frames
                else:
                    break

            # Liberar el objeto de captura de video
            cap.release()

            # Cerrar todas las ventanas
            cv2.destroyAllWindows()

            # Imprimir la emoción más frecuente de todo el video
            if emotion_groups:
                final_emotion = Counter(emotion_groups).most_common(1)[0][0]
                emotions.append(final_emotion)
                print(f"Emoción más frecuente en el video /user_{studen}/skill_{skill}/{file}: {final_emotion}")
            else:
                print("No hay emociones (excluyendo 'Neutral') almacenadas.")

# Mostrar las emociones encontradas para cada usuario y
print(emotions, len(emotions))

# Guardar los valores iniciales en un archivo .py
with open('../emotions_values.py', 'w') as file:
    file.write("emotions = ")
    file.write(emotions)
