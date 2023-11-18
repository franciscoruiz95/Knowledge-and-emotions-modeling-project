import numpy as np
import pandas as pd
from BKT_algorithm import BKT
import matplotlib.pyplot as plt
import pprint

# Cargar el dataset
data = pd.read_csv('../../../DataSet.csv')
unique_skills_names = data['CategoryName'].unique()
def skill_names(skill):
    skill_name = {
        skill : unique_skills_names[skill],
    }
    return skill_name[skill]

def graph(probability_for_skill):
    # Configura el gráfico
    plt.figure(figsize=(10, 6))
    plt.title('Trayectoria de Probabilidades de aprender una Habilidad')
    plt.xlabel('Iteración')
    plt.ylabel('Probabilidad')

    # Itera sobre las habilidades y grafica las probabilidades
    for skill, probabilities in probability_for_skill.items():
        plt.plot(probabilities, label=f"{skill + 1}: {skill_names(skill)}")

    # Añade leyenda y muestra el gráfico
    plt.legend()
    plt.grid(True)
    plt.show()

def iterator(response):
    Probabilities = {}

    for skill in range(0, 5):
        probability = []
        print(f"\tSkill --> {skill + 1}:")
        # Crear una instancia de BKT para cada skill
        bkt_instance = BKT(skill + 1)
        for resp in response[skill]:
            bkt_instance.update(resp)
            prob = bkt_instance.probability()
            probability.append(prob)
            print(f"\t\tProbability: {prob}")
        print(f"\tSkill: {skill + 1}, Probability total: {prob}")
        Probabilities[skill] = probability
    return Probabilities

def main():
    # Generate ramdon array 0 or 1
    response_0_or_1 = [np.random.randint(2, size=50) for _ in range(0, 5)]
    graph(iterator(response_0_or_1))

    # Generate ramdon array 0 and 1
    response_0_and_1 = []
    iter = 30
    for i in range(0, 5):
        if i % 2 == 0: # Crear un array de ceros
            response_0_and_1.append(np.zeros(iter))
        else: # Crear un array de unos
            response_0_and_1.append(np.ones(iter))
            
    graph(iterator(response_0_and_1))

if __name__ == "__main__":
    main()