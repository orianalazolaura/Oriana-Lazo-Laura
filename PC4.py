# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta 
# o abrimos el folder desde visual Studio Code 


# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.
# python -m venv .venv
# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.

# Luego activamos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# deactivate
# En MacOS/Linux:
# source .venv/bin/activate

# Acontinuación instalamos Streamlit 
# pip install Streamlit

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu computadora, no en Jupyter Notebook.
# python -m streamlit hello

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
# python -m streamlit run PC4.py
#  your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Generamos 3 páginas en la aplicación web de Streamlit.
# Generamos una página principal, otra donde contaran su experiencia aprendiendo a programar y una tercera donde presentarán sus gráficos.

# Creamos la lista de páginas
paginas = ['Inicio', 'Experiencia', 'Gráficos']

# Creamos botones de navegación tomando la lista de páginas
pagina_seleccionada = st.sidebar.selectbox('Selecciona la sección que deseas ver', paginas)

# Generamos condicionales para mostrar el contenido de cada página
if pagina_seleccionada == 'Inicio':

    # La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
    st.markdown("<h1 style='text-align: center;'>Yo y mi mundo</h1>", unsafe_allow_html=True)

    # <h1 style='text-align: center;'>Nombre de tu blog</h1>: Esto es una cadena de código HTML. 
    # La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
    # el atributo style se utiliza para agregar estilos CSS. 
    # En este caso, el texto está alineado al centro (text-align: center;). 
    # Pueden agregar emojis en el texto de Markdown utilizando códigos de emoji, por ejemplo:
    # <h1 style='text-align: center;'>Aquí escribe un nombre creativo para tu blog 📝</h1>
    # También pueden personalizar el color del texto utilizando el atributo style, por ejemplo:
    # <h1 style='text-align: center; color: blue;'>Nombre de tu blog</h1>
    # El texto dentro de las etiquetas <h1> ("Aquí escribe un nombre creativo para tu blog") es el contenido del encabezado.

    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

    # Creamos dos columnas separadas para la imagen y el texto
    col1, col2 = st.columns(2)

    # col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
    # La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
    # Las columnas creadas se asignan a las variables col1 y col2.

    # En la primera columna colocamos la imagen de perfil
    col1.image("Oriana .jpg", caption='Foto personal', width=300)

    # col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
    # La función image toma como primer argumento el nombre del archivo de la imagen que se desea mostrar. 
    # En este caso, la imagen es "ellie.png". 
    # El argumento caption se utiliza para proporcionar una etiqueta a la imagen, 
    # en este caso "Aquí puedes escribir una etiqueta debajo de la imagen". 
    # El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

    # En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
    # Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
    # ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?

    texto = """
    Oriana Camila Lazo Laura
    Arequipa 
    Comunicación Audiovisual
    Me gusta cómo se puede fusionar la creatividad personal junto a la tecnología y, paralelamente, la creación de narrativas. Además, me atrae que se empleen herramientas como de audio, diseño y video a fin de exponer mis ideas en medios digitales.
    Me gustaría convertirme en una productora audiovisual, porque siento que poseo la capacidad y responsabilidad de ejecutar futuros proyectos, evidentemente, dentro de un presupuesto y tiempo determinado. Además, me encanta entender y traspasar las tendencias actuales, analizar qué tipo de contenido es demandado actualmente por la audiencia y cómo se distribuyen los proyectos en las plataformas de streaming, redes sociales o cine.
    En mis tiempos libres, me gusta leer sobre género de ficción, drama o romance. También, a veces, practico pilates o ejercicios de respiración para deshacerme del estrés ocasional. Escucho música K-pop o pop en inglés.
    """

    # Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
    
    # Mostramos el texto
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

    # <div style='text-align: justify; font-size: 15px;'>{texto}</div>: Esta es una cadena de código HTML. 
    # La etiqueta <div> se utiliza para agrupar contenido en HTML. 
    # En este caso, el texto está justificado (text-align: justify;). 
    # El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
    # El texto dentro de las etiquetas <div> es la variable texto.
    # f"": Esto es un f-string en Python.
    # Permite insertar el valor de una variable directamente en la cadena. 
    # En este caso, {texto} se reemplaza por el valor de la variable texto.

elif  pagina_seleccionada == 'Experiencia':

    # Agregamos un título
    st.markdown("<h1 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h1>", unsafe_allow_html=True)

    # En esta sección debes describir y comentar tu experiencia aprendiendo a programar
    # ¿Cómo te sentiste al principio?, 
    # ¿Qué te ha enseñado la programación?, ¿Qué te gusta de programar?, 
    # ¿Qué te gustaría hacer con la programación en el futuro? 

    # Agregar un  texto para la respuesta
    texto_2 = """
    Me he sentido desorientada respecto a las funciones de Pyhton. Antes de matricularme en el curso, sabía la existencia de este programa, pero no lo había utilizado para mis tareas académicas o uso personal. Entonces, cuando tuve que aprender a usar este programa, fue complicado comprender el lenguaje de programación. Esta me ha enseñado a usar las estructuras de control, por ejemplo, las condicionales if/else y los bucles for/while para controlar el flujo de ejecución de un código en específico. Además, me gusta crear blogs, mapas, esquemas y gráficos visuales, pues, desde mi experiencia, ayudan a entender, de mejor manera, lo que anteriormente se ejecuta a través de códigos. En el futuro, me gustaría seguir creando algoritmos que, al ejecutarse, generen imágenes, patrones o gráficos visualmente atractivos e interesantes de trabajar 🐎🦄.
    """

    # Mostramos el texto
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2}</div>", unsafe_allow_html=True)

    # <div style='text-align: justify; font-size: 15px;'>{texto_2}</div>: Esta es una cadena de código HTML.
    # La etiqueta <div> se utiliza para agrupar contenido en HTML.
    # En este caso, el texto está justificado (text-align: justify;).
    # El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
    # El texto dentro de las etiquetas <div> es la variable texto_2.
    # f"": Esto es un f-string en Python.
    # Permite insertar el valor de una variable directamente en la cadena. 
    # En este caso, {texto_2} se reemplaza por el valor de la variable texto.

    # Agregamos un subtítulo para el video
    st.markdown("<h2 style='text-align: center;'>Presiona para observar mis comienzos en Python</h2>", unsafe_allow_html=True)
    
    # <h2 style='text-align: center;'>Aquí escribe un nombre creativo para presentar tu video</h2>: Esta es una cadena de código HTML.
    # La etiqueta <h2> se utiliza para un encabezado de segundo nivel en una página web.
    # El texto está centrado (text-align: center;).
    # El texto dentro de las etiquetas <h2> ("Aquí escribe un nombre creativo para presentar tu video") es el contenido del encabezado.
    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
    # Puedes agregar emojis en el texto de Markdown utilizando códigos de emoji.
    # Por ejemplo, puedes agregar un emoji de video 🎥 

    # Agregamos un video realizado en las practicas anteriores
    #st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E")
    
    # st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E"): Esta línea está mostrando un video en la aplicación web.
    # La función video toma como primer argumento la URL del video que se desea mostrar.
    # En este caso, la URL es "https://www.youtube.com/watch?v=X_Z7d04x9-E".
    # Puedes cambiar la URL por la de tu video en YouTube o en otra plataforma de video.

    # O creamos un botón para ir al enlace del video con button
    st.markdown(f"<div style='text-align: center;'><a href='https://drive.google.com/file/d/1O5hZ73pKA0oiZi9TmHkz1TLbZbdw_2AQ/view?usp=sharing' target='_blank'><button>Ver video</button></a></div>", unsafe_allow_html=True) 

    # <div style='text-align: center;'><a href='https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link' target='_blank'><button>Ver video</button></a></div>:
    # Esta es una cadena de código HTML.
    # La etiqueta <div> se utiliza para agrupar contenido en HTML.
    # En este caso, el contenido está centrado (text-align: center;).
    # La etiqueta <a> se utiliza para crear un enlace.
    # El atributo href especifica la URL a la que se dirige el enlace.
    # En este caso, la URL es 'https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link'.
    # El atributo target='_blank' indica que el enlace se abrirá en una nueva pestaña del navegador.
    # La etiqueta <button> se utiliza para crear un botón.
    # El texto dentro de las etiquetas <button> ("Ver video") es el contenido del botón.
    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
    # Puedes cambiar la URL por la de tu video en YouTube o en otra plataforma de video.
    
else:

    # Agregamos un título para la página de gráficos
    st.markdown("<h1 style='text-align: center;'>Mis primeros gráficos</h1>", unsafe_allow_html=True)

    # Creamos una lista de gráficos
    graficos = ['Gráfico de barras verticales de lenguas aisladas', 'Gráfico de barras de familias lingüísticas', 'Gráfico de barras horizontales de familias lingüísticas', 'mapa cusco']

    # Creamos un cuadro de selección en la página de gráficos
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    # El cuadro de selección se crea con la función selectbox.
    # El primer argumento es el texto que se muestra en el cuadro de selección.
    # El segundo argumento es una lista de opciones que se pueden seleccionar.
    # En este caso, las opciones son los elementos de la lista graficos.
    # La opción seleccionada se asigna a la variable grafico_seleccionado.
    # La variable grafico_seleccionado se utiliza para mostrar el gráfico correspondiente en la aplicación web.
    

    # Mostramos el gráfico seleccionado
    if grafico_seleccionado == 'Gráfico 1: Promedio de tarjetas rojas recibidas por equipo como local':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico de barras muestra el promedio de tarjetas rojas recibidas por cada equipo jugando como local, revelando que Alavés, Leganés y Sevilla son los clubes con la mayor indisciplina al superar el 0.25 de promedio. Contrastando esta tendencia, la mayoría de los equipos presenta promedios muy bajos (0.05 o menos), destacando que Barcelona, Osasuna y Real Madrid tienen un promedio de cero tarjetas rojas recibidas como locales.</div>", unsafe_allow_html=True)
        st.image("Promedio de tarjetas rojas recibidas por equipo como local.png", caption='Gráfico de barras', width=500)
        pass
    elif grafico_seleccionado == 'Gráfico 2: Real Madrid - Resultados como local':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico circular ilustra la notable dominancia del Real Madrid jugando en su estadio, ya que un abrumador 84.2% de sus partidos como local resultaron en victoria. Las derrotas (10.5%) y los empates (5.3%) constituyen una pequeña fracción de sus resultados, lo que confirma que el equipo es extremadamente sólido y formidable cuando juega ante su afición.</div>", unsafe_allow_html=True)
        st.image("Real Madrid - Resultados como local.png", caption='Gráfico circular', width=500)
        pass
    elif grafico_seleccionado == 'Gráfico 3: Goles anotados por el equipo de Barcelona':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El histograma muestra la frecuencia con la que el F.C. Barcelona anotó una determinada cantidad de goles en sus partidos jugando como local. La barra más alta indica que el resultado más común es anotar entre 1 y 2 goles (probablemente 2), ya que esto ocurrió en 7 ocasiones. Por otro lado, el equipo tuvo una frecuencia moderada de anotar entre 4 y 5 goles (4 ocasiones), y una frecuencia menor de anotar entre 6 y 7 goles (2 ocasiones). También, es notable que hubo una ocasión en la que el equipo anotó 0 goles y otra en la que anotó entre 3 y 4 (probablemente 3), lo que indica una buena variabilidad pero con una concentración de resultados en un número bajo a medio de goles.</div>", unsafe_allow_html=True)
        st.image("Gráfico de Barcelona 1.png", caption='Gráfico de barras', width=500)
        pass
    elif grafico_seleccionado == 'Mapa de mis películas favoritas':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El archivo mapa_peliculas_favoritas.html es un mapa interactivo geográfico creado con la librería Folium, que utiliza marcadores de cine (íconos de película de color rojo) para visualizar la ubicación geográfica asociada a sus películas favoritas. Específicamente, el mapa incluye marcadores en diversas partes del mundo, incluyendo Noruega (Frozen), cerca de Francia/Suiza (La Bella y la Bestia), Sudamérica (Up), Los Ángeles (Titanic) y Tokio (Hachiko), donde cada marcador al ser seleccionado despliega una ventana emergente con el título, director, año, país y género de la película correspondiente.</div>", unsafe_allow_html=True)
        # Si "mapa_cusco.html" es un archivo HTML (no una imagen), debes mostrarlo con st.components.v1.html
        import streamlit.components.v1 as components
        with open("mapa_peliculas_favoritas.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=500)
        pass

    # if grafico_seleccionado == 'Gráfico de barras verticales de lenguas aisladas':
    # st.markdown("<div style='text-align: justify; font-size: 20px;'>Aquí debe ir una breve interpretación de tu gráfico</div>", unsafe_allow_html=True)
    # st.image("aisladas_base_datos.png", caption='Gráfico de lenguas aisladas', width=500): Esta línea está mostrando una imagen en la aplicación web.
    # La función image toma como primer argumento el nombre del archivo de la imagen que se desea mostrar.
    # En este caso, la imagen es "aisladas_base_datos.png".
    # El argumento caption se utiliza para proporcionar una etiqueta a la imagen,
    # en este caso "Gráfico de lenguas aisladas".
    # El argumento width se utiliza para especificar el ancho de la imagen, en este caso 500 píxeles.

    # elif grafico_seleccionado == 'mapa_cusco':
    # import streamlit.components.v1 as components
    # with open("mapa_cusco.html", "r", encoding="utf-8") as f:
    #     html_content = f.read()
    # components.html(html_content, height=500): Esta línea está mostrando un archivo HTML en la aplicación web.
    # La función components.html toma como primer argumento el contenido HTML que se desea mostrar.
    # En este caso, el contenido HTML se lee desde el archivo "mapa_cusco.html".
    # El argumento height se utiliza para especificar la altura del contenido HTML, en este caso 500 píxeles.
    
    # Si no tenemos el archivo HTML, podemos agregar el código para crear el mapa de Cusco directamente en Streamlit.
    # Primero debes crear el diccionario de coordenadas del mapa de Cusco.
    # Luego debes crear el mapa utilizando la librería folium y streamlit-folium.
    # pip install folium
    # pip install streamlit-folium
        #import folium
        #from streamlit_folium import st_folium

        # Mostrar el mapa en Streamlit
        #st_folium(mapa_cusco, width=700, height=500)
    



