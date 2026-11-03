
import spacy

# Cargar modelo de lenguaje español
nlp = spacy.load("es_core_news_sm")

# Negaciones que debemos conservar
NEGACIONES = {
    "no",
    "nunca",
    "jamás",
    "jamas",
    "tampoco",
    "ni"
}


def procesar_texto(mensaje):

    # Procesamiento de lenguaje natural
    doc = nlp(str(mensaje).lower().strip())

    tokens = []

    for token in doc:

        # Ignorar puntuación y espacios
        if token.is_punct or token.is_space:
            continue

        # Eliminar stopwords, conservando negaciones
        if token.is_stop and token.text not in NEGACIONES:
            continue

        # Obtener el lema de la palabra
        lema = token.lemma_.strip().lower()

        if lema:
            tokens.append(lema)

    return tokens


# Pruebas
if __name__ == "__main__":

    mensajes = [
        "Estoy muy enojado porque me insultaron",
        "No estoy feliz, hoy me siento triste",
        "Nunca vuelvas a amenazarme",
        "Tampoco me gusta que me hablen así",
        "Estoy muy contento porque aprobé mi examen"
    ]

    for mensaje in mensajes:

        resultado = procesar_texto(mensaje)

        print("\nMensaje original:", mensaje)
        print("Tokens procesados:", resultado)
