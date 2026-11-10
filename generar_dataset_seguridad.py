
import pandas as pd
from pathlib import Path

# EMOTION GUARD AI
# GENERADOR DE DATASET DE SEGURIDAD

# Objetivo
# Crear un dataset para entrenar un modelo de Machine Learning
# especializado en detectar contenido potencialmente dañino.

# Categorías:
# - seguro
# - ofensivo
# - agresividad
# - acoso
# - sexual_no_solicitado
# - phishing_textual

# 1. CONFIGURACIÓN
MENSAJES_POR_CATEGORIA = 100

dataset = {

    # Mensajes cotidianos que no presentan riesgos evidentes.
    "seguro": [

        "Hola, cómo estás",
        "Ya llegué a mi casa",
        "Nos vemos mañana",
        "Me puedes enviar el documento",
        "A qué hora comienza la reunión",
        "Ya terminé mi tarea",
        "Voy camino a la universidad",
        "Gracias por compartir la información",
        "Mañana tenemos clases",
        "Puedes revisar este archivo",
        "Te mando el horario",
        "Ya recibí tu correo",
        "Vamos a trabajar en el proyecto",
        "La reunión será por la tarde",
        "Necesito imprimir unos documentos",
        "El profesor dejó una actividad",
        "Nos vemos en la entrada",
        "Voy a preparar la presentación",
        "Puedes llamarme cuando tengas tiempo",
        "El archivo está guardado en la carpeta",
                "Buenos días, espero que tengas un excelente día",
        "¿Puedes ayudarme con esta actividad?",
        "Ya envié el reporte al profesor",
        "La clase de hoy comienza a las ocho",
        "Nos reuniremos en la biblioteca",
        "Te comparto las fotografías del evento",
        "Muchas gracias por tu apoyo",
        "El proyecto está quedando muy bien",
        "¿Me confirmas si recibiste el archivo?",
        "Hoy tenemos que entregar el trabajo",
        "Voy a revisar los pendientes de la semana",
        "Puedes encontrar la información en el documento",
        "La computadora necesita una actualización",
        "Estoy preparando el informe mensual",
        "El equipo ya está listo para trabajar",
        "Mañana visitaré a mis compañeros",
        "Te envío la ubicación de la reunión",
        "La presentación quedó guardada correctamente",
        "¿Cuál es la fecha de entrega?",
        "Voy a organizar mis actividades",
        "Mi familia llegará por la tarde",
        "Ya compré los materiales para la escuela",
        "El autobús llegará en diez minutos",
        "Hoy hace mucho frío",
        "¿Qué película quieres ver?",
        "Me gusta escuchar música mientras estudio",
        "Voy a preparar algo de comer",
        "El fin de semana iremos al parque",
        "Necesito descansar un poco",
        "Mi teléfono tiene poca batería",
        "¿Puedes pasarme la dirección del lugar?",
        "La tienda abre a las nueve",
        "El pedido llegó esta mañana",
        "Estoy aprendiendo a programar en Python",
        "El código funciona correctamente",
        "Ya corregí los errores del programa",
        "Voy a guardar una copia de seguridad",
        "La base de datos contiene los registros",
        "Necesito consultar el manual del sistema",
        "El servidor está funcionando correctamente",
        "La aplicación recibió una nueva actualización",
        "Puedes descargar el archivo desde la página oficial",
        "Mi contraseña es diferente para cada cuenta",
        "Activé la verificación en dos pasos",
        "Recibí un correo de confirmación de mi registro",
        "El banco me envió un comprobante de pago",
        "Voy a revisar mis movimientos bancarios",
        "No compartas tu contraseña con otras personas",
        "El enlace pertenece al sitio oficial de la universidad",
        "Recibí un mensaje de mi compañero de trabajo",
        "Necesito cambiar mi contraseña por seguridad",
        "El paquete llegará mañana según el seguimiento oficial",
        "La empresa confirmó la entrega de mi pedido",
        "Pagué mi servicio desde la aplicación oficial",
        "El recibo de pago llegó a mi correo",
        "Voy a contactar al soporte desde su página oficial",
        "Mi cuenta tiene activada la protección adicional",
        "El administrador publicó un aviso importante",
        "La reunión fue programada para el viernes",
        "El profesor compartió el material de estudio",
        "Hoy terminé de leer el libro",
        "Estoy trabajando en una nueva actividad",
        "¿Quieres que revisemos juntos el proyecto?",
        "El archivo contiene información de la empresa",
        "Ya guardé los cambios del documento",
        "La impresora necesita hojas nuevas",
        "El técnico revisará el equipo mañana",
        "La conexión a internet está estable",
        "Voy a reiniciar mi computadora",
        "El sistema generó un reporte correctamente",
        "La capacitación comienza la próxima semana",
        "El departamento recibió los documentos",
        "Puedes consultar el horario en el calendario",
        "Ya confirmé mi asistencia al evento",
        "Te deseo mucho éxito en tu examen",
        "Gracias por avisarme con anticipación",
        "Nos comunicamos después de la reunión",
        "Estoy de acuerdo con la propuesta",
        "Que tengas una excelente tarde",
        "El trabajo fue entregado correctamente"

    ],

    # Insultos y expresiones denigrantes.
    "ofensivo": [

        "Eres una persona insoportable",
        "No tienes idea de lo que haces",
        "Qué persona tan desagradable",
        "Eres un completo inútil",
        "Tu comportamiento es ridículo",
        "No sirves para hacer nada",
        "Eres una persona arrogante",
        "Qué comentario tan estúpido",
        "Siempre dices puras tonterías",
        "Eres bastante desagradable",
        "No soporto tu actitud",
        "Qué manera tan absurda de pensar",
        "Eres una persona despreciable",
        "Tu opinión no tiene sentido",
        "Deja de comportarte como un tonto",
        "Eres muy grosero con los demás",
        "Qué persona tan ignorante",
        "Tus comentarios son desagradables",
        "No sabes respetar a nadie",
        "Eres alguien bastante irrespetuoso",
        "Tu forma de hablar es muy desagradable",
        "Qué comentario tan ignorante",
        "No sabes hacer bien tu trabajo",
        "Eres demasiado presumido",
        "Tu actitud demuestra muy poca educación",
        "Siempre arruinas las cosas",
        "Qué persona tan molesta",
        "No tienes nada interesante que decir",
        "Eres bastante desagradable al tratar a otros",
        "Tu comportamiento deja mucho que desear",
        "No sabes escuchar a nadie",
        "Qué manera tan tonta de responder",
        "Eres una persona muy arrogante",
        "Tus palabras son completamente absurdas",
        "No tienes respeto por los demás",
        "Siempre haces comentarios fuera de lugar",
        "Eres demasiado insoportable",
        "Qué respuesta tan mediocre",
        "No sabes comportarte correctamente",
        "Tu actitud es realmente vergonzosa",
        "Eres muy egoísta con todos",
        "Qué persona tan desagradable eres",
        "No tienes educación para conversar",
        "Tus ideas son bastante ridículas",
        "Eres un mal compañero",
        "No sabes reconocer tus errores",
        "Tu presencia resulta bastante molesta",
        "Eres una persona muy desconsiderada",
        "Qué comentario tan fuera de lugar",
        "No sabes tratar bien a las personas",
        "Siempre buscas hacer sentir mal a los demás",
        "Tu forma de pensar es bastante absurda",
        "Eres demasiado irresponsable",
        "No tienes capacidad para entenderlo",
        "Qué actitud tan patética",
        "Tus argumentos no tienen sentido",
        "Eres una persona muy desagradable",
        "Deja de decir tantas tonterías",
        "No sabes hacer nada correctamente",
        "Tu comportamiento es una vergüenza",
        "Eres demasiado presumido para admitir errores",
        "Qué manera tan grosera de expresarte",
        "No tienes consideración por nadie",
        "Tu opinión resulta bastante ofensiva",
        "Eres alguien muy poco agradable",
        "No sabes mantener una conversación respetuosa",
        "Qué comentario tan desagradable acabas de hacer",
        "Tu actitud es bastante infantil",
        "Eres una persona muy maleducada",
        "Siempre tienes algo desagradable que decir",
        "No sabes valorar el esfuerzo de los demás",
        "Qué forma tan absurda de comportarte",
        "Eres demasiado negativo",
        "Tu manera de actuar es decepcionante",
        "No tienes la menor consideración",
        "Eres muy difícil de soportar",
        "Qué persona tan presumida",
        "Tus comentarios demuestran poca madurez",
        "No sabes aceptar una opinión diferente",
        "Eres bastante desagradable cuando hablas",
        "Tu comportamiento es completamente irrespetuoso",
        "Qué manera tan pésima de tratar a alguien",
        "Eres muy desconsiderado con tus compañeros",
        "No tienes argumentos para defender tus ideas",
        "Siempre haces quedar mal a los demás",
        "Tu actitud resulta bastante molesta",
        "Eres una persona poco confiable",
        "Qué respuesta tan grosera",
        "No sabes reconocer el trabajo de otros",
        "Tu manera de expresarte es muy ofensiva",
        "Eres demasiado cerrado de mente",
        "Qué comportamiento tan desagradable",
        "No tienes respeto por las opiniones ajenas",
        "Tus palabras demuestran mucha inmadurez",
        "Eres bastante egoísta y presumido",
        "No sabes convivir con otras personas",
        "Tu actitud es muy poco profesional",
        "Qué comentario tan innecesario",
        "Eres una persona muy irrespetuosa",
        "Tu no eres mejor que yo"

    ],

    # Amenazas y expresiones de hostilidad.
    "agresividad": [

        "Te voy a hacer daño",
        "Te arrepentirás de lo que hiciste",
        "Si te encuentro tendrás problemas",
        "Voy a golpearte cuando te vea",
        "No sabes de lo que soy capaz",
        "Te voy a destruir",
        "Más te vale tener cuidado conmigo",
        "Voy a buscarte para arreglar esto",
        "No vas a salirte con la tuya",
        "Te voy a hacer pagar por esto",
        "Si vuelves a hacerlo habrá consecuencias",
        "Te espero afuera para resolverlo",
        "Voy a lastimarte si no obedeces",
        "No me importa lo que pase contigo",
        "Te voy a perseguir hasta encontrarte",
        "Esto no se va a quedar así",
        "Te voy a dar una lección",
        "No vuelvas a cruzarte en mi camino",
        "Vas a tener problemas conmigo",
        "Te advierto que esto tendrá consecuencias",
        "Voy a golpearte si vuelves a acercarte",
        "Te voy a encontrar y tendrás que responder",
        "No sabes lo que te espera",
        "Si vuelves a molestarme te haré daño",
        "Voy a destruir todo lo que tienes",
        "Te haré pagar por haberme traicionado",
        "No me importa lastimarte",
        "Te voy a dar una paliza",
        "Si te vuelvo a ver tendrás problemas",
        "Voy a romperte la cara",
        "No vas a poder esconderte de mí",
        "Te haré sufrir por lo que hiciste",
        "Voy a buscarte para golpearte",
        "Si no haces lo que digo te arrepentirás",
        "Te voy a lastimar cuando menos lo esperes",
        "No tienes idea de lo que puedo hacerte",
        "Voy a acabar contigo",
        "Te voy a perseguir hasta hacerte daño",
        "Si vuelves a hablarme así te golpeo",
        "Te advierto que puedo hacerte mucho daño",
        "Voy a destrozar tus cosas",
        "No vas a salir ileso de esto",
        "Te voy a cobrar cada una de tus acciones",
        "Si te acercas otra vez te voy a golpear",
        "Voy a hacer que te arrepientas de conocerme",
        "No me provoques porque perderé el control",
        "Te voy a atacar si vuelves a hacerlo",
        "Vas a pagar por haberme enfrentado",
        "No voy a tener piedad contigo",
        "Te voy a romper todo lo que tengas",
        "Voy a ir por ti y no podrás escapar",
        "Si no te callas te voy a golpear",
        "Te haré daño para que aprendas",
        "No volverás a meterte conmigo",
        "Voy a hacerte la vida imposible",
        "Te voy a golpear delante de todos",
        "No me importa si terminas lastimado",
        "Te voy a hacer pagar por desafiarme",
        "Si te encuentro te vas a arrepentir",
        "Voy a destruirte si vuelves a traicionarme",
        "Te voy a atacar cuando estés solo",
        "No vas a olvidar lo que te voy a hacer",
        "Voy a romper todo si no me obedeces",
        "Te voy a lastimar por meterte conmigo",
        "Si vuelves a acercarte te irá muy mal",
        "Te voy a hacer daño para que tengas miedo",
        "No me importa enfrentarme contigo a golpes",
        "Voy a golpearte hasta que dejes de molestar",
        "Te voy a buscar para ajustar cuentas",
        "Si no obedeces tendrás que enfrentarme",
        "Voy a hacer que lamentes haberme conocido",
        "No te salvarás cuando te encuentre",
        "Te voy a causar problemas por lo que hiciste",
        "Si vuelves a insultarme te golpeo",
        "Voy a romper tus pertenencias",
        "Te voy a hacer pagar con la misma moneda",
        "No vas a poder detenerme cuando me enoje",
        "Voy a enfrentarte y no será una conversación",
        "Te voy a lastimar si sigues desafiándome",
        "No me importa lo que te pase después",
        "Voy a hacerte daño por haberme engañado",
        "Te voy a golpear si no te apartas",
        "Vas a arrepentirte de haberme provocado",
        "Voy a buscarte para resolver esto por la fuerza",
        "No voy a detenerme hasta que recibas tu castigo",
        "Te voy a hacer pagar por humillarme",
        "Si vuelves a tocar mis cosas tendrás problemas",
        "Voy a destrozar lo que tanto te importa",
        "Te voy a atacar si vuelves a desafiarme",
        "No tendrás tranquilidad después de lo que hiciste",
        "Voy a golpearte si no dejas de provocarme",
        "Te haré daño aunque intentes evitarme",
        "Voy a ir a buscarte para pelear",
        "Si no me das lo que quiero habrá violencia",
        "Te voy a hacer pagar por desobedecerme",
        "Voy a destruir tus cosas si me vuelves a fallar",
        "No me detendré si intentas enfrentarte conmigo",
        "Te voy a lastimar por hacerme enojar",
        "Voy a resolver esto a golpes contigo",
        "Te voy a hacer daño mentalmente "

    ],

    # Hostigamiento, intimidación y presión.
    "acoso": [
 
        "Te escribo todos los días aunque no quieras",
        "No voy a dejar de buscarte",
        "Sé dónde estudias y dónde trabajas",
        "Contéstame aunque me hayas bloqueado",
        "No aceptaré que quieras alejarte",
        "Voy a seguir contactándote",
        "No tienes derecho a ignorarme",
        "Siempre estaré vigilando lo que haces",
        "Te buscaré por todas tus redes",
        "No dejaré de insistir hasta que respondas",
        "Aunque me bloquees encontraré otra forma",
        "Quiero saber dónde estás en todo momento",
        "No puedes hablar con otras personas",
        "Voy a revisar con quién te relacionas",
        "No aceptaré que termines esta relación",
        "Te seguiré escribiendo hasta que me hagas caso",
        "Sé quiénes son tus amigos",
        "No puedes evitar que te contacte",
        "Voy a aparecer donde estés",
        "Tienes que responderme cuando yo quiera",
                "No dejaré de escribirte aunque me ignores",
        "Te llamaré desde otros números si me bloqueas",
        "Voy a seguir buscándote hasta que aceptes hablar",
        "Quiero saber con quién estás y a dónde vas",
        "No puedes salir sin decirme dónde estarás",
        "Te enviaré mensajes hasta que me respondas",
        "Voy a revisar todas tus publicaciones para saber qué haces",
        "No aceptaré que me bloquees de ninguna red social",
        "Te encontraré aunque cambies de número",
        "Voy a presentarme en tu casa si no contestas",
        "No tienes permiso para ignorar mis mensajes",
        "Quiero que me informes cada vez que salgas",
        "Voy a seguirte para saber con quién te reúnes",
        "No dejaré que te alejes de mí",
        "Te escribiré desde otra cuenta si me bloqueas",
        "Voy a buscar a tus amigos para saber dónde estás",
        "No puedes esconderte de mí para siempre",
        "Te contactaré por todos los medios posibles",
        "Necesito saber dónde estás durante todo el día",
        "No voy a respetar que quieras dejar de hablarme",
        "Voy a insistir hasta que aceptes verme",
        "Si no contestas iré a buscarte personalmente",
        "No dejaré de llamarte hasta que respondas",
        "Voy a revisar tus horarios para encontrarte",
        "Quiero saber quiénes son todas las personas con las que hablas",
        "No puedes evitar que esté pendiente de ti",
        "Te buscaré incluso si cambias de escuela",
        "Voy a escribirle a tus conocidos para encontrarte",
        "No aceptaré que quieras terminar el contacto",
        "Voy a seguir apareciendo donde estés",
        "Te mandaré mensajes todos los días aunque no quieras",
        "No dejaré de preguntarte dónde estás",
        "Voy a vigilar tus redes sociales constantemente",
        "Quiero que me mandes tu ubicación cada hora",
        "No puedes salir con otras personas sin avisarme",
        "Voy a buscarte en tu trabajo si no respondes",
        "Te llamaré repetidamente hasta que contestes",
        "No respetaré que me hayas pedido espacio",
        "Voy a crear otra cuenta para seguir contactándote",
        "Siempre sabré dónde encontrarte",
        "No dejaré de preguntarte con quién estás",
        "Voy a seguir enviándote solicitudes aunque las rechaces",
        "Quiero revisar todos tus movimientos",
        "No tienes derecho a desaparecer sin avisarme",
        "Voy a buscarte en los lugares que frecuentas",
        "Te seguiré contactando aunque me digas que no",
        "No voy a aceptar que me ignores",
        "Voy a preguntar a tus compañeros dónde te encuentras",
        "Te escribiré cada vez que te vea conectado",
        "Quiero que me expliques por qué hablas con otras personas",
        "No dejaré de buscar una forma de comunicarme contigo",
        "Voy a estar pendiente de cada cosa que publiques",
        "Te enviaré mensajes desde diferentes perfiles",
        "No puedes impedir que quiera saber de ti",
        "Voy a aparecer en los lugares que visitas",
        "Necesito que respondas todos mis mensajes",
        "Voy a insistir aunque me hayas pedido que pare",
        "No dejaré de llamarte durante el día",
        "Quiero saber por qué no contestas inmediatamente",
        "Voy a seguirte en todas tus cuentas nuevas",
        "No aceptaré que me elimines de tus contactos",
        "Te buscaré cada vez que intentes alejarte",
        "Voy a preguntarle a tu familia dónde estás",
        "No dejaré de enviarte solicitudes de amistad",
        "Quiero controlar con quién te relacionas",
        "Voy a escribirte hasta que me prestes atención",
        "No respetaré tu decisión de no verme",
        "Te buscaré en tu universidad si no respondes",
        "Voy a estar pendiente de tus horarios de salida",
        "No dejaré de contactarte aunque me lo pidas",
        "Voy a utilizar otras cuentas para encontrarte",
        "Quiero que me digas dónde estás en todo momento",
        "Voy a revisar quién comenta tus fotografías",
        "No puedes impedir que siga buscándote",
        "Te enviaré mensajes incluso durante la madrugada",
        "Voy a buscarte cada vez que cambies de ubicación",
        "No dejaré de insistir hasta conseguir tu atención",
        "Quiero saber con quién pasas cada momento",
        "Voy a seguir intentando comunicarme aunque me bloquees",
        "ye voy segir en la calle "

    ],

    # Contenido sexual no solicitado.
    # Los ejemplos se mantienen sin descripciones explícitas.
    "sexual_no_solicitado": [

    # 20 ejemplos originales
    "Envíame fotografías íntimas aunque no quieras",
    "Mándame imágenes de tu cuerpo",
    "Quiero que me envíes fotos sexuales",
    "No acepto que te niegues a mandarme fotografías",
    "Envíame contenido íntimo por privado",
    "Quiero recibir fotografías tuyas sin ropa",
    "Mándame imágenes íntimas ahora mismo",
    "Deberías enviarme fotografías provocativas",
    "No seas tímida y mándame contenido sexual",
    "Insisto en que me mandes fotos íntimas",
    "Quiero que compartas imágenes privadas conmigo",
    "Envíame fotografías íntimas para demostrarme que confías",
    "No voy a dejar de pedirte imágenes sexuales",
    "Mándame fotografías privadas aunque te dé vergüenza",
    "Quiero recibir contenido íntimo sin que nadie se entere",
    "Comparte imágenes de carácter sexual conmigo",
    "Te estoy pidiendo fotografías íntimas y debes enviarlas",
    "No acepto un no como respuesta cuando pido fotos",
    "Envíame imágenes sexuales por este chat",
    "Quiero fotografías íntimas tuyas sin importar tu decisión",

    # Solicitudes directas y lenguaje coloquial
    "Mándame fotos de tus tetas",
    "Pásame una foto de tus pechos",
    "Quiero ver tus senos",
    "Mándame una foto sin ropa",
    "¿Me mandas una foto en ropa interior?",
    "Envíame una foto de tu cuerpo desnudo",
    "Mándame unas fotitos íntimas",
    "Pásame fotos de tu trasero",
    "Quiero ver cómo te ves sin ropa",
    "Mándame una foto más atrevida",
    "¿Tienes fotos íntimas?",
    "Mándame una foto de tus partes íntimas",
    "Quiero ver tus pechos por cámara",
    "Pásame una foto provocativa",
    "Envíame una foto íntima por WhatsApp",
    "Mándame una foto de tu cuerpo completo sin ropa",
    "¿Me enseñas tus senos?",
    "Quiero que me mandes fotos privadas",
    "Mándame una foto en tanga",
    "Pásame una foto de tus nalgas",

    # Propuestas sexuales no solicitadas
    "¿Quieres coger conmigo?",
    "¿Quieres tener sexo conmigo?",
    "Quiero acostarme contigo",
    "¿Te gustaría hacerlo conmigo?",
    "Vamos a tener relaciones sexuales",
    "Quiero que tengamos sexo esta noche",
    "¿Te gustaría hacerlo en la cama?",
    "Tengo ganas de acostarme contigo",
    "Quiero hacer cosas sexuales contigo",
    "¿Quieres que hagamos algo íntimo?",
    "Me gustaría tener sexo contigo",
    "Quiero que vengas para hacerlo",
    "¿Te animas a tener relaciones conmigo?",
    "Quiero pasar una noche contigo en la cama",
    "¿Quieres hacer el amor conmigo?",

    # Insinuaciones y presión sexual
    "No seas aburrida y mándame una foto íntima",
    "Ándale, mándame una foto sin ropa",
    "No te cuesta nada enseñarme tus pechos",
    "Si me quieres, mándame una foto íntima",
    "Demuestra que confías en mí enviándome fotos",
    "No seas tímida, enséñame tu cuerpo",
    "Ya te pedí una foto íntima, mándamela",
    "No me digas que no, solo quiero verte",
    "Si no me mandas fotos es porque no me quieres",
    "Prometo que nadie verá las fotos que me mandes",
    "Mándame algo más atrevido, no seas así",
    "Quiero que me enseñes más de tu cuerpo",
    "No voy a dejar de pedirte fotos íntimas",
    "Aunque no quieras, quiero que me mandes una foto",
    "Te estoy diciendo que me mandes una foto desnuda",

    # Mensajes sexuales insistentes y no deseados
    "Deja de hacerte del rogar y mándame fotos",
    "Ya sé que no quieres, pero mándame una foto",
    "No importa que me hayas dicho que no",
    "Quiero que me mandes fotos íntimas ahora",
    "Te voy a seguir pidiendo fotos hasta que aceptes",
    "Mándame tus fotos privadas y no le digas a nadie",
    "No me importa si te incomoda, quiero ver tu cuerpo",
    "Quiero que me envíes contenido sexual por privado",
    "Deja de negarte y enséñame tus pechos",
    "No tienes por qué negarte a mandarme fotos íntimas",
            "Mándame una foto de tus pechos, quiero verte",
        "¿Me enseñas tus tetas por videollamada?",
        "Quiero que me mandes una foto desnuda",
        "Pásame fotos íntimas, no seas tímida",
        "¿Cuándo me vas a mandar esas fotos sin ropa?",
        "Mándame una foto de tu escote y de tu cuerpo",
        "Quiero verte en ropa interior",
        "Envíame una foto íntima aunque sea una sola vez",
        "¿Por qué no quieres enseñarme tu cuerpo?",
        "Mándame una foto íntima por mensaje privado",
        "Quiero que hagamos cosas sexuales aunque no quieras",
        "Deja de decir que no y acepta tener sexo conmigo",
        "Mándame fotos íntimas para que pueda complacerte",
        "Quiero que me enseñes tu cuerpo por cámara",
        "Pásame una foto de tus senos ahora mismo",
        "No me importa que te dé pena, quiero ver tus fotos",
        "Te prometo que no compartiré las fotografías íntimas",
        "Mándame contenido sexual aunque ya te dije que lo quiero",
        "Quiero que hagas algo sexual conmigo por videollamada",
        "Insisto en que me envíes fotografías íntimas"

],

    # Mensajes que intentan engañar para obtener información.
    "phishing_textual": [

        "Tu cuenta será suspendida, confirma tu contraseña ahora",
        "Ganaste un premio, ingresa tus datos para reclamarlo",
        "Tu banco necesita verificar tu contraseña mediante este enlace",
        "Comparte el código de seguridad que recibiste",
        "Tu cuenta será bloqueada si no verificas tus datos",
        "Actualiza tus datos bancarios en el siguiente enlace",
        "Hemos detectado actividad sospechosa, confirma tu identidad",
        "Tu paquete está retenido, ingresa tus datos personales",
        "Para recibir tu premio necesitamos tu número de tarjeta",
        "Tu contraseña venció, inicia sesión para renovarla",
        "Comparte el código que llegó a tu teléfono para activar tu cuenta",
        "Tu cuenta tiene un problema, verifica tus datos inmediatamente",
        "Evita el bloqueo ingresando tu contraseña en este formulario",
        "Tu banco solicita el número de tarjeta y el código de seguridad",
        "Recibiste una transferencia, confirma tus datos para liberarla",
        "Tu cuenta será eliminada si no verificas tu identidad",
        "Ingresa tu usuario y contraseña para recibir el reembolso",
        "Para recuperar tu cuenta comparte el código de verificación",
        "Tu premio está listo, proporciona tus datos personales",
        "Detectamos un problema, ingresa tus credenciales para solucionarlo",

        "Tu cuenta bancaria presenta un problema, verifica tu identidad",
        "Se detectó un acceso desconocido, comparte tu código de seguridad",
        "Tu tarjeta será suspendida si no actualizas tus datos",
        "Confirma tu contraseña para evitar el cierre de tu cuenta",
        "Tenemos un reembolso pendiente, ingresa tus datos bancarios",
        "Tu cuenta necesita una actualización urgente de seguridad",
        "Comparte el código SMS para validar tu operación bancaria",
        "Tu sesión ha expirado, vuelve a ingresar tus credenciales",
        "Recibiste un mensaje de seguridad, confirma tu número de tarjeta",
        "Tu cuenta será bloqueada por falta de verificación",
        "Para liberar tu transferencia necesitamos tu contraseña",
        "Ingresa tus datos personales para confirmar tu identidad",
        "Tu banco detectó movimientos irregulares, verifica tu cuenta",
        "Comparte el código de acceso para cancelar la operación",
        "Tu cuenta tiene un cargo pendiente, valida tus datos",
        "Actualiza tu información bancaria para evitar restricciones",
        "Se requiere tu contraseña para confirmar el reembolso",
        "Tu cuenta fue seleccionada para una revisión, proporciona tus datos",
        "Confirma el código recibido para recuperar tu acceso",
        "Tu tarjeta necesita una validación inmediata",

        "Tu paquete no pudo ser entregado, confirma tu dirección",
        "Tenemos un envío retenido, proporciona tus datos personales",
        "Tu pedido está pendiente de pago, ingresa los datos de tu tarjeta",
        "Confirma tu número telefónico para recibir tu paquete",
        "Tu envío será devuelto si no verificas tu información",
        "Se requiere un pago adicional para liberar tu paquete",
        "Actualiza tu dirección de entrega mediante este formulario",
        "Tu paquete está detenido, proporciona tu identificación",
        "Confirma tus datos para continuar con la entrega",
        "Tu envío necesita una validación de identidad",

        "Ganaste un premio especial, proporciona tu número de tarjeta",
        "Fuiste seleccionado para recibir dinero, confirma tus datos",
        "Reclama tu recompensa ingresando tu contraseña",
        "Tu premio está por vencer, comparte tu código de acceso",
        "Has ganado un teléfono, necesitamos tus datos bancarios",
        "Recibirás un regalo si completas este registro",
        "Tu recompensa está disponible, ingresa tus credenciales",
        "Para recibir el premio debes pagar una cuota de liberación",
        "Felicidades, comparte tu código de verificación para cobrar",
        "Tu bono será cancelado si no registras tus datos",

        "Tu cuenta de correo será eliminada, confirma tu contraseña",
        "Detectamos un inicio de sesión sospechoso, comparte tu código",
        "Tu buzón está lleno, ingresa tus credenciales para ampliarlo",
        "Tu contraseña será desactivada si no verificas tu identidad",
        "Se bloqueará tu correo si no actualizas tus datos",
        "Confirma tu cuenta para evitar perder todos tus mensajes",
        "Comparte tu código de recuperación para restaurar el acceso",
        "Tu correo requiere una validación de seguridad urgente",
        "Ingresa tu contraseña para desbloquear tu bandeja de entrada",
        "Tu cuenta presenta actividad irregular, verifica tus credenciales",

        "Tu cuenta de redes sociales será suspendida, confirma tus datos",
        "Alguien reportó tu perfil, ingresa tus credenciales para recuperarlo",
        "Tu perfil necesita una verificación, comparte el código recibido",
        "Confirma tu contraseña para conservar tu cuenta",
        "Tu cuenta fue seleccionada para una revisión de seguridad",
        "Se detectó una infracción, ingresa tus datos para evitar el bloqueo",
        "Comparte tu código de acceso para verificar tu perfil",
        "Tu cuenta será deshabilitada si no confirmas tu identidad",
        "Necesitamos tu contraseña para restaurar tu perfil",
        "Tu sesión presenta un error, vuelve a ingresar tus datos",

        "Un familiar necesita dinero urgentemente, realiza una transferencia",
        "Soy del soporte técnico, necesito tu contraseña para ayudarte",
        "Comparte el código que recibiste para confirmar que eres tú",
        "Para solucionar el problema necesito acceso a tu cuenta",
        "Envía una fotografía de tu tarjeta bancaria por ambos lados",
        "Proporciona el número de tu tarjeta y su código de seguridad",
        "Necesito tu contraseña para completar el trámite",
        "Transfiere el dinero para desbloquear tu supuesto premio",
        "Ingresa tus datos en este formulario para recibir el reembolso",
        "Comparte tu código de autenticación para cancelar el cargo",

        "Tu cuenta tiene una deuda pendiente, paga mediante este enlace",
        "Evita una multa proporcionando tus datos personales",
        "Tu servicio será cancelado si no verificas tu información",
        "Se requiere un pago inmediato para mantener activo tu servicio",
        "Tu suscripción presenta un error, ingresa tus datos bancarios",
        "Confirma tu identidad para recibir una supuesta devolución",
        "Tu cuenta necesita una renovación, proporciona tus credenciales",
        "Se detectó un problema con tu pago, comparte los datos de tu tarjeta",
        "Tu acceso será restringido si no completas esta verificación",
        "Para evitar el bloqueo necesitamos tu código de autenticación"


    ]
}


# 2. VALIDAR CANTIDAD DE MENSAJES

print("\nEMOTION GUARD AI")
print("Generador de Dataset de Seguridad")

print("\nCategorías:", list(dataset.keys()))

for categoria, mensajes in dataset.items():

    print(f"Mensajes de {categoria}: {len(mensajes)}")

    if len(mensajes) != MENSAJES_POR_CATEGORIA:

        raise ValueError(
            f"La categoría {categoria} debe tener "
            f"{MENSAJES_POR_CATEGORIA} mensajes."
        )


# 3. CONVERTIR LOS MENSAJES EN REGISTROS

registros = []

for categoria, mensajes in dataset.items():

    for mensaje in mensajes:

        registros.append({
            "mensaje": mensaje,
            "categoria": categoria
        })


# 4. CREAR DATAFRAME

df = pd.DataFrame(registros)


# 5. VALIDAR DATASET

print("\n========== VALIDANDO DATASET ==========")

# Comprobar mensajes vacíos.
vacios = df["mensaje"].isna().sum()

print("Mensajes vacíos:", vacios)

if vacios > 0:
    raise ValueError("Existen mensajes vacíos.")


# Comprobar mensajes duplicados.
duplicados = df["mensaje"].str.strip().str.lower().duplicated().sum()

print("Mensajes duplicados:", duplicados)

if duplicados > 0:
    raise ValueError("Existen mensajes duplicados.")


# Comprobar que todas las categorías tengan la cantidad esperada.
distribucion = df["categoria"].value_counts()

for categoria in dataset:

    if distribucion[categoria] != MENSAJES_POR_CATEGORIA:

        raise ValueError(
            f"Distribución incorrecta en {categoria}."
        )


print("Validación completada correctamente.")


# 6. MEZCLAR LOS REGISTROS

df = df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)


# 7. CREAR CARPETA Y GUARDAR CSV

carpeta_datasets = Path(__file__).resolve().parent / "datasets"

carpeta_datasets.mkdir(exist_ok=True)

ruta = carpeta_datasets / "dataset_seguridad.csv"

df.to_csv(
    ruta,
    index=False,
    encoding="utf-8-sig"
)


# 8. MOSTRAR RESULTADOS

print("\n========== DATASET GENERADO ==========")

print("Archivo:", ruta)

print("\nDistribución de categorías:")
print(df["categoria"].value_counts())

print("\nPrimeros 10 registros:")
print(df.head(10).to_string(index=False))

print("\n¡DATASET DE SEGURIDAD GENERADO CORRECTAMENTE!")
