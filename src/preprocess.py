import pandas as pd
import sys

def main(input_path, output_path):
    # Lire le fichier brut
    df = pd.read_csv(input_path)

    # Exemple simple : supprimer les lignes vides
    df = df.dropna()

    # Sauvegarder le fichier nettoyé
    df.to_csv(output_path, index=False)
    print(f"Preprocessing terminé. Fichier sauvegardé dans {output_path}")

if __name__ == "__main__":
    # Récupérer les chemins depuis les arguments
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    main(input_path, output_path)
