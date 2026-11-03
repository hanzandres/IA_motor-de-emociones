
import pandas as pd
import joblib
import os

from preprocessing import procesar_texto

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

import matplotlib.pyplot as plt

# 1. CARGAR DATASET=
datos = pd.read_csv("dataset.csv")

# Verificar columnas
if not {"mensaje", "emocion"}.issubset(datos.columns):
    raise ValueError("El dataset debe contener mensaje y emocion.")

datos = datos.dropna(subset=["mensaje", "emocion"])

print("DATASET CARGADO CORRECTAMENTE")
print("Total de mensajes:", len(datos))
print("\nDistribución:")
print(datos["emocion"].value_counts())


# 2. PROCESAMIENTO NLP
print("\nProcesando mensajes con spaCy...")

X = datos["mensaje"].astype(str).apply(
    lambda mensaje: " ".join(procesar_texto(mensaje))
)

y = datos["emocion"].astype(str)

print("Procesamiento NLP completado.")


# ==========================================
# 3. DIVIDIR DATOS
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nDatos separados:")
print("Entrenamiento:", len(X_train))
print("Prueba:", len(X_test))


# ==========================================
# 4. DEFINIR ALGORITMOS
# ==========================================

algoritmos = {
    "Logistic Regression": LogisticRegression(
        max_iter=2000,
        class_weight="balanced"
    ),

    "Multinomial Naive Bayes": MultinomialNB(),

    "Linear SVC": LinearSVC(
        class_weight="balanced",
        random_state=42
    )
}


# ==========================================
# 5. COMPARAR MODELOS
# ==========================================

resultados = {}

validacion = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

print("\n========== COMPARACIÓN DE MODELOS ==========")

for nombre, algoritmo in algoritmos.items():

    pipeline = Pipeline([
        (
            "tfidf",
            TfidfVectorizer(
                ngram_range=(1, 2),
                sublinear_tf=True,
                min_df=1
            )
        ),
        ("clasificador", algoritmo)
    ])

    puntuaciones = cross_val_score(
        pipeline,
        X_train,
        y_train,
        cv=validacion,
        scoring="f1_macro"
    )

    promedio = puntuaciones.mean()

    resultados[nombre] = {
        "pipeline": pipeline,
        "f1": promedio
    }

    print(f"\nModelo: {nombre}")
    print(f"F1-score promedio: {promedio:.4f}")


# ==========================================
# 6. SELECCIONAR MEJOR MODELO
# ==========================================

mejor_nombre = max(
    resultados,
    key=lambda nombre: resultados[nombre]["f1"]
)

mejor_modelo = resultados[mejor_nombre]["pipeline"]

print("\n==========================================")
print("MEJOR MODELO:", mejor_nombre)
print("F1-score de validación:",
      round(resultados[mejor_nombre]["f1"], 4))


# ==========================================
# 7. ENTRENAR MEJOR MODELO
# ==========================================

mejor_modelo.fit(X_train, y_train)

print("\nMODELO ENTRENADO CORRECTAMENTE")


# ==========================================
# 8. EVALUACIÓN FINAL
# ==========================================

predicciones = mejor_modelo.predict(X_test)

print("\n========== RESULTADOS DEL MODELO ==========")

print(
    classification_report(
        y_test,
        predicciones,
        zero_division=0
    )
)

print("\nMATRIZ DE CONFUSIÓN:")

etiquetas = mejor_modelo.classes_

matriz = confusion_matrix(
    y_test,
    predicciones,
    labels=etiquetas
)

print(matriz)


# ==========================================
# 9. GUARDAR MATRIZ COMO IMAGEN
# ==========================================

os.makedirs("modelo", exist_ok=True)

disp = ConfusionMatrixDisplay(
    confusion_matrix=matriz,
    display_labels=etiquetas
)

disp.plot(
    xticks_rotation=45,
    cmap="Blues"
)

plt.title("Matriz de confusión - Emotion Guard AI")
plt.tight_layout()
plt.savefig("modelo/matriz_confusion.png")
plt.close()


# ==========================================
# 10. GUARDAR MODELO COMPLETO
# ==========================================

joblib.dump(
    mejor_modelo,
    "modelo/emotion_guard_ai.pkl"
)

print("\n==========================================")
print("ENTRENAMIENTO FINALIZADO")
print("Mejor modelo:", mejor_nombre)
print("Archivo guardado: modelo/emotion_guard_ai.pkl")
print("Matriz guardada: modelo/matriz_confusion.png")
print("==========================================")
