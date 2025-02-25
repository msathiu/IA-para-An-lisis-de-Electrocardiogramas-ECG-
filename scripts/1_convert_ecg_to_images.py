import wfdb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from tqdm import tqdm  # Para mostrar la barra de progreso

# --- CONFIGURACIÓN ---
record_name = "100"  # Número de registro (Ejemplo: "100", "101", etc.)
base_data_path = "../data/mit-bih-supraventricular-arrhythmia-database-1.0.0"  # Ruta base desde /scripts
data_path = os.path.join(base_data_path, record_name)  # Ruta del archivo específico
output_folder = "../processed_data/raw_images"  # Carpeta donde se guardarán las imágenes
csv_path = "../processed_data/ecg_data.csv"  # Archivo CSV con rutas y etiquetas

# Crear carpetas de salida si no existen
os.makedirs(output_folder, exist_ok=True)

# --- 1. Cargar Datos ---
print("Cargando datos del ECG...")
record = wfdb.rdrecord(data_path)
annotation = wfdb.rdann(data_path, 'atr')

# Convertir señal a DataFrame
data = pd.DataFrame(record.p_signal, columns=record.sig_name)

# --- 2. Segmentación de Latidos y Guardado de Imágenes ---
window_size = int(0.5 * record.fs)  # 0.5 segundos antes y después del latido
labels = []

total_beats = len(annotation.sample)  # Total de latidos a procesar

print(f"Procesando {total_beats} latidos...")
for idx, symbol in tqdm(zip(annotation.sample, annotation.symbol), total=total_beats):
    if idx - window_size >= 0 and idx + window_size < len(data):
        # Extraer segmento
        beat_segment = data.iloc[idx - window_size: idx + window_size, 0].values

        # Crear carpeta por clase de latido dentro de output_folder
        class_folder = os.path.join(output_folder, symbol)
        os.makedirs(class_folder, exist_ok=True)

        # Generar nombre de imagen
        img_name = f"{symbol}_{idx}.png"
        img_path = os.path.join(class_folder, img_name)

        # Graficar y guardar como imagen
        plt.figure(figsize=(4, 4))
        plt.plot(beat_segment, color="black")
        plt.axis("off")
        plt.savefig(img_path, bbox_inches="tight", pad_inches=0)
        plt.close()

        # Guardar en lista para DataFrame
        labels.append([img_path, symbol])

# Crear DataFrame y guardarlo
df = pd.DataFrame(labels, columns=["image_path", "label"])
df.to_csv(csv_path, index=False)

print(f"✅ Datos guardados en {csv_path}")
