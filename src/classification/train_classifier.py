import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Charger embeddings sauvegardés
embeddings = np.load("data/embeddings/embeddings.npy")
df = pd.read_csv("data/processed/dataset_cleaned.csv")

X = embeddings
y = df["type"]

# Train / Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Modèle
clf = LogisticRegression(max_iter=1000)

clf.fit(X_train, y_train)

# Évaluation
y_pred = clf.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Sauvegarde modèle
joblib.dump(clf, "models/ticket_classifier.pkl")

print("Modèle sauvegardé dans models/")
