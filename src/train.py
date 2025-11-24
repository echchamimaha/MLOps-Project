import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import sys

def main(input_path, model_path):
    df = pd.read_csv(input_path)

    # Features / target
    X = df.drop("label", axis=1)
    y = df["label"]

    model = LinearRegression()
    model.fit(X, y)

    joblib.dump(model, model_path)
    print(f"Modèle sauvegardé dans {model_path}")

if __name__ == "__main__":
    input_path = sys.argv[1]
    model_path = sys.argv[2]
    main(input_path, model_path)
