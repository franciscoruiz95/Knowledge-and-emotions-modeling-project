import numpy as np
import pandas as pd
from BKT_algorithm import BKT
import pprint

def __main__():
    # Cargar el dataset
    data = pd.read_csv('../DataSet.csv')
    # d_f = data[(data['UserId'] == 3) & (data['CategoryId'] == 1)]
    # pprint.pprint(d_f)
    # Obtener las claves unicara para cada estudiante
    unique_users = data['UserId'].unique()
    # Obtener las claves unicas para cada categoria
    unique_skills = data['CategoryId'].unique()

    for studen in unique_users:
        print(f"Student --> {studen}:")
        for skill in unique_skills:
            # Crear una instancia de BKT para cada skill
            bkt_instance = BKT(skill, studen)
            Probability = bkt_instance.fit(data[(data['UserId'] == studen) & (data['CategoryId'] == skill)])
            print(f"\t\tSkill: {skill}, Probability: {Probability}")

__main__()