
import pandas as pd
from pathlib import Path

# ==========================================
# EMOTION GUARD AI
# GENERADOR DEL DATASET
# ==========================================

# Definimos las categorías del sistema
dataset = {
    "felicidad": [],
    "tristeza": [],
    "enojo": [],
    "agresividad": [],
    "ofensivo": []
}

# Cantidad de mensajes por categoría
MENSAJES_POR_CATEGORIA = 100

print("EMOTION GUARD AI")
print("Generador de Dataset")
print("Categorías:", list(dataset.keys()))



# ==========================================
# CATEGORIA 1: FELICIDAD
# ==========================================

dataset["felicidad"] = [
    "Estoy muy feliz hoy",
    "Qué bonito se siente lograr algo que me costó tanto",
    "No puedo dejar de sonreír, todo salió increíble",
    "Me da muchísimo gusto verte bien",
    "Hoy sí fue un día de esos que se disfrutan",
    "Estoy emocionado por lo que viene",
    "Me siento orgulloso de lo que conseguí",
    "Qué alegría me dio recibir esa noticia",
    "La verdad, hoy me siento de maravilla",
    "Me encanta pasar tiempo con mi familia",
    "Estoy contentísimo con el resultado",
    "Me hizo el día que me tomaras en cuenta",
    "Qué chido que por fin se nos hizo",
    "Ando de buenas porque todo va mejorando",
    "Me siento muy agradecido por lo que tengo",
    "No sabes la felicidad que me da esto",
    "Me salió todo mejor de lo que esperaba",
    "Estoy feliz de poder compartir este momento",
    "Qué padre que podamos estar juntos",
    "Hoy tengo una sonrisa que no se me quita",
    "Me emociona muchísimo empezar este proyecto",
    "Estoy satisfecho con mi esfuerzo",
    "Me da gusto saber que estás bien",
    "Qué buena noticia, me alegraste la tarde",
    "Por fin pude cumplir una de mis metas",
    "Me siento con mucha energía y entusiasmo",
    "La pasé increíble con mis amigos",
    "Me encanta cómo están saliendo las cosas",
    "Estoy feliz por esta nueva oportunidad",
    "Qué bonito es sentir que voy avanzando",
    "Hoy todo me salió bastante bien",
    "Me siento afortunado de tenerte cerca",
    "Me dio un montón de gusto verte",
    "Estoy celebrando porque lo conseguimos",
    "Qué emoción, ya quiero que llegue ese día",
    "Me encanta cuando compartimos buenas noticias",
    "Estoy de excelente humor esta mañana",
    "Me siento pleno con lo que estoy viviendo",
    "Qué felicidad saber que lo logramos",
    "Me puso de buenas escuchar eso",
    "Estoy muy contento con mi desempeño",
    "Me alegra muchísimo que hayas venido",
    "Hoy tengo motivos de sobra para sonreír",
    "Qué gusto que todo haya salido bien",
    "Me siento motivado para seguir adelante",
    "Estoy feliz de haber aprendido algo nuevo",
    "Me encanta ver que nuestro esfuerzo dio frutos",
    "Qué padre estuvo la reunión de hoy",
    "Me siento muy bien conmigo mismo",
    "Me dio mucha emoción recibir tu mensaje",
    "Estoy agradecido por este día tan bonito",
    "No podría estar más contento con la noticia",
    "Me llena de alegría compartir esto contigo",
    "Qué buena onda que me hayas apoyado",
    "Estoy feliz porque ya estoy viendo resultados",
    "Me siento emocionado y con muchas ganas",
    "Hoy sí que tengo razones para estar de buenas",
    "Me encantó pasar la tarde contigo",
    "Me da mucha satisfacción haberlo terminado",
    "Qué bonito que te acordaras de mí",
    "Estoy feliz de que nuestra amistad siga creciendo",
    "Me siento muy animado para comenzar",
    "La noticia me cayó de maravilla",
    "Qué alegría que todo esté mejor",
    "Estoy contento con la decisión que tomé",
    "Me hace feliz saber que cuento contigo",
    "Hoy fue un día excelente de principio a fin",
    "Me siento orgulloso de no haberme rendido",
    "Qué emoción poder cumplir este sueño",
    "Estoy disfrutando mucho esta etapa",
    "Me da gusto que hayamos llegado a un acuerdo",
    "Me siento feliz y tranquilo",
    "Qué chulada de día, todo salió perfecto",
    "Me puso muy feliz tu visita",
    "Estoy encantado con este nuevo comienzo",
    "Me alegra ver que estás alcanzando tus metas",
    "Hoy me siento más optimista que nunca",
    "Qué padre es compartir los logros",
    "Estoy muy ilusionado con el futuro",
    "Me siento agradecido por tantas cosas buenas",
    "Me dio mucha felicidad escuchar tu voz",
    "Estoy feliz porque pude ayudar",
    "Qué gusto tener un motivo para celebrar",
    "Me siento genial después de terminar mi trabajo",
    "Me encanta cuando estamos todos reunidos",
    "Hoy desperté con muchísimas ganas de hacer cosas",
    "Me siento muy satisfecho con el avance",
    "Qué bonito detalle, me alegraste el día",
    "Estoy feliz de haber tomado esa oportunidad",
    "Me da mucha emoción lo que estamos construyendo",
    "Qué buena vibra se siente hoy",
    "Me siento tranquilo y contento con mi vida",
    "Estoy muy feliz de que estés aquí",
    "Me encanta ver sonreír a las personas que quiero",
    "Qué orgullo me da nuestro equipo",
    "Hoy sí valió la pena todo el esfuerzo",
    "Me siento agradecido y de buenas",
    "Estoy emocionado por conocer algo nuevo",
    "Me hizo muy feliz que me felicitaras",
    "Qué increíble que hayamos podido lograrlo",
]

print("Mensajes de felicidad:", len(dataset["felicidad"]))



# ==========================================
# CATEGORIA 2: TRISTEZA
# ==========================================

dataset["tristeza"] = [
    "Hoy me siento muy triste",
    "Tengo ganas de llorar y no sé por qué",
    "Me pesa mucho que ya no estés aquí",
    "Extraño demasiado a mi familia",
    "Siento que nadie entiende lo que estoy pasando",
    "Últimamente nada me emociona",
    "Me duele recordar cómo terminaron las cosas",
    "Qué feo se siente estar solo",
    "Hoy no tengo ánimos de hacer nada",
    "Me siento vacío desde que te fuiste",
    "Me cuesta aceptar que todo cambió",
    "La verdad, extraño mucho esos días",
    "Me desanimó bastante lo que pasó",
    "Siento un nudo en la garganta",
    "Me duele que ya no hablemos como antes",
    "No tengo ganas de salir ni de convivir",
    "Me siento apagado desde hace varios días",
    "A veces quisiera volver a empezar",
    "Me pone triste que no podamos vernos",
    "Hoy fue un día bastante pesado para mí",
    "Me siento decepcionado de cómo salieron las cosas",
    "Me hace falta tenerte cerca",
    "No puedo evitar sentir nostalgia",
    "Me entristece pensar que ya no volverá a ser igual",
    "Siento que estoy perdiendo algo importante",
    "Me quedé con muchas cosas por decir",
    "Me duele mucho esta despedida",
    "Qué difícil es acostumbrarse a tu ausencia",
    "Me siento solo aunque esté acompañado",
    "No encuentro motivos para celebrar hoy",
    "Me agüita que las cosas no salieran bien",
    "Traigo el ánimo por los suelos",
    "Me dieron ganas de llorar al recordar eso",
    "Me siento desmotivado con todo",
    "Me pesa mucho esta situación",
    "No dejo de pensar en lo que perdí",
    "Me siento triste por haber fallado",
    "Me duele que no hayas podido venir",
    "Extraño cuando todo era más sencillo",
    "Me siento sin fuerzas para continuar hoy",
    "La noticia me dejó muy desanimado",
    "Me entristece que nos hayamos distanciado",
    "Hoy quisiera quedarme en casa y descansar",
    "Me siento muy sensible últimamente",
    "Me da tristeza ver cómo nos alejamos",
    "No sé cómo explicar esta sensación de vacío",
    "Me cuesta mucho levantar el ánimo",
    "Me siento mal por lo que ocurrió",
    "Me duele que las cosas hayan terminado así",
    "Qué triste es despedirse de alguien querido",
    "Me siento nostálgico al ver esas fotografías",
    "No esperaba que esto me afectara tanto",
    "Me hace falta platicar contigo",
    "Hoy tengo el corazón muy pesado",
    "Me siento decepcionado y triste",
    "Me agüita no poder cumplir esa meta",
    "Me da mucha pena que ya no seamos cercanos",
    "Siento que últimamente todo me sale mal",
    "Me quedé muy bajoneado después de eso",
    "Me entristece no haber podido ayudarte",
    "No tengo mucho ánimo para hablar",
    "Me siento desconectado de todos",
    "Me duele recordar nuestra última conversación",
    "Qué difícil es extrañar a alguien",
    "Me siento frustrado y con ganas de llorar",
    "Hoy amanecí con el ánimo muy bajo",
    "Me pone triste que no me hayas escuchado",
    "Me cuesta trabajo dejar ir esos recuerdos",
    "Siento mucha nostalgia por mi infancia",
    "Me pesa que ya no podamos compartir momentos",
    "No me siento bien emocionalmente hoy",
    "Me siento desilusionado por lo que pasó",
    "Me entristece haber perdido esa oportunidad",
    "Tengo un vacío que no sé cómo llenar",
    "Me duele sentir que ya no te importo",
    "Me siento muy vulnerable en este momento",
    "Hoy nada parece salir como esperaba",
    "Me da tristeza no poder estar con ustedes",
    "Me siento cansado de fingir que todo está bien",
    "Me duele que nuestra amistad haya cambiado",
    "Extraño mucho las pláticas de antes",
    "Me siento bajoneado por mis resultados",
    "Me da pena reconocer que estoy triste",
    "No encuentro palabras para explicar mi tristeza",
    "Me afecta mucho sentirme ignorado",
    "Hoy me ganó la nostalgia",
    "Me siento solo en esta etapa",
    "Me pone triste pensar en lo que pudo ser",
    "Me cuesta trabajo sonreír estos días",
    "Me siento desanimado después de ese rechazo",
    "Qué complicado es superar una pérdida",
    "Me duele que no podamos arreglarlo",
    "Me siento triste por estar lejos de casa",
    "Me pesa mucho haberme equivocado",
    "Hoy necesito un momento para mí",
    "Me siento sin ilusión por ahora",
    "Me agüita que no haya salido como quería",
    "Tengo mucha tristeza acumulada",
    "Me cuesta encontrar tranquilidad después de esto",
    "Me siento muy afectado por la situación"
]

print("Mensajes de tristeza:", len(dataset["tristeza"]))



# ==========================================
# CATEGORIA 3: ENOJO
# ==========================================

dataset["enojo"] = [
    "Estoy muy enojado por lo que hiciste",
    "Qué coraje que siempre pase lo mismo",
    "Me molesta muchísimo que no me escuches",
    "Estoy harto de repetir lo mismo",
    "Esta situación ya me tiene cansado",
    "Me da mucho coraje que no respeten mi tiempo",
    "No soporto que cambien los planes a última hora",
    "Estoy irritado porque nada funciona",
    "Me desespera que no pongan atención",
    "La verdad, esto sí me hizo enojar",
    "Me choca que lleguen tarde sin avisar",
    "Estoy fastidiado con tantas excusas",
    "Me molesta que no valoren mi esfuerzo",
    "Qué frustrante que no podamos avanzar",
    "Ya me cansé de esta discusión",
    "Me enfurece que no cumplan su palabra",
    "Estoy de malas por todo lo que pasó",
    "Me da rabia que me culpen sin razón",
    "No es posible que sigan haciendo lo mismo",
    "Me tiene hasta el tope esta situación",
    "Me irrita que interrumpan cuando hablo",
    "Estoy molesto porque no avisaron",
    "Me desespera tener que esperar tanto",
    "Qué poca paciencia me queda con este asunto",
    "Me enoja que no tomen en serio mi trabajo",
    "Estoy harto de tantas mentiras",
    "Me da coraje que ignoren mis mensajes",
    "Me molesta que hagan ruido cuando estudio",
    "Ya estuvo bueno de tantas vueltas",
    "Me saca de quicio que no respeten los acuerdos",
    "Estoy frustrado porque no me sale el ejercicio",
    "Me enoja que siempre me dejen todo al último",
    "Qué fastidio tener que explicar otra vez",
    "Me molesta que hablen sin saber",
    "Estoy muy alterado por esta noticia",
    "Me da muchísimo coraje esa injusticia",
    "Me choca que no acepten sus errores",
    "Estoy perdiendo la paciencia con este problema",
    "Me enfada que no tomen en cuenta mi opinión",
    "Ya me cansé de que todo sea tan complicado",
    "Me pone de malas que no contesten lo acordado",
    "Me irrita que se burlen de mi esfuerzo",
    "Qué enojo que se haya perdido tanto tiempo",
    "Estoy molesto por la falta de respeto",
    "Me frustra que no podamos llegar a un acuerdo",
    "Me enoja que me interrumpan a cada rato",
    "No me parece justo lo que están haciendo",
    "Me tiene muy fastidiado este retraso",
    "Me da coraje que no reconozcan lo que hice",
    "Estoy harto de que no haya soluciones",
    "Me molesta que cambien las reglas sin avisar",
    "Qué desesperante es esta situación",
    "Me enfurece que no respeten los turnos",
    "Estoy de malas porque no dormí bien",
    "Me irrita que siempre haya pretextos",
    "Me enoja que no me den una respuesta clara",
    "Estoy cansado de discutir por lo mismo",
    "Me molesta que se aprovechen de mi paciencia",
    "Me da rabia que no cumplan con su parte",
    "No puedo creer que hayan hecho eso otra vez",
    "Me frustra que no funcione como debería",
    "Estoy muy molesto con el resultado",
    "Qué coraje que se haya cancelado todo",
    "Me choca que no respeten mi espacio",
    "Estoy harto de que me hagan esperar",
    "Me enfada que no escuchen las indicaciones",
    "Me molesta que me cambien el trabajo al final",
    "Me desespera tanta desorganización",
    "Me da coraje que se pierdan mis cosas",
    "Estoy irritado por el ruido de todo el día",
    "Me enoja que no sean claros conmigo",
    "Qué frustración no poder resolverlo",
    "Me molesta que no valoren mi tiempo",
    "Estoy fastidiado de tantas interrupciones",
    "Me da rabia que me responsabilicen de todo",
    "Me tiene cansado esta falta de compromiso",
    "Me enfada que no respeten lo que acordamos",
    "Estoy molesto porque no me avisaste",
    "Me saca de quicio que no cooperen",
    "Qué coraje que no haya salido el plan",
    "Me irrita que hagan comentarios fuera de lugar",
    "Estoy harto de que me ignoren",
    "Me enoja que no revisen bien las cosas",
    "Me desespera que todo se haga al aventón",
    "Me molesta que no me dejen terminar",
    "Estoy frustrado con este resultado",
    "Me da mucho coraje que no sea justo",
    "Ya no tengo paciencia para esta discusión",
    "Me fastidia que no respeten los horarios",
    "Me enoja que me digan una cosa y hagan otra",
    "Qué molesto que no tomen responsabilidad",
    "Estoy de malas por este contratiempo",
    "Me choca tener que solucionar errores ajenos",
    "Me enfada que no haya comunicación",
    "Me molesta que no consideren mi opinión",
    "Estoy cansado de tanta falta de organización",
    "Me da coraje que no se cumpla lo prometido",
    "Me irrita que hagan como si nada hubiera pasado",
    "Esta situación me está sacando de quicio",
    "Me siento muy enojado y frustrado"
]

print("Mensajes de enojo:", len(dataset["enojo"]))


# ==========================================
# CATEGORIA 4: AGRESIVIDAD
# ==========================================

dataset["agresividad"] = [
    "Te voy a golpear si te vuelves a acercar",
    "Quiero hacerte daño",
    "Voy a romper tus cosas para lastimarte",
    "Te voy a atacar cuando salgas",
    "Quiero lastimarte físicamente",
    "Voy a darte una paliza",
    "Te voy a aventar contra la pared",
    "Pienso golpearte hasta que te calles",
    "Voy a destruir tu auto para vengarme",
    "Te espero afuera para arreglar esto a golpes",
    "Quiero partirte la cara",
    "Voy a ir a buscarte para golpearte",
    "Te voy a patear si no te quitas",
    "Quiero romperte la nariz",
    "Voy a lanzarte algo para herirte",
    "Te voy a hacer pagar con golpes",
    "Voy a destrozar todo lo que tengas",
    "Quiero atacarte y hacerte sufrir",
    "Te voy a empujar por las escaleras",
    "Voy a golpearte en cuanto te vea",
    "Te voy a lastimar si sigues molestándome",
    "Quiero darte un golpe para que aprendas",
    "Voy a romperte los dientes",
    "Te voy a perseguir para golpearte",
    "Voy a quemar tus pertenencias",
    "Quiero aventarte al suelo",
    "Te voy a herir con lo que encuentre",
    "Voy a destrozar tu habitación",
    "Te voy a dar una golpiza",
    "Quiero romper tus cosas frente a ti",
    "Voy a agredirte si te acercas",
    "Te voy a lanzar un puñetazo",
    "Quiero golpearte hasta desquitarme",
    "Voy a destruir lo que más quieres",
    "Te voy a tirar al piso",
    "Quiero hacerte sangrar",
    "Voy a ir por ti para atacarte",
    "Te voy a golpear en la cara",
    "Voy a romper tus ventanas para dañarte",
    "Quiero lastimarte con mis propias manos",
    "Te voy a dar una patada",
    "Voy a aventarte al suelo si te acercas",
    "Quiero destrozar tus pertenencias",
    "Te voy a atacar con un objeto",
    "Voy a golpearte para que tengas miedo",
    "Quiero causarte una lesión",
    "Te voy a empujar y tirar al suelo",
    "Voy a romper todo lo que sea tuyo",
    "Te voy a pegar cuando estés distraído",
    "Quiero agredirte físicamente",
    "Voy a buscarte para romperte la cara",
    "Te voy a golpear si vuelves a hablarme así",
    "Quiero hacerte daño de verdad",
    "Voy a aventarte una silla",
    "Te voy a patear en cuanto te acerques",
    "Quiero romperte un brazo",
    "Voy a destrozar tu teléfono para lastimarte",
    "Te voy a dar un puñetazo",
    "Quiero golpearte frente a todos",
    "Voy a lanzarte al suelo",
    "Te voy a atacar con un cuchillo",
    "Quiero herirte para que sufras",
    "Voy a romper la puerta y entrar a golpearte",
    "Te voy a golpear hasta dejarte en el suelo",
    "Quiero destruir tus cosas y hacerte daño",
    "Voy a patearte si no haces lo que digo",
    "Te voy a aventar por las escaleras",
    "Quiero lastimarte con un golpe",
    "Voy a ir a tu casa para golpearte",
    "Te voy a romper la boca a golpes",
    "Quiero atacarte físicamente",
    "Voy a romper tus muebles para desquitarme",
    "Te voy a golpear con todas mis fuerzas",
    "Quiero hacerte una herida",
    "Voy a lanzarte contra la puerta",
    "Te voy a dar varios golpes",
    "Quiero golpearte para que no lo olvides",
    "Voy a destrozar tu bicicleta para dañarte",
    "Te voy a atacar cuando estés solo",
    "Quiero romperte la cara",
    "Voy a golpearte si no te alejas",
    "Te voy a empujar para que te caigas",
    "Quiero lastimarte y no me importa nada",
    "Voy a destruir tus pertenencias por coraje",
    "Te voy a patear hasta que te alejes",
    "Quiero golpearte ahora mismo",
    "Voy a romper tus cosas para que sufras",
    "Te voy a agredir en cuanto te encuentre",
    "Quiero dejarte una lesión",
    "Voy a lanzarte un objeto para golpearte",
    "Te voy a dar una paliza si regresas",
    "Quiero hacerte daño con mis propias manos",
    "Voy a destrozar tu puerta y tus muebles",
    "Te voy a golpear para vengarme",
    "Quiero atacarte y romper tus cosas",
    "Voy a lastimarte si vuelves a acercarte",
    "Te voy a tirar al suelo de un golpe",
    "Quiero golpearte y destruir tus pertenencias",
    "Voy a buscarte para hacerte daño",
    "Voy a golpearte si vuelves a amenazarme"
]

print("Mensajes de agresividad:", len(dataset["agresividad"]))


# ==========================================
# CATEGORIA 5: OFENSIVO
# ==========================================

dataset["ofensivo"] = [
    "Eres un completo idiota",
    "No sirves para nada",
    "Qué persona tan estúpida",
    "Eres un inútil",
    "Tu comentario fue muy ofensivo",
    "Eres un mediocre y no entiendes nada",
    "Qué tonto eres",
    "Das pena con tus comentarios",
    "Eres una persona desagradable",
    "No tienes ni tantita inteligencia",
    "Qué ridículo te ves",
    "Eres un presumido insoportable",
    "Tu actitud es bastante desagradable",
    "Eres un ignorante",
    "Qué comentario tan corriente",
    "No sabes hacer absolutamente nada",
    "Eres un fastidio para todos",
    "Qué persona tan necia",
    "Tu opinión es una tontería",
    "Eres un incompetente",
    "Qué bruto eres para entender",
    "Me parece que eres un patán",
    "Eres una vergüenza",
    "Tus ideas son absurdas",
    "Qué persona tan insoportable",
    "Eres un maleducado",
    "No tienes respeto por nadie",
    "Qué comentario tan tonto",
    "Eres un presumido de primera",
    "Tu comportamiento da vergüenza",
    "Eres un necio",
    "Qué poca capacidad tienes",
    "Eres un payaso",
    "No dices más que tonterías",
    "Qué persona tan molesta",
    "Eres un arrogante",
    "Tu forma de hablar es desagradable",
    "Eres un pesado",
    "Qué comentario tan estúpido",
    "No tienes idea de lo que hablas",
    "Eres un desconsiderado",
    "Qué insoportable puede ser tu actitud",
    "Eres un grosero",
    "Tu trabajo está hecho con las patas",
    "Qué manera tan tonta de pensar",
    "Eres un presumido y maleducado",
    "No aportas absolutamente nada",
    "Qué persona tan desagradable eres",
    "Eres un incompetente total",
    "Tu comentario fue una estupidez",
    "Qué necedad la tuya",
    "Eres un pesado y un grosero",
    "No tienes educación",
    "Qué ridículo comentario hiciste",
    "Eres un inútil para trabajar en equipo",
    "Tu actitud es una porquería",
    "Eres un ignorante presumido",
    "Qué tontería acabas de decir",
    "No sabes ni lo básico",
    "Eres una persona muy desagradable",
    "Qué mal caes con esa actitud",
    "Eres un creído",
    "Tu manera de actuar es patética",
    "Qué comentario tan miserable",
    "Eres un mal compañero",
    "No tienes sentido común",
    "Qué persona tan necia e insoportable",
    "Eres un presumido sin motivo",
    "Tu explicación fue pésima",
    "Eres un grosero de primera",
    "Qué actitud tan absurda",
    "No sabes comportarte",
    "Eres un verdadero fastidio",
    "Qué comentario tan fuera de lugar",
    "Eres un tonto",
    "Tu comportamiento es vergonzoso",
    "Eres un maleducado y arrogante",
    "Qué manera tan absurda de responder",
    "No tienes respeto ni educación",
    "Eres una persona arrogante que no soporta a los demás",
    "Qué persona tan torpe",
    "Tu respuesta fue bastante mediocre",
    "Eres un patán con todos",
    "Qué comentario tan desagradable",
    "No sabes tratar a los demás",
    "Eres un necio de primera",
    "Tu actitud es insoportable",
    "Qué manera tan tonta de expresarte",
    "Eres un completo incompetente",
    "No tienes ni idea de lo que haces",
    "Qué persona tan grosera",
    "Eres un creído y maleducado",
    "Tu comentario fue una falta de respeto",
    "Qué actitud tan patética",
    "Eres un fastidioso",
    "No sabes escuchar ni aprender",
    "Qué tontería de respuesta",
    "Eres una persona muy grosera",
    "Tu comportamiento deja mucho que desear",
    "Eres un idiota y un arrogante"
]

print("Mensajes ofensivos:", len(dataset["ofensivo"]))



# ==========================================
# VALIDACION DEL DATASET
# ==========================================

print("\n========== VALIDANDO DATASET ==========")

# Convertir los mensajes en registros
registros = []

for categoria, mensajes in dataset.items():

    # Comprobar cantidad de mensajes
    if len(mensajes) != MENSAJES_POR_CATEGORIA:
        raise ValueError(
            f"Error: {categoria} tiene {len(mensajes)} mensajes."
        )

    for mensaje in mensajes:
        registros.append({
            "mensaje": mensaje.strip(),
            "emocion": categoria
        })

# Crear DataFrame
df = pd.DataFrame(registros)

# Comprobar mensajes vacíos
if df["mensaje"].isna().any() or (df["mensaje"].str.strip() == "").any():
    raise ValueError("Existen mensajes vacíos.")

# Comprobar mensajes duplicados
duplicados = df[df["mensaje"].str.lower().duplicated()]

if not duplicados.empty:
    print("\nADVERTENCIA: Se encontraron duplicados:")
    print(duplicados.to_string(index=False))
    raise ValueError("Corrige los mensajes duplicados antes de continuar.")

# Comprobar total de mensajes
if len(df) != 500:
    raise ValueError(f"Se esperaban 500 mensajes y hay {len(df)}.")

print("Cantidad total:", len(df))
print("Mensajes vacíos: 0")
print("Mensajes duplicados: 0")
print("Validación completada correctamente.")



# ==========================================
# GENERAR ARCHIVO CSV
# ==========================================

# Mezclar los mensajes para evitar que queden agrupados
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Guardar el archivo en la carpeta del proyecto
ruta = Path(__file__).resolve().parent / "dataset.csv"

df.to_csv(ruta, index=False, encoding="utf-8-sig")

print("\n========== DATASET GENERADO ==========")
print("Archivo:", ruta)
print("\nDistribución de categorías:")
print(df["emocion"].value_counts())

print("\nPrimeros 10 registros:")
print(df.head(10).to_string(index=False))

print("\n¡DATASET GENERADO CORRECTAMENTE!")



