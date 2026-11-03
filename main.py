
import joblib

from preprocessing import procesar_texto

# 1. CARGAR MODELO

modelo = joblib.load("modelo/emotion_guard_ai.pkl")

print("MODELO CARGADO CORRECTAMENTE")

# 2. MOTOR DE EMOCIONES
def analizar_emocion(mensaje):

    # Procesamiento NLP
    texto_procesado = " ".join(procesar_texto(mensaje))

    # Predicción
    prediccion = modelo.predict([texto_procesado])[0]

    print("\n========== EMOTION GUARD AI ==========")

    print("Mensaje:", mensaje)
    print("Texto procesado:", texto_procesado)
    print("Emoción detectada:", prediccion)

    # Obtener clasificador interno
    clasificador = modelo.named_steps["clasificador"]

    # Mostrar confianza solo cuando hay probabilidades disponibles
    if hasattr(clasificador, "predict_proba"):

        probabilidades = modelo.predict_proba([texto_procesado])[0]
        confianza = max(probabilidades) * 100

        print(f"Puntuación estimada: {confianza:.2f}%")

    else:
        print("El modelo no proporciona probabilidades calibradas.")

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


print("\nBIENVENIDO A EMOTION GUARD AI")

while True:

    mensaje = input("\nEscribe un mensaje (o salir): ")

    if mensaje.lower().strip() == "salir":

        print("Cerrando Emotion Guard AI...")
        break

    if not mensaje.strip():

        print("Escribe un mensaje válido.")
        continue

    analizar_emocion(mensaje)
