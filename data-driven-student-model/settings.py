import numpy as np
import random 
import pathlib
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import pprint

DATA_PATH = "../DataSet.csv"
# Load DataSet
DATA = pd.read_csv(DATA_PATH)

# Load the saved model HMMM
HMM = joblib.load('environment/Emotions/TrainedHMM.joblib')

# mmm = HMM.predict(np.array([[2, 1, 3]]))
# print(f"predict {mmm[0]}")

# Define the number of states for the HMM
STATE_ID = DATA['EmotionId'].unique()
N_STATE= len(STATE_ID)
STATE_NAMES = DATA['Emotion'].unique()
STATE_ID_SORTED = sorted(STATE_ID)

EMOION_NAMES = {
    0:  'Neutral' ,
    1:  'Happy'   ,
    2:  'Sad'     ,
    3:  'Surprise',
    4:  'Fear'    ,
    5:  'Disgust' ,
    6:  'Anger'   ,
    7:  'Contempt'
}

MAPPER_TO_HIDDEN_STATE = {state : hidden_state for state, hidden_state in enumerate(STATE_ID_SORTED)}
MAPPER_TO_STATE = {hidden_state: state for state, hidden_state in enumerate(STATE_ID_SORTED)}

print(type(STATE_ID_SORTED))
pprint.pprint(STATE_ID_SORTED)
pprint.pprint(MAPPER_TO_HIDDEN_STATE)
pprint.pprint(MAPPER_TO_STATE)