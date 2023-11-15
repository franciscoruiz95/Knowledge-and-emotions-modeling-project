from sklearn.mixture import GaussianMixture as GMM
from pyBKT.models import Model
import numpy as np
import pandas as pd
import pprint

# Cargar el dataset
data = pd.read_csv('../DataSet.csv')
pprint.pprint(data)
# definine la ruta del nuevo dataset
data_path = '../dataForEM.csv'

# Renombrar las columnas según los nombres predeterminados de PyBKT
new_data = data[['UserId', 'CategoryId', 'Output']]
new_column_names = {
    'UserId': 'user_id',
    'CategoryId': 'skill_name',
    # 'CategoryName': 'skill_name',
    'Output': 'correct'
}
new_data = new_data.rename(columns=new_column_names)
new_data.to_csv(data_path, index=False)

# skill_data = data[data['sequence_id'] == 1]
# pprint.pprint(skill_data)

# Obtener la lista única de habilidades (skills)
unique_skills_names = new_data['skill_name'].unique()

# Creamos un diccionario para guardar todos los datos Iniciales por cada skill
# initial_values = {skill_name : [PL, PG, PS, PT]}
var = ['p_init', 'p_guess', 'p_slip', 'p_transit']
initial_values = {skill : {val : 0 for val in var} for skill in unique_skills_names}

# Se instancia el modelo EM
model = Model()
model.fit(data_path = data_path)

# Se recorren cada un de los skills y se optiene los valores iniciales
for skill_name in unique_skills_names:
    params = model.params().loc[(str(skill_name))]
    initial_values[skill_name]['p_init'] = params.loc[('prior', 'default')]['value']
    initial_values[skill_name]['p_guess'] = params.loc[('guesses', 'default')]['value']
    initial_values[skill_name]['p_slip'] = params.loc[('slips', 'default')]['value']
    initial_values[skill_name]['p_transit'] = params.loc[('learns', 'default')]['value']

#leer el mensaje del archivo message.txt
with open('message.txt', 'r') as file:
    # Lee el contenido del archivo y lo guarda en una variable
    message = file.read()

# Guardar los valores iniciales en un archivo .py
with open('initial_values.py', 'w') as file:
    file.write(f"{message}\n")
    file.write("initial_values = {\n")
    for skill, values in initial_values.items():
        file.write(f"\t{skill} : " + "{\n")
        for val, initial  in values.items():
            file.write(f"\t\t'{val}'\t: {round(initial, 6)},\n")
        file.write("\t},\n")
    file.write("}")