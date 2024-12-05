# Este código sirve para instalar Streamlit en tu computadora y hacer un primer programa en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.

# Primero, debes abrir el folder donde se encuentra tu archivo de Python en la terminal de tu computadora.
# Para hacerlo, debes escribir el siguiente comando en la terminal de tu computadora
# cd ruta_de_tu_carpeta
# o desde Visual Studio Code, seleccionas Open Folder y seleccionas la carpeta 
# donde se encuentra tu archivo de Python

# Segundo, debes instalar un entorno virtual en tu computadora.
# python -m venv .venv
# Este comando crea un entorno virtual en la carpeta actual con el nombre .venv.

# Para activar el entorno virtual, debes escribir el siguiente comando en la terminal de tu computadora
# .venv\Scripts\activate
# Para desactivar el entorno virtual, debes escribir el siguiente comando en la terminal de tu computadora
# deactivate

# Tercero, debes instalar Streamlit en tu entorno virtual.
# pip install Streamlit 

# Cuarto, puedes abrir el tutorial de Streamlit en tu navegador.
# streamlit hello o python -m streamlit hello

# Quinto, debes abrir el archivo de Python en la terminal de tu computadora.
# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
#  streamlit run your_script.py o python -m streamlit run your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Creamos una barra lateral
sidebar = st.sidebar

# Si usas el siguiente código mostrará un título en la aplicación Streamlit. 
# st.title("Nombre de tu blog"): Esta línea está creando un título en la aplicación web.
# Pero, a diferencia de st.markdown, el texto estará alineado a la izquierda y no podrás cambiar el color del texto.

# La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
st.markdown("<h1 style='text-align: center;'>Blog semestre 2024 - II</h1>", unsafe_allow_html=True)

# <h1 style='text-align: center;'>Nombre de tu blog</h1>: Esto es una cadena de código HTML. 
# La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
# el atributo style se utiliza para agregar estilos CSS. 
# En este caso, el texto está alineado al centro (text-align: center;). 
# El texto dentro de las etiquetas <h1> ("Aquí escribe un nombre creativo para tu blog") es el contenido del encabezado.

# unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad. 
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

# Creamos dos columnas separadas para la imagen y el texto
col1, col2 = st.columns(2)

# col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
# La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
# Las columnas creadas se asignan a las variables col1 y col2.

# En la primera columna colocamos la imagen
col1.image("notas_campo.jpg", caption='cuaderno de campo', width=300)

# col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
# La función image toma como primer argumento la ruta de la imagen que se va a mostrar. 
# En este caso, la imagen es "ellie.png". 
# El argumento caption se utiliza para proporcionar un pie de foto a la imagen, en este caso 'Ellie'. 
# El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

# En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
# Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
# ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?

texto = """
Soy Luisa Gomez, soy egresada de Lingüística de la PUCP. Actualmente, estoy en mi cuarto ciclo de la maestría en Lingüística. Mis intereses están ligados a la lingüística computacional, lamentablemente esta área no es una especialidad en Latinoamérica. Por tal motivo, luego de terminar la maestría mi objetivo es postular a un doctorado en esa especialidad. Mi tesis de maestría está orientado en generar un modelo que clasifique lenguas por familias lingüísticas en base a rasgos registrados en una base de datos abierta llamada Grambank. Asimismo, con ese clasificador buscaré responder qué sucede con las lenguas aisladas que en la literatura se menciona que son peculiares al no compartir rasgos con lenguas que sí conforman una familia lingüística. Este semestre me han visto en sus clases de teoría debido a que estuve realizando trabajo de campo para el curso de Etnografía para Lingüístas y estoy analizando el uso del lenguaje en las prácticas pedagógicas de los docentes del curso de Pensamiento Computacional.
"""

# Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
# Mostramos el texto
col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

# <div style='text-align: justify; font-size: 15px;'>{texto}</div>: Esta es una cadena de código HTML. 
# La etiqueta <div> se utiliza para agrupar contenido en HTML. 
# En este caso, el texto está justificado (text-align: justify;). 
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto.

# f"": Esta es una cadena de formato en Python. 
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena. 
# En este caso, {texto} se reemplaza por el valor de la variable texto.

# Debajo de las columnas colocamos un subtítulo que describa tu experiencia aprendiendo a programar
# Deben presentar tu experiencia aprendiendo a programar: ¿Cómo te sentiste al principio?, 
# ¿Qué te ha enseñado la programación?, ¿Qué te gusta de programar?, 
# ¿Qué te gustaría hacer con la programación en el futuro? 

# Agregamos un subtítulo
st.markdown("<h2 style='text-align: center;'>Un mensaje para ustedes 💻</h2>", unsafe_allow_html=True)

# <h2 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h2>: Esta es una cadena de código HTML.
# La etiqueta <h2> se utiliza para el encabezado secundario de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h2> ("Mi experiencia aprendiendo a programar 💻") es el contenido del encabezado
# unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad.
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
# Puedes agregar emojis en el texto de Markdown utilizando códigos de emoji.

# Agregar un  texto para la respuesta
texto_2 = """
Ha sido muy grato ser su jefa de prácticas este semestre. Fueron un grupo muy diverso y al igual que yo dicté las clases también aprendí de ustedes resolviendo sus dudas e indagando sobre sus intereses. El mejor consejo que les puedo brindar es siempre no quedarse con las dudas y organizar sus tiempos para evitar procrastinar. Si no pueden cumplir los plazos pues escriban un correo y si tienen dudas o faltaron pueden escribir un correo y pedir asesorías. Estoy segura que sus profesores con gusto podrán ayudarlos. Finalmente, recuerden que siempre van a depender de ustedes mismos para ser resilentes ante cualquier circunstancia académica adversa.
"""

# Mostramos el texto
st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_2}</div>", unsafe_allow_html=True)

# <div style='text-align: justify; font-size: 15px;'>{texto_2}</div>: Esta es una cadena de código HTML.
# La etiqueta <div> se utiliza para agrupar contenido en HTML.
# En este caso, el texto está justificado (text-align: justify;).
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto_2.
# f"": Esta es una cadena de formato en Python.
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena.
# En este caso, {texto_2} se reemplaza por el valor de la variable texto_2.

# Ahora agregamos un video a mi blog donde explico algún tema de las clases
# Agregamos un subtítulo
st.markdown("<h2 style='text-align: center;'>A continuación una pequeña despedida ... </h2>", unsafe_allow_html=True)
# <h2 style='text-align: center;'>Explicación de un tema de las clases 📚</h2>: Esta es una cadena de código HTML
# La etiqueta <h2> se utiliza para el encabezado secundario de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h2> ("A continuación una pequeña despedida ... ") es el contenido del encabezado
# unsafe_allow_html=True: Este es un argumento opcional en la función markdown.

# Agregamos un video a la aplicación web ( menor a 20 MB)
st.video("pc4-video.mp4")
# st.video("ppc-2024-1.mp4"): Esta línea está agregando un video a la aplicación web.

# Agregamos un subtítulo
st.subheader("🔎 Buscador de blog PC4")

# <h2 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h2>: Esta es una cadena de código HTML.
# La etiqueta <h2> se utiliza para el encabezado secundario de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h2> ("Mi experiencia aprendiendo a programar 💻") es el contenido del encabezado
# unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad.
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
# Puedes agregar emojis en el texto de Markdown utilizando códigos de emoji.


codigo = st.text_input("Escribe tu código")
if codigo:
    if codigo == '20172352':
        st.markdown("<a href='https://pc4-yasmin.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20186119':
        st.markdown("<a href='https://no-blog.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20193461':
        st.markdown("<a href='https://miexperienciaaprendiendopython.streamlit.app' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20196410':
        st.markdown("<a href='https://experiencia-programando2024.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20200404':
        st.markdown("<a href='https://pc4-tino.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20210758':
        st.markdown("<a href='https://gatherstep.streamlit.app' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20211379':
        st.markdown("<a href='https://blog-chiroque.streamlit.app' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20211487':
        st.markdown("<a href='https://pc04yadhieligonzalespalma.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20211490':
        st.markdown("<a href='https://dramaversion.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20211496':
        st.markdown("<a href='https://pc4cespedes-eduardo-mb6khn4ykxfhljud4zqn84.streamlit.app' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20216387':
        st.markdown("<a href='https://pc4abi.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20216479':
        st.markdown("<a href='https://pc4-danis.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20216565':
        st.markdown("<a href='https://pc4-sandradelcarpiosilvera-tc2dphaka2xzgm9tsphzqd.streamlit.app' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20216608':
        st.markdown("<a href='https://pc4angelm.streamlit.app' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20220526':
        st.markdown("<a href='https://pc4siguas.streamlit.app' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20221056':
        st.markdown("<a href='https://pensamiento.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20221145':
        st.markdown("<a href='https://pc4-elena.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20221324':
        st.markdown("<a href='https://kasenliuli.streamlit.app' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20221602':
        st.markdown("<a href='https://mi-blog-pc4.streamlit.app' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20221972':
        st.markdown("<a href='https://magusyblog2020.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20225131':
        st.markdown("<a href='https://crisblog.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20225966':
        st.markdown("<a href='https://pc4-rodrigoalegree.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20226680':
        st.markdown("<a href='https://biografia-pablo-sandoval.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20230464':
        st.markdown("<a href='https://pc4--blog-final-2024-02.streamlit.app' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    else:
        st.write("Código incorrecto")



# Agregamos un subtítulo en la barra lateral
sidebar.markdown("<h1 style='text-align: center;'>Repositorio del curso, páginas de las librerías y programas importantes</h1>", unsafe_allow_html=True)


repositorio = f'<a href="https://github.com/4591526/1CCO19-2024/tree/main/2024-II" target="_blank"><button>Repositorio del curso</button></a>'
libreria1 = f'<a href="https://matplotlib.org/stable/gallery/index.html" target="_blank"><button>Matplotlib</button></a>'
libreria2 = f'<a href="https://geopandas.org/en/stable/gallery/index.html" target="_blank"><button>Geopandas</button></a>'
libreria3 = f'<a href="https://python-visualization.github.io/folium/latest/getting_started.html" target="_blank"><button>Folium</button></a>'
libreria4 = f'<a href="https://seaborn.pydata.org/examples/index.html" target="_blank"><button>Seaborn</button></a>'
libreria5 = f'<a href="https://plotly.com/python/plotly-express/" target="_blank"><button>Plotly Express</button></a>'
libreria6 = f'<a href="https://streamlit.io" target="_blank"><button>Streamlit</button></a>'
libreria2 = f'<a href="https://geopandas.org/en/stable/gallery/index.html" target="_blank"><button>Geopandas</button></a>'
programa = f'<a href="https://code.visualstudio.com" target="_blank"><button>Visual Studio Code</button></a>'

with st.sidebar:
    st.markdown(repositorio, unsafe_allow_html=True)
    st.markdown(libreria1,  unsafe_allow_html=True)
    st.markdown(libreria2,  unsafe_allow_html=True)
    st.markdown(libreria3,  unsafe_allow_html=True)
    st.markdown(libreria4,  unsafe_allow_html=True)
    st.markdown(libreria5,  unsafe_allow_html=True)
    st.markdown(libreria6,  unsafe_allow_html=True)
    st.markdown(libreria2,  unsafe_allow_html=True)
    st.markdown(programa,  unsafe_allow_html=True)

