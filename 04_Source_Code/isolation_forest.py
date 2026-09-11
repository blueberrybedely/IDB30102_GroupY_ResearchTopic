import pandas as pd
from sklearn.ensemble import IsolationForest

data = pd.read_csv("ics_dataset.csv")

features = data.select_dtypes(include=["number"])

model = IsolationForest(
    contamination="auto",
    random_state=42
)

model.fit(features)

data["anomaly_label"] = model.predict(features)

data["anomaly_status"] = data["anomaly_label"].map({
    1: "Normal",
    -1: "Anomalous"
})

print(data[["anomaly_label", "anomaly_status"]].head())
