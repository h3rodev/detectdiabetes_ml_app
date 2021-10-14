# 1. Import Libraries

import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

#EDA or Visualization
import seaborn as sns
import matplotlib.pyplot as plt

# 2. Read the the dataset

df = pd.read_csv("diabetesdata.csv")

# 3. EDA

x = np.array(df.drop(['Outcome'], 1))
y = np.array(df['Outcome'])

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
# print(X_train.shape)
# print(X_test.shape)

# 4. Fit the model
classifier = KNeighborsClassifier()

classifier.fit(X_train, y_train)

#print(classifier.score(X_test, y_test))

# 5. Predict the if the patient is Diabetic


def getData(p, g, bp, st, i, bmi, dpf, a):
    example_measures = np.array([[p, g, bp, st, i, bmi, dpf, a]])

    example_measures = example_measures.reshape(len(example_measures), -1)

    outcome = classifier.predict(example_measures).tolist()[0]
    if outcome == 1:
        outcome = "Diabetic"
    else:
        outcome = "Not Diabetic"

    data = {
        "probability": round(classifier.score(X_test, y_test), 2),
        "result": outcome
    }
    return data
