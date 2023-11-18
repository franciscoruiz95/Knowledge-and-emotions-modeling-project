import gym
from gym import spaces
import numpy as np
from environment.Knowledge.BKT_algorithm import BKT
import joblib
import settings as ST

# Crear el modelo de estudiante basado en reglas
class StudentModel(gym.Env):
    def __init__(self):
        super().__init__()
        self.action = np.random.randint(5)
        self.reward = 0.0
        self.state = np.random.randint(ST.N_STATE)
        # Se instancia un modelo BKT por cada acción (categoría) 
        self.P = {
            action : BKT(action + 1) for action in range(0, 5) 
        }

        self.emotions_names = {
            0:  'Neutral' ,
            1:  'Happy'   ,
            2:  'Sad'     ,
            3:  'Surprise',
            4:  'Fear'    ,
            5:  'Disgust' ,
            6:  'Anger'   ,
            7:  'Contempt'
        }

        # Se carga el Modelo Oculto de Markov entrenada para predecir las emociones
        self.HMMmodel = ST.HMM

        # Acciones: 5 categorías {0 : Aritmética, 1 : Proporciones, 2 : Geometría, 3 : Porcentajes, 4 : Tiempo-Velocidad}
        self.action_space = spaces.Discrete(5)

        # Observaciones: 8 emociones
        self.observation_space = spaces.Discrete(ST.N_STATE)

    def step(self, action):
        print(action)
        probability = self.P[action].probability()
        print(probability)
        self.reward = np.random.choice([0, 1], p=[1 - probability, probability])
        print(self.reward)
        self.action = action
        # se pasa self.action + 1 porque el modelo fue entrenado con las categorias del 1 al 5
        self.state = ST.MAPPER_TO_STATE[self._predict_next_state([self.action + 1, self.reward, ST.MAPPER_TO_HIDDEN_STATE[self.state]])[0]]
        self.P[action].update(self.reward)
        # self.render()
        print(self.state)
        return self.state, self.reward , False, False, {}  # Devolver observación, recompensa

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.action = 0
        self.reward = 0
        self.state = 0

        return self.state, {}  # Estado inicial aleatorio

    def render(self):
        print(f"State: {self.state}, Action: {self.action}, Reward: {self.reward}")
    
    def _predict_next_state(self, seq):
        seq = np.array([seq])
        return self.HMMmodel.predict(seq)