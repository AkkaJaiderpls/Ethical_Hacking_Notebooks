# INTRODUCCION A LAS BASES DE DATOS

Antes de aprender sobre las inyecciones de SQL, debemos aprender mas sobre las bases de datos y el lenguaje de consultas estructurado (SQL). Las aplicaciones web utilizan bases de datos de back-end para almacenar diversos contenidos e informacion relacionada con la aplicacion web. Estos pueden ser activos de aplicaciones web ccentrales como imagenes y archivos, contenido como publicaciones y actualizaciones, o datos de usuario como nombres de usuario y contraseñas.

Hay muchos tipos diferentes de bases de datos, cada uno de los cuales se ajusta a un tipo particular de uso. Tradicionalmente, una aplicacion usaba base de datos basadas en archivos, lo que era muy lento con el aumento de tamaño. Esto llevo a la adopcion de los llamados Database Management System (DBMS).

## SISTEMAS DE GESTION DE BASES DE DATOS (DBMS)

Un Sistema de Administracion de Bases de Datos (DBMS) ayuda a crear, definir, alojar y administrar bases de datos. Se diseñaron varios tipos de DBMS a lo largo del tiempo, como DBMS relacional basado en archivos, NoSQL, basado en graficos y almacenes de clave/valor.

Existen multiples formas de interactuar con un DBMS, como herramienta de linea de comandos. interfaces graficas o incluso API (interfaces de programacion de aplicaciones). Los DBMS se utilizan en varios sectores de la banca, las finanzas y la educacion para registrar grandes cantidades de adatos. Algunas de las caracteristicas esenciales de un DBMS incluyen:

### *   CONCURRENCIA.-
Una aplicacion del mundo real puede tener multiples usuarios interactuando con ella simultaneamente. Un DBMS se asegura de que estas interacciones simultaneas tengan exito sin corromper ni perder ningun dato.

### *   CONSISTENCIA.-
Con tantas interacciones simultaneas, el DBMS debe asegurarse de que los datos permanezcan consistentes y validos en toda la base de datos.

### *   SEGURIDAD.-
Un DBMS proporciona controles de seguridad detallados a traves de permisos y autenticacion de usuarios. Esto evitara la visualizacion o edicion no autorizada de datos confidenciales.

### *   RELIABILIDAD.-
Es facil hacer una copia de seguridad de las bases de datos y revertirlas a un estado anterior en caso de perdida de datos o una violacion.

### *   LENGUAJE DE CONSULTA ESTRUCTURADO.-
SQL simplifica la interaccion del usuario con la base de datos con una sintaxis intuituva que admite varias operaciones.

## ARQUITECTURA

TER1 generalmente consiste en aplicaciones del lado del cliente, como sitios web o programas GUI. Estas aplicaciones consisten en interacciones de alto nivel, como el inicio de sesion del usuario o los comentarios. Los datos de estas interacciones se pasan a TIER2 a traves de llamadas API u otras aplicaciones.

El segundo mivel es el middleware, que interpreta estos eventos y los pone en la forma requerida por el DBMS. Finalmente, la capa de aplicacion utiliza bibliotecas y controladores especificos segun el tipo de DBMS para interactuar con ellos. El DBMS recibe consultas de segundo nivel y realiza las operaciones solicitadas. Estas operaciones podrian incluir la insercion, recuperacion, eliminacion o actualizacion de datos. Despues del procesamiento, el DBMS devuelve los datos solicitados o los codigos de error en casos de consultas no validas.

Es posible aloar el servidory el DBMS en el mismo host. Sin embargo, las bases de datos con grandes vantidades de datos que admiten muchos usuarios normalmente se alojan por separado para mejorar el rendimiento y la escabilidad.