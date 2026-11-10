
import joblib

from pathlib import Path
from preprocessing import procesar_texto



# 1. CARGAR MODELOS
print("\nCargando motores de inteligencia artificial...")

# Modelo de emociones
modelo_emociones = joblib.load(
    "modelo/emotion_guard_ai.pkl"
)

# Modelo de seguridad
modelo_seguridad = joblib.load(
    "modelos/modelo_seguridad.pkl"
)

# Vectorizador de seguridad
vectorizador_seguridad = joblib.load(
    "modelos/vectorizador_seguridad.pkl"
)

print("Motor de emociones cargado correctamente.")
print("Motor de seguridad cargado correctamente.")


# 2. MOTOR DE EMOCIONES
def analizar_emocion(mensaje):

    texto_procesado = " ".join(
        procesar_texto(mensaje)
    )

    prediccion = modelo_emociones.predict(
        [texto_procesado]
    )[0]

    print("\n========== MOTOR DE EMOCIONES ==========")

    print("Emoción detectada:", prediccion)

    # Obtener confianza si está disponible
    if hasattr(modelo_emociones, "predict_proba"):

        probabilidades = modelo_emociones.predict_proba(
            [texto_procesado]
        )[0]

        confianza = max(probabilidades) * 100

        print(f"Confianza estimada: {confianza:.2f}%")

    # Alertas emocionales
    if prediccion == "agresividad":

        print("AVISO: Posible expresión agresiva.")

    elif prediccion == "enojo":

        print("AVISO: Posible expresión de enojo.")

    elif prediccion == "ofensivo":

        print("AVISO: Posible lenguaje ofensivo.")

    else:

        print("Sin alerta emocional según la clasificación.")

    print("========================================")

    return prediccion


# 3. MOTOR DE SEGURIDAD
def analizar_seguridad(mensaje):

    texto_procesado = " ".join(
        procesar_texto(mensaje)
    )

    # Convertir texto en valores numéricos
    texto_vectorizado = vectorizador_seguridad.transform(
        [texto_procesado]
    )

    # Clasificar mensaje
    prediccion = modelo_seguridad.predict(
        texto_vectorizado
    )[0]

    print("\n========== MOTOR DE SEGURIDAD ==========")

    print("Clasificación:", prediccion)

    # Obtener confianza estimada
    if hasattr(modelo_seguridad, "predict_proba"):

        probabilidades = modelo_seguridad.predict_proba(
            texto_vectorizado
        )[0]

        confianza = max(probabilidades) * 100

        print(f"Confianza estimada: {confianza:.2f}%")

    # Sistema de alertas de seguridad
    alertas = {
        "ofensivo": "Posible lenguaje ofensivo.",
        "agresividad": "Posible mensaje agresivo o amenazante.",
        "acoso": "Posible situación de acoso.",
        "sexual_no_solicitado": "Posible contenido sexual no solicitado.",
        "phishing_textual": "Posible intento de phishing."
    }

    if prediccion == "seguro":

        print("ESTADO: No se detectó una amenaza según el modelo.")

    elif prediccion in alertas:

        print("ALERTA:", alertas[prediccion])

    print("========================================")

    return prediccion


# 4. MOTOR CENTRAL
def analizar_mensaje(mensaje):

    print("\n\n########################################")
    print("       EMOTION GUARD AI")
    print("########################################")

    print("\nMensaje analizado:")
    print(mensaje)

    # Ejecutar ambos motores
    emocion = analizar_emocion(mensaje)

    seguridad = analizar_seguridad(mensaje)

    # Resultado general
    print("\n========== RESULTADO GENERAL ==========")

    print("Emoción:", emocion)
    print("Seguridad:", seguridad)

    if seguridad != "seguro":

        print("RESULTADO: Se detectó una posible situación de riesgo.")

    else:

        print("RESULTADO: Sin riesgo de seguridad detectado por el modelo.")

    print("########################################")


# 5. INICIO DEL PROGRAMA
print("\n========================================")
print("       BIENVENIDO A EMOTION GUARD AI")
print("========================================")

print("Motores activos:")
print("- Motor de emociones")
print("- Motor de seguridad")

while True:

    mensaje = input("\nEscribe un mensaje (o salir): ")

    if mensaje.lower().strip() == "salir":

        print("\nCerrando Emotion Guard AI...")
        break

    if not mensaje.strip():

        print("Escribe un mensaje válido.")
        continue

    analizar_mensaje(mensaje)
