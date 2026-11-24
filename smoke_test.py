import sys
from pathlib import Path

import joblib
import pandas as pd
from sklearn.model_selection import train_test_split

ROOT = Path(__file__).resolve().parent.parent
FEATURES = ["Hours_Studied", "Attendance", "Previous_Scores",
            "Motivation_Level", "Parental_Involvement", "Access_to_Resources"]

try:
    # 1. load the saved pipeline
    model = joblib.load(ROOT / "models" / "G01_model.joblib")
    # 2. rebuild the same test set and predict three rows
    df = pd.read_csv(ROOT / "data" / "stage1_students.csv")
    df["high_score"] = (df["Exam_Score"] >= 70).astype(int)
    _, X_test, _, y_test = train_test_split(df[FEATURES], df["high_score"], test_size=0.2,
                                            random_state=42, stratify=df["high_score"])
    sample = X_test.head(3)
    predictions = model.predict(sample)
    probabilities = model.predict_proba(sample)[:, 1]
except Exception as error:
    # 3. stop with an error message if loading or predicting fails
    sys.exit("SMOKE TEST FAILED: " + str(error))

for i, (p, prob) in enumerate(zip(predictions, probabilities)):
    print(f"Row {i}: predicted class {p}, probability of 70 or more {prob:.3f}, actual {y_test.iloc[i]}")
print("SMOKE TEST PASSED")
