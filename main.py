
import spacy
import joblib

# 1. Cargar modelo de lenguaje español
nlp = spacy.load("es_core_news_sm")

# 2. Cargar nuestro modelo de Machine Learning
modelo = joblib.load("modelo/emociones.pkl")
vectorizador = joblib.load("modelo/vectorizador.pkl")


# 3. Procesamiento de lenguaje natural
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


# 4. Motor de emociones
def analizar_emocion(mensaje):

    texto_procesado = procesar_texto(mensaje)

    # Convertir texto en números
    vector = vectorizador.transform([texto_procesado])

    # Realizar predicción
    prediccion = modelo.predict(vector)[0]

    # Obtener puntuación estimada
    probabilidades = modelo.predict_proba(vector)[0]
    confianza = max(probabilidades) * 100

    print("\n========== EMOTION GUARD AI ==========")

    print("Mensaje:", mensaje)
    print("Texto procesado:", texto_procesado)
    print("Emoción detectada:", prediccion)
    print(f"Puntuación del modelo: {confianza:.2f}%")

    # Sistema de alertas
    if prediccion == "agresividad":
        print("ALERTA: Posible mensaje amenazante.")

    elif prediccion == "ofensivo":
        print("ALERTA: Posible lenguaje ofensivo.")

    elif prediccion == "enojo":
        print("AVISO: Posible expresión de enojo.")

    else:
        print("Mensaje sin alerta según la clasificación.")

    print("======================================")


# 5. Programa principal
print("BIENVENIDO A EMOTION GUARD AI")

while True:

    mensaje = input("\nEscribe un mensaje (o salir): ")

    if mensaje.lower().strip() == "salir":
        print("Cerrando Emotion Guard AI...")
        break

    if not mensaje.strip():
        print("Escribe un mensaje válido.")
        continue

    analizar_emocion(mensaje)
