import os
import shutil
import pandas as pd
from sklearn.model_selection import train_test_split
from tqdm import tqdm  # Para la barra de progreso

# --- CONFIGURACIÓN ---
csv_path = "../processed_data/ecg_data.csv"  # Ruta del CSV con los datos
output_folder = "../processed_data/split_data"  # Carpeta donde se guardarán los datos divididos

# Crear carpetas para cada división
for split in ["train", "val", "test"]:
    os.makedirs(os.path.join(output_folder, split), exist_ok=True)

# Cargar DataFrame
df = pd.read_csv(csv_path)

# Dividir datos
train_df, test_df = train_test_split(df, test_size=0.2, stratify=df["label"], random_state=42)
val_df, test_df = train_test_split(test_df, test_size=0.5, stratify=test_df["label"], random_state=42)

# Mover imágenes a sus respectivas carpetas
for dataset, split in zip([train_df, val_df, test_df], ["train", "val", "test"]):
    print(f"📂 Moviendo imágenes a {split}...")
    for _, row in tqdm(dataset.iterrows(), total=len(dataset), desc=f"Procesando {split}"):
        class_folder = os.path.join(output_folder, split, row["label"])
        os.makedirs(class_folder, exist_ok=True)
        shutil.copy(row["image_path"], class_folder)

    # Guardar CSV de la partición
    dataset.to_csv(f"../processed_data/{split}_data.csv", index=False)

print("✅ Datos divididos en entrenamiento, validación y prueba.")
