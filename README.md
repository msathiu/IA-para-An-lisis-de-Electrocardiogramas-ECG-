# IA para Análisis de Electrocardiogramas (ECG)

Este proyecto tiene como objetivo desarrollar una solución de inteligencia artificial para el análisis de electrocardiogramas utilizando datos de la **MIT-BIH Arrhythmia Database**. El pipeline del proyecto abarca la conversión de señales ECG a imágenes, la creación de un DataFrame con las etiquetas correspondientes, la división de los datos en conjuntos de entrenamiento, validación y prueba, y el entrenamiento de una red neuronal convolucional (CNN) para la clasificación de latidos.

---

## 📂 Estructura del Proyecto

La organización del repositorio es la siguiente:

```
IA-para-An-lisis-de-Electrocardiogramas-ECG-/
│
├── data/ 
│   └── (Archivos originales de la base de datos MIT-BIH: .dat, .hea, .atr, etc.)
│
├── processed_data/
│   ├── images/ 
│   │   └── (Imágenes generadas a partir de los segmentos de ECG, organizadas por clase)
│   ├── ecg_data.csv  (CSV con la ruta de las imágenes y sus etiquetas)
│   ├── split_data/ 
│   │   ├── train/  (Imágenes para entrenamiento)
│   │   ├── val/    (Imágenes para validación)
│   │   └── test/   (Imágenes para prueba)
│   ├── train_data.csv
│   ├── val_data.csv
│   └── test_data.csv
│
├── notebooks/
│   └── (Jupyter Notebooks para análisis exploratorio y pruebas)
│
├── scripts/
│   ├── 1_convert_ecg_to_images.py  (Script para convertir ECG a imágenes y generar un CSV con las etiquetas)
│   ├── 2_clean_and_split_data.py   (Script para dividir los datos en conjuntos de entrenamiento, validación y prueba)
│   └── 3_train_cnn_model.py        (Script para entrenar la red neuronal convolucional)
│
├── models/
│   └── (Modelo entrenado se guardará aquí, por ejemplo: ecg_cnn_model.h5)
│
├── requirements.txt  (Librerías y dependencias necesarias)
└── README.md         (Este archivo)
```

---

## ⚙️ Requisitos

- Python 3.7 o superior
- [wfdb](https://github.com/MIT-LCP/wfdb-python)
- matplotlib
- pandas
- scikit-learn
- tensorflow (o tensorflow-cpu, según tu configuración)

Instala todas las dependencias con:

```bash
pip install -r requirements.txt
```

---

## 🚀 Cómo Empezar

1. **Clonar el Repositorio:**

   ```bash
   git clone https://github.com/msathiu/IA-para-An-lisis-de-Electrocardiogramas-ECG-.git
   cd IA-para-An-lisis-de-Electrocardiogramas-ECG-
   ```

2. **Colocar los Datos Originales:**

   - Coloca los archivos originales de la **MIT-BIH Arrhythmia Database** en la carpeta `data/`.

3. **Conversión de ECG a Imágenes y Generación del CSV:**

   Ejecuta el script:
   ```bash
   python scripts/1_convert_ecg_to_images.py
   ```
   Este script extrae los segmentos de latidos, los guarda como imágenes organizadas por clase y genera el archivo `processed_data/ecg_data.csv`.

4. **Dividir los Datos en Conjuntos de Entrenamiento, Validación y Prueba:**

   Ejecuta el script:
   ```bash
   python scripts/2_clean_and_split_data.py
   ```
   Esto moverá las imágenes a las carpetas correspondientes y creará los CSVs para cada conjunto.

5. **Entrenar la Red Neuronal Convolucional:**

   Ejecuta el script:
   ```bash
   python scripts/3_train_cnn_model.py
   ```
   El modelo entrenado se guardará en la carpeta `models/`.

---

## 📖 Descripción de los Scripts

- **`scripts/1_convert_ecg_to_images.py`**  
  Este script carga los registros de ECG y sus anotaciones, extrae segmentos de latidos y los guarda como imágenes en `processed_data/images/`. Además, genera un archivo CSV (`processed_data/ecg_data.csv`) con la ruta de cada imagen y su etiqueta.

- **`scripts/2_clean_and_split_data.py`**  
  Utiliza el CSV generado anteriormente para dividir el dataset en conjuntos de entrenamiento, validación y prueba, organizando las imágenes en la carpeta `processed_data/split_data/` y generando CSVs para cada subconjunto.

- **`scripts/3_train_cnn_model.py`**  
  Este script carga los conjuntos de datos de imágenes y entrena una red neuronal convolucional (CNN) con TensorFlow para clasificar los latidos según sus etiquetas. El modelo entrenado se guarda en `models/ecg_cnn_model.h5`.

---

## 📌 Notas

- Asegúrate de que la estructura de carpetas se mantenga igual para evitar errores en la ejecución de los scripts.
- Si deseas probar el modelo o realizar ajustes, se recomienda trabajar en los notebooks ubicados en la carpeta `notebooks/`.

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si tienes sugerencias o mejoras, por favor crea un _pull request_ o abre un _issue_.

---

## 📄 Licencia

Este proyecto se distribuye bajo la licencia [MIT](LICENSE).

---

¡Gracias por visitar el proyecto! Si tienes alguna pregunta o necesitas asistencia, no dudes en contactar.

---

Este README proporciona una visión general completa del proyecto y cómo ejecutarlo. ¡Adáptalo según tus necesidades!
