
import spacy

nlp = spacy.load("es_core_news_sm")

def procesar_texto(mensaje):

    # procesamiento de lenjage natural 
    doc = nlp(mensaje.lower())

    tokens = []

    for token in doc:

        # Ignorar puntuación y espacios
        if token.is_punct or token.is_space:
            continue

        # Eliminar stopwords, conservando negaciones
        if token.is_stop and token.text not in ["no", "nunca", "jamás"]:
            continue

        # Obtener lema de la palabra
        tokens.append(token.lemma_)

    return tokens


# Prueba
mensaje = "Estoy muy enojado porque me insultaron"

resultado = procesar_texto(mensaje)

print("Mensaje original:", mensaje)
print("Tokens procesados:", resultado)
