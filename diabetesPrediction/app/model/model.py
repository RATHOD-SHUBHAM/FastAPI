import pickle
from pathlib import Path
import numpy as np

# Get the base directory
BASE_DIR = Path(__file__).resolve(strict=True).parent
print(BASE_DIR)

__version__ = '0.1'

# Load the model
with open(f"{BASE_DIR}/diabetesPrediction.pkl", "rb") as f:
    SVM_Classifier = pickle.load(f)

# Load the model
with open(f"{BASE_DIR}/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

class Prediction:

    def diabetesPrediction(ip_data):
        # changing the input_data to numpy array
        input_data_as_numpy_array = np.asarray(ip_data)

        # reshape the array as we are predicting for one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

        # Standardize ip
        std_data = scaler.transform(input_data_reshaped)

        ip_predictions = SVM_Classifier.predict(std_data)

        if ip_predictions[0] == 1:
           return 'Patient is Diabetic'
        else:
            return 'Patient is Not Diabetic'





