import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import wandb

# Initialize WandB
wandb.login(key="c468f0a8ae0c118cf6cc735f7c2b1e8f6365a3c5")  # Replace with your actual API key
wandb.init(project="distance_classification_project")

# Sample dataset
data = {
    "feature1": [1, 2, 3, 4, 5],
    "feature2": [5, 4, 3, 2, 1],
    "label": [0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

# Split dataset
X = df[["feature1", "feature2"]]
y = df["label"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple KNN classifier
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
wandb.log({"Predictions": predictions.tolist()})

print("Predictions:", predictions)

wandb.finish()
