import pandas as pd
import joblib
from sklearn.metrics import r2_score
import sys

def main(input_path, model_path):
    df = pd.read_csv(input_path)

    X = df.drop("label", axis=1)
    y = df["label"]

    model = joblib.load(model_path)
    preds = model.predict(X)
    score = r2_score(y, preds)

    print(f"R2 score : {score}")

if __name__ == "__main__":
    input_path = sys.argv[1]
    model_path = sys.argv[2]
    main(input_path, model_path)
