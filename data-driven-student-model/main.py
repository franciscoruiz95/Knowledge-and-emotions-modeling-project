import sys
import time
import gym
import numpy as np
from agent import QLearning
from environment import StudentModel
import matplotlib.pyplot as plt
import settings as ST

ENVIRONMENT = "StudentModel-v1"

def get_emotions():
    emotions = []
    for i in ST.STATE_ID_SORTED:
        emotions.append(ST.EMOION_NAMES[i])
    
    return emotions


def graphic(values):
    # Matriz dada
    matrix = np.array(values)

    # Encontrar el máximo para cada fila y su índice correspondiente
    max_indices = np.argmax(matrix, axis=1)
    max_values = np.max(matrix, axis=1)

    # Crear una lista de acciones para el eje x
    acciones = ['Aritmética', 'proporciones', 'Geometría', 'Porcentajes', 'Tiempo-Velocidad']

    # Crear una lista de emociones para el eje y
    # emociones = ['Neutral', 'Happy', 'Sad', 'Surprise', 'Fear', 'Disgust', 'Anger', 'Contempt']
    emociones = get_emotions()

    # Asignar colores para cada emoción
    colores = ['gray', 'cyan', 'magenta', 'blue', 'red', 'yellow', 'orange', 'green', ]

    # Crear un gráfico de líneas que muestre la acción correspondiente al valor máximo para cada emoción
    for i in range(len(emociones)):
        plt.plot(acciones, matrix[i], label=emociones[i], color=colores[i], marker='o')
        # plt.text(acciones[max_indices[i]], max_values[i] + 0.05, f"{max_values[i]:.2f}", ha='center')

    plt.xlabel('Acciones')
    plt.ylabel('Puntaje según Q-learning')
    plt.title('Acciones con puntaje más alto por cada emoción')
    plt.legend()
    plt.show()

if __name__ == "__main__":

    env = gym.make(ENVIRONMENT)
    agent = QLearning(
        env.observation_space.n, env.action_space.n, alpha=0.1, gamma=0.9, epsilon=0.1
    )

    iterations = 10 if len(sys.argv) == 1 else int(sys.argv[1])

    observation, _ = env.reset()
    
    for _ in range(iterations):
        action = agent.get_action(observation, "epsilon-greedy")
        new_observation, reward, terminated, _, _ = env.step(action)
        agent.update(observation, action, new_observation, reward, terminated)
        observation = new_observation
        agent.render('step')
        agent.render()

        print('*************************************************************')

    graphic(agent.q_table)