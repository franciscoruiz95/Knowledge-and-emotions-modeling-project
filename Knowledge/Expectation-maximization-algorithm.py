from sklearn.mixture import GaussianMixture as GMM
import numpy as np
import pandas as pd

# Cargar el dataset
#data = pd.read_csv('tu_dataset.csv')

# Configurar la generación de datos aleatorios
np.random.seed(42)

# Número de estudiantes
num_students = 100

# Generar habilidades de manera aleatoria en el rango [0, 5)
skills = np.random.randint(0, 5, size=num_students)

# Generar respuestas (0 o 1) con mayor probabilidad para habilidades más altas
prob_correct = 0.8 - 0.1 * skills
responses = np.random.binomial(1, prob_correct)

# Crear un DataFrame con las habilidades y respuestas
data = pd.DataFrame({'skill': skills, 'response': responses})

print(data)
# Seleccionar las columnas relevantes (skill y response)
X = data[['skill', 'response']]

# Crear un modelo de mezcla gaussiana GMM para obtener los parámetros iniciales
gmm = GMM(n_components=5, random_state=42)  # Ajusta el número de componentes según tu caso
gmm.fit(X) #Estima los parámetros del modelo con el algoritmo EM.

# Obtener los parámetros estimados del GMM
gmm_weights = gmm.weights_
gmm_means = gmm.means_
gmm_covariances = gmm.covariances_
print("gmm_weights:", gmm_weights)
print("gmm_means:", gmm_means)
print("gmm_covariances:", gmm_covariances)

# Calcular los valores iniciales de los parámetros del modelo BKT
PL = np.mean(gmm_weights)  # Usar el peso promedio de los componentes del GMM
PG = np.mean(gmm_means[:, 1])  # Usar la media promedio de la columna 'response'
PS = np.mean(gmm_covariances[:, 1, 1])  # Usar la covarianza promedio de la columna 'response'
# Calcular un valor inicial para PT basado en la suma ponderada de las medias de las habilidades en el GMM
PT = np.sum(gmm_weights * gmm_means[:, 1]) / np.sum(gmm_weights)

# Guardar los valores iniciales en un archivo de texto (txt)
with open('initial_values.txt', 'w') as file:
    file.write(f"Valores iniciales para implementar el modelo BKT\n")
    file.write(f"PL: {PL:2f}\n")
    file.write(f"PG: {PG:2f}\n")
    file.write(f"PS: {PS:2f}\n")
    file.write(f"PT: {PT:2f}\n")

# # Mostrar los valores iniciales calculados
# print("p_init:", PL)
# print("p_guess:", PG)
# print("p_slip:", PS)
# print("p_transit:", PT)