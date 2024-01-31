## Objetivos
- Crear plantilla de entornos de trabajo personalizadas para analisis
- Desarrollar proyectos autocontenibles y multiplataforma

## Plantillas de proyecto
Medio que posibilita portar o construir un diseño predefinido.
#### Por qué usarlo ?
- Agilizar tu trabajo
- La rutina y automatización reducirán la fatiga por decisión
- Personalizar es más fácil que construir de cero
- La reproducibilidad se vuelve mucho más factible
- Encontrar las cosas se vuelve sencillo

### Cookiecutter
Manejador de plantillas multiplataforma
- Parmite crear plantillas en cualquier lenguaje
- Se puede utilizar desde la terminal o como una libreria
- Por detras utiliza jinja que esta escrito con lenguaje similar a python

#### Instalacion
- Crear una carpeta para almacenar el proyecto
- conda config --add channels conda-forge 
    - Esto es para que conda utilice un gestor de paquete (conda-forge) que es donde esta cookiecutter
- Metodos
    - Creando un entorno de desarrollo unico para el proyecto
        - conda create --name name_proyect cookiecutter=1.7.3
        - En este caso usamos un paquete especifico
    - Instalando en un entorno ya creado
        - conda install cookiecutter
        - pip install cookiecutter
- conda env export --from-history --file environment.yml
    - Para guardas informacion de que debe instalar para instalar en otros equipos
#### Crear crear proyecto desde una plantilla
- Crear proyecto desde otra plantilla ya creada en github
    - cookiecutter https://github.com/platzi/curso-entorno-avanzado-ds --checkout cookiecutter-personal-platzi
    - En este caso se utiliza --checkout porque la plantilla esta en una rama especifica
    - Seguimos las instrucciones y ya podemos iniciar a trabajar

#### Crear plantilla perzonalizada
1. Crear carpeta
    - mkdir {{ cookiecutter.project_slug }}
    - Todo lo que esta en esta carpeta es lo que siempre se creara
2. Crear carpetas y archivos que siempre se utilizaran en los proyectos
    - Utilizar {{ cookiecutter.name_variable }} en los archivos que se quieran crear variables para que se puedan cambiar al momento de hacer el proyecto
    - Tambien se pueden crear condicionales como por ejemplo 
        ```
        {% if cookiecutter.project_packages == "All" -%}
            - fs
            - jupyter
            - jupyterlab
            - pathlib
            {% endif -%}
            - pip
        {% if cookiecutter.project_packages == "All" -%}
            - pyprojroot
        {% endif -%}
            - python={{ cookiecutter.python_version }}
            - pip:
        {% if cookiecutter.project_packages == "All" -%}
                - pyhere
        {% endif -%}
        ```
3. Crear archivo de configuracion de variables
    - cookiecutter.json -> Se crea fuera de la carpeta de la estructura
    - Se crean las variables y sus valor por defecto


4. Crear un Proyecto
    cookiecutter ./Folder/origin


#### Implementar hooks
Son tareas que se ejecutan antes o despues de crear el proyecto
1. Se debe crear la carpeta hooks
2. Crear los archivos
    - pre_gen_project.py
    - post_gen_project.py
3. Escribir instrucciones en los dos archivos para que se ejecuten antes o despues de las creaciones

#### Cargar Repositorio
1. Crear repositorio en git hub
2. Crear el archivo .gitkeep para las carpetas vacias, con el fin de que git cree las carpetas
3. Inicializar repositorio y crear el primer commit
4. Crear la coneccion con git hub y cargarlo
