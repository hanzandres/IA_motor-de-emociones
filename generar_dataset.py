
import pandas as pd
from pathlib import Path

# ==========================================
# EMOTION GUARD AI
# GENERADOR DEL DATASET
# ==========================================

# Definimos las categorías del sistema
dataset = {
    "normal": [],
    "felicidad": [],
    "tristeza": [],
    "enojo": []
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
# CATEGORIA: NORMAL
# ==========================================

dataset["normal"] = [

    "Hola, cómo estás",
    "Buenos días, cómo amaneciste",
    "Ya llegué a mi casa",
    "Voy camino a la escuela",
    "Nos vemos mañana",
    "A qué hora empieza la clase",
    "Ya terminaste tu tarea",
    "Hoy tengo que trabajar",
    "Voy a preparar algo de comer",
    "Me puedes pasar la información",
    "El archivo está en mi computadora",
    "Mañana tenemos reunión",
    "Ya revisé el documento",
    "Estoy esperando el autobús",
    "Qué hiciste durante el día",
    "Ahorita regreso",
    "Voy a salir un momento",
    "Ya está listo el proyecto",
    "Me puedes llamar después",
    "Dónde dejaste las llaves",
    "Tengo que comprar algunas cosas",
    "El profesor dejó una actividad",
    "Nos toca entregar el trabajo",
    "Ya instalé el programa",
    "Estoy actualizando mi computadora",
    "La reunión será por la tarde",
    "Te mando el archivo más tarde",
    "Hoy tengo clases en la mañana",
    "Voy a revisar mis pendientes",
    "El transporte viene retrasado",
    "Qué película vamos a ver",
    "Ya terminé de desayunar",
    "Necesito cargar mi teléfono",
    "El internet está funcionando",
    "Voy a ordenar mi habitación",
    "A qué hora sales del trabajo",
    "Estoy haciendo unas compras",
    "El paquete todavía no llega",
    "Puedes revisar este documento",
    "Tengo que imprimir unas hojas",
    "La biblioteca cierra temprano",
    "Hoy toca trabajar en equipo",
    "Ya guardé los cambios",
    "Voy a encender la computadora",
    "El archivo tiene varias páginas",
    "Me falta terminar una actividad",
    "Dónde podemos reunirnos",
    "La clase empieza a las ocho",
    "Tengo que organizar mis horarios",
    "Voy a consultar el calendario",
    "El proyecto tiene tres apartados",
    "Ya hice una copia del archivo",
    "Puedes compartir tu pantalla",
    "El profesor está revisando los trabajos",
    "Mañana iremos a la universidad",
    "Necesito comprar un cuaderno",
    "La tienda está cerca de aquí",
    "Voy a preparar mi mochila",
    "El teléfono tiene poca batería",
    "Ya recibí tu correo",
    "Te comparto el enlace del documento",
    "Estoy leyendo un libro",
    "La computadora necesita actualizarse",
    "Voy a buscar información",
    "El autobús pasa cada veinte minutos",
    "Tenemos que revisar los requisitos",
    "La actividad está en la plataforma",
    "Puedes enviarme el horario",
    "Voy a guardar este documento",
    "Ya organicé mis carpetas",
    "El archivo está en formato PDF",
    "Hoy tenemos una exposición",
    "Necesito conectar el cargador",
    "La impresora no tiene papel",
    "Voy a preparar la presentación",
    "El equipo está en el laboratorio",
    "Tenemos que instalar las dependencias",
    "El programa ya está funcionando",
    "Voy a comprobar la conexión",
    "La base de datos tiene cinco tablas",
    "Ya terminé de escribir el código",
    "El servidor está encendido",
    "Voy a revisar los registros",
    "La aplicación necesita una actualización",
    "El documento tiene algunos cambios",
    "Mañana revisamos los resultados",
    "Estoy organizando mis archivos",
    "Puedes abrir la carpeta del proyecto",
    "La contraseña está guardada en el gestor",
    "Voy a consultar el manual",
    "El sistema tiene varias opciones",
    "La entrega es el viernes",
    "Ya preparé los materiales",
    "El horario aparece en la página",
    "Tengo una pregunta sobre la actividad",
    "Voy a terminar este pendiente",
    "Nos vemos en la entrada",
    "El salón está en el segundo piso",
    "Ya llegué a la universidad",
    "estas bien amor"

]


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
if len(df) != 400:
    raise ValueError(f"Se esperaban 400 mensajes y hay {len(df)}.")

print("Cantidad total:", len(df))
print("Mensajes vacíos: 0")
print("Mensajes duplicados: 0")
print("Validación completada correctamente.")



# ==========================================
# GENERAR ARCHIVO CSV
# ==========================================

# Mezclar los mensajes para evitar que queden agrupados
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Crear la carpeta datasets si todavía no existe
carpeta_datasets = Path(__file__).resolve().parent / "datasets"

carpeta_datasets.mkdir(exist_ok=True)

# Ruta del nuevo dataset de emociones
ruta = carpeta_datasets / "dataset_emociones.csv"

df.to_csv(ruta, index=False, encoding="utf-8-sig")

print("\n========== DATASET GENERADO ==========")
print("Archivo:", ruta)
print("\nDistribución de categorías:")
print(df["emocion"].value_counts())

print("\nPrimeros 10 registros:")
print(df.head(10).to_string(index=False))

print("\n¡DATASET GENERADO CORRECTAMENTE!")



