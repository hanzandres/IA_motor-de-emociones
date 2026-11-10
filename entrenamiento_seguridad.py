
import pandas as pd
import joblib
import matplotlib.pyplot as plt

from pathlib import Path
from preprocessing import procesar_texto

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    classification_report,
    accuracy_score,
    ConfusionMatrixDisplay
)

# 1. CARGAR DATASET
RUTA_DATASET = Path("datasets/dataset_seguridad.csv")
RUTA_MODELOS = Path("modelos")

RUTA_MODELOS.mkdir(exist_ok=True)

datos = pd.read_csv(RUTA_DATASET)

print("========== ENTRENAMIENTO DE SEGURIDAD ==========")
print("Total de mensajes:", len(datos))

# Verificar columnas
if not {"mensaje", "categoria"}.issubset(datos.columns):
    raise ValueError("El dataset debe tener las columnas mensaje y categoria.")

# 2. PROCESAMIENTO DEL TEXTO
print("\nProcesando mensajes...")

datos["procesado"] = datos["mensaje"].apply(
    lambda mensaje: " ".join(procesar_texto(mensaje))
)

X = datos["procesado"]
y = datos["categoria"]


# 3. DIVIDIR DATOS
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nMensajes para entrenamiento:", len(X_entrenamiento))
print("Mensajes para pruebas:", len(X_prueba))


# 4. CONVERTIR TEXTO A VECTORES TF-IDF
vectorizador = TfidfVectorizer(
    ngram_range=(1, 2),
    min_df=1,
    sublinear_tf=True
)

X_train_tfidf = vectorizador.fit_transform(X_entrenamiento)
X_test_tfidf = vectorizador.transform(X_prueba)


# 5. ENTRENAR MODELO
modelo = LogisticRegression(
    max_iter=2000,
    class_weight="balanced",
    random_state=42
)

print("\nEntrenando modelo...")
modelo.fit(X_train_tfidf, y_entrenamiento)

# 6. EVALUAR MODELO
predicciones = modelo.predict(X_test_tfidf)

precision = accuracy_score(y_prueba, predicciones)

print("\n========== RESULTADOS ==========")
print(f"Exactitud (Accuracy): {precision:.2%}")

print("\nReporte de clasificación:")
print(
    classification_report(
        y_prueba,
        predicciones,
        zero_division=0
    )
)


# 7. MATRIZ DE CONFUSIÓN
fig, ax = plt.subplots(figsize=(10, 8))

ConfusionMatrixDisplay.from_predictions(
    y_prueba,
    predicciones,
    cmap="Reds",
    xticks_rotation=45,
    ax=ax
)

plt.title("Matriz de confusión - Seguridad")
plt.tight_layout()

plt.savefig(
    RUTA_MODELOS / "matriz_confusion_seguridad.png"
)

plt.close()

# 8. GUARDAR MODELO Y VECTORIZADOR
joblib.dump(
    modelo,
    RUTA_MODELOS / "modelo_seguridad.pkl"
)

joblib.dump(
    vectorizador,
    RUTA_MODELOS / "vectorizador_seguridad.pkl"
)

print("\n========== ENTRENAMIENTO FINALIZADO ==========")
print("Modelo guardado correctamente.")
print("Vectorizador guardado correctamente.")
print("Matriz de confusión generada.")
