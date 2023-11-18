import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from hmmlearn import hmm
import joblib

# Cargar el dataset
data = pd.read_csv('../../../DataSet.csv')

# Extract the "Value" column as the observations for the HMM
train_data = data[['CategoryId', 'Output', 'EmotionId']].values

print("Train Data")
print(train_data)

# Define the number of states for the HMM
state_id = data['EmotionId'].unique()
n_states = len(state_id)
state_names = data['Emotion'].unique()

#Initialize the HMM model
model = hmm.GaussianHMM(n_components=n_states, covariance_type="full")

# Fit the HMM model to the observations
model.fit(train_data)

# # Predict the hidden states for each observation
# hidden_states = model.predict(np.array([[3, 1, 1]]))

# Save the model
filename = 'TrainedHMM.joblib'
joblib.dump(model, filename)

print('\t**********Trained Markov Hidden Model*********************')
print('\t...to predict use TrainedHMM.joblib')
print(f'\tHidden status id: {n_states}-->{state_id}')
print(f'\tHidden status names: {n_states}-->{state_names}')
print(f"\tObservable states: 3-->['CategoryId' 'Output' 'EmotionId']")
print("\t***********************************************************")