import os
import tensorflow as tf

# --- CONFIGURACIÓN ---
batch_size = 32
img_size = (128, 128)
data_path = "processed_data/split_data"

# Cargar datos
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    os.path.join(data_path, "train"), image_size=img_size, batch_size=batch_size)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    os.path.join(data_path, "val"), image_size=img_size, batch_size=batch_size)

# Mostrar nombres de clases cargadas
print(f"Clases detectadas: {train_ds.class_names}")
print(f"Tamaño del dataset - Entrenamiento: {len(train_ds)} batches, Validación: {len(val_ds)} batches")
