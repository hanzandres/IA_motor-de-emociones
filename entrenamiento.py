
import pandas as pd
import spacy

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# 1. Cargar modelo NLP
nlp = spacy.load("es_core_news_sm")

# 2. Cargar dataset
datos = pd.read_csv("dataset.csv")

# 3. Procesamiento NLP
def procesar_texto(mensaje):

    doc = nlp(mensaje.lower())

    tokens = []

    for token in doc:

        if token.is_punct or token.is_space:
            continue

        if token.is_stop and token.text not in ["no", "nunca", "jamas"]:
            continue

        tokens.append(token.lemma_)

    return " ".join(tokens)


datos["procesado"] = datos["mensaje"].apply(procesar_texto)

# 4. Separar datos
X = datos["procesado"]
y = datos["emocion"]

# 5. Vectorización
vectorizador = TfidfVectorizer()
X_vectorizado = vectorizador.fit_transform(X)

# 6. Dividir datos para entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorizado,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# 7. Crear modelo
modelo = LogisticRegression(max_iter=1000)

# 8. Entrenar Machine Learning
modelo.fit(X_train, y_train)

print("MODELO ENTRENADO CORRECTAMENTE")

# 9. Evaluar modelo
predicciones = modelo.predict(X_test)

print("\nRESULTADOS DEL MODELO:")
print(classification_report(y_test, predicciones, zero_division=0))


import joblib
import os

os.makedirs("modelo", exist_ok=True)

joblib.dump(modelo, "modelo/emociones.pkl")
joblib.dump(vectorizador, "modelo/vectorizador.pkl")

print("Modelo guardado correctamente.")