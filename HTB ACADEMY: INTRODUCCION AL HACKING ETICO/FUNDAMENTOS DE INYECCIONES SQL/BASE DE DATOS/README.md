# INTRODUCCION A LAS BASES DE DATOS

<br>
Antes de aprender sobre las inyecciones de SQL, debemos aprender mas sobre las bases de datos y el lenguaje de consultas estructurado (SQL). Las aplicaciones web utilizan bases de datos de back-end para almacenar diversos contenidos e informacion relacionada con la aplicacion web. Estos pueden ser activos de aplicaciones web ccentrales como imagenes y archivos, contenido como publicaciones y actualizaciones, o datos de usuario como nombres de usuario y contraseñas.

Hay muchos tipos diferentes de bases de datos, cada uno de los cuales se ajusta a un tipo particular de uso. Tradicionalmente, una aplicacion usaba base de datos basadas en archivos, lo que era muy lento con el aumento de tamaño. Esto llevo a la adopcion de los llamados Database Management System (DBMS).

<br>

## SISTEMAS DE GESTION DE BASES DE DATOS (DBMS)

<br>

Un Sistema de Administracion de Bases de Datos (DBMS) ayuda a crear, definir, alojar y administrar bases de datos. Se diseñaron varios tipos de DBMS a lo largo del tiempo, como DBMS relacional basado en archivos, NoSQL, basado en graficos y almacenes de clave/valor.

Existen multiples formas de interactuar con un DBMS, como herramienta de linea de comandos. interfaces graficas o incluso API (interfaces de programacion de aplicaciones). Los DBMS se utilizan en varios sectores de la banca, las finanzas y la educacion para registrar grandes cantidades de adatos. Algunas de las caracteristicas esenciales de un DBMS incluyen:

<br>

### * CONCURRENCIA.- ###
Una aplicacion del mundo real puede tener multiples usuarios interactuando con ella simultaneamente. Un DBMS se asegura de que estas interacciones simultaneas tengan exito sin corromper ni perder ningun dato.

### * CONSISTENCIA.- ###
Con tantas interacciones simultaneas, el DBMS debe asegurarse de que los datos permanezcan consistentes y validos en toda la base de datos.

### * SEGURIDAD.- ###
Un DBMS proporciona controles de seguridad detallados a traves de permisos y autenticacion de usuarios. Esto evitara la visualizacion o edicion no autorizada de datos confidenciales.

### * RELIABILIDAD.- ###
Es facil hacer una copia de seguridad de las bases de datos y revertirlas a un estado anterior en caso de perdida de datos o una violacion.

### * LENGUAJE DE CONSULTA ESTRUCTURADO.- ##
SQL simplifica la interaccion del usuario con la base de datos con una sintaxis intuituva que admite varias operaciones.

## ARQUITECTURA ##

<br>

![](https://academy.hackthebox.com/storage/modules/33/db_2.png)

<br>

<br>

TER1 generalmente consiste en aplicaciones del lado del cliente, como sitios web o programas GUI. Estas aplicaciones consisten en interacciones de alto nivel, como el inicio de sesion del usuario o los comentarios. Los datos de estas interacciones se pasan a TIER2 a traves de llamadas API u otras aplicaciones.

El segundo mivel es el middleware, que interpreta estos eventos y los pone en la forma requerida por el DBMS. Finalmente, la capa de aplicacion utiliza bibliotecas y controladores especificos segun el tipo de DBMS para interactuar con ellos. El DBMS recibe consultas de segundo nivel y realiza las operaciones solicitadas. Estas operaciones podrian incluir la insercion, recuperacion, eliminacion o actualizacion de datos. Despues del procesamiento, el DBMS devuelve los datos solicitados o los codigos de error en casos de consultas no validas.

Es posible aloar el servidory el DBMS en el mismo host. Sin embargo, las bases de datos con grandes vantidades de datos que admiten muchos usuarios normalmente se alojan por separado para mejorar el rendimiento y la escabilidad.

<br>

# TIPOS DE BASES DE DATOS #

<br>

Las base de datos en general, se clasifican en "Bases de datos RELACIONALES" y "Bases de Datos NO RELACIONALES". Solo las bases de datos relacionales utilizan SQL, minetras que las bases de datos no relacionales utilizan una
variedad de metodos para su comunicacion.

<br>

## BASES DE DATOS RELACIONALES ##

<br>

![](https://academy.hackthebox.com/storage/modules/75/web_apps_relational_db.jpg)

<br>

<br>

Una base de datos relacional es el tipo mas comun de base de datos. Se puede utilizar distintos tipos de bases de datos relacionales para cada enfoque. Por ejemplo, la primera tabla pudede almacenar y mostrar informacion basica del cliente, la segunda la cantidad de productos vendidos y su costo, y la tercera tabla enumerar quien compro esos productos y con que datos de pagos.

Las tablas en una base de datos relacional tienen asociada una clave que brinda un resumen rapidp. Estas tablas (tambien llamadas entidades) estan todas relacionadas entre si.

Sin embargo, cuando se procesa una base de datos integrada, se requiere un concepto para vicvular una tabla con otra usando su clave, llamada RELATIONAL DATABASE MANAGEMENT SYSTEM (RDBMS). Muchas empresas actualmente utilizan RDBMS porque es un concepto facil de aprender, usar y comprender.

Por ejemplo, podemos tener una tabla USERS en una base de datos relacionales que contiene columnas como ID, USERNAME, FIRST_NAME, LAST_NAME y otros. Los ID se pueden utilizar como la clave de la tabla. Otra tabla, por ejemplo. puede contener puvlicaciones realizadas por todos los usuarios con coumnas como ID, USER_ID, DATE, CONTENT y asi.

Podemos vincular el ID desde la tabla USERS a la tabla POST con USER_ID para poder recuperar los detalles del usuario para cada publicacion. Una tabla puede tener mas de una clave. Asi por ejmplo, la columna ID se puede utilizar para vincular la tabla POST a otra que contenga COMENTARIOS, cada uno de los cuales pertenece a una publicacion en particular, y asi, sucesivamente.

"La relacion entre tablas dentro de una base de datos se llama ESQUEMA".

De esta manera, mediante el uso de bases de datos relacionales, se vuelve rapido y facil recuperar todos lo datos sobre in elemento en particular. Asi, por ejemplo, podemos recuperar los detalles vinculados a un usuario en especifico de todas las tablas con una sola consulta.

<br>

## BASES DE DATOS NO RELACIONALES ##

<br>

Una base de datos no relacional (tambien llamadas bases de datos NOSQL) no utilizan tablas, filas, columnas, claves principales, relaciones o esquemas. En cambio. una base de datos NOSQL almacena datos usando varios modelos de almacenamiento. Debido a la falta de una estructura definida para la base de datos, las bases de datos NOSQL son muy escalables y flexibles. Hay cuatro modelos de almacenamientos comunes para las bases de datos NOSQL:

<br>

### *   Clave-Valor ###

### *   Basado en Documentos ###

### *   Wide-Column ###

### *   Grafico ###

<br>

Cada uno de los modelos anteriores tiene una forma diferente de almacenar datos, por ejemplo, el Clave-Valor generalmente almacena datos en JSON o XML, y tiene una clave valor para cada par y almacena tanto sus datos como su valor.

<br>

![](https://academy.hackthebox.com/storage/modules/75/web_apps_non-relational_db.jpg)

<br>

El ejemplo anterior se puede representar usando JSON como:

    {
        "100001": {
        "date": "01-01-2021",
        "content": "Welcome to this web application."
        },
        "100002": {
            "date": "02-01-2021",
            "content": "This is the first post on this web app."
        },
        "100003": {
            "date": "02-01-2021",
            "content": "Reminder: Tomorrow is the ..."
        }
    }

Se parece a un elemento de diccionario en idiomas como Python o PHP.

El ejemplo mas comun de una base de datos NOSQL es MongoDB.

" Las bases de datos no relacionales tienen un metodo difernete de inteccion conocido como inyecciones NOSQL. Las inyecciones SQL son completamente distintas a las inyecciones NOSQL. "

