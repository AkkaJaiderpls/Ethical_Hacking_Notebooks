# INTRODUCCION A MYSQL #

<br>

Es crucial aprender mas sobre MYSQL y SQL para comprender el como funcionan las inyecciones de SQL para utilizarlas correctamente.

<br>

## LENGUAJE DE CONSULTAS ESTRUCTURADO SQL ##

<br>

La sintaxis de SQL puede diferir de un RDBMS a otro. Sin embargo, todos deben seguir el estandar ISO para el lenguaje de consulta estructurado. Vamos a ver la sintaxis de MYSQL/MariaDB para los ejemplos.

SQL se puede usar para realizar las siguientes acciones:

 * Recuperar Datos

 * Actualizar Datos

 * Borrar Datos

 * Crear nuevas tablas y bases de datos

 * Agregar y/o Eliminar usuarios

 * Asignar permisos a estos usuarios

<br>

## LINEA DE COMANDOS ##

<br>

La utilidad "mysql" se utiliza par autenticarse e interactuatse con una base de datos MYSQL/MariaDB. La bander "-u" se utiliza para proporcionar el nombre de usuario y la bander "-p" para la contraseña. La bandera -p deber pasarse vacia con el objetivo de no pasarla directamente en la linea de comandos, ya que podria almacenarse como texto sin cifrar en el archivo "bash_history".

<br>

    $   mysql -u root -p
        Enter password:
        ...SNIP...

    MariaDB>

<br>

<br>

Nuevamente, tambien es posible usar la contraseña directamente en el comando, aunque esto debe evitarse, ya que podria almacenarse en el historial de la terminal.

    $   mysql -u root -p<password>
        Enter password:
        ...SNIP...

    MariaDB>

<br>

    Nota: No debe haber espacio entre '-p' y la contraseña.

<br>

Los ejemplos anteriores iniciamos como superusuario, es decir "root" con la contraseña "password" para tener privilegios para ejecutar todos los comandos. Otros usuarios pueden tener privilegios menores. Podemos ver que privilegios tenemos usando el comando SHOW GRANTS que veremos mas adelante.

Cuando no especificamos un HOST, por defecto usaremos el servidor de localhost. Podemos especificar un host remoto y un puerto usando las banderas "-h" y "-P".

<br>

    $   mysql -u root -h docker.hackthebox.eu -P 3306 -p

        Enter password:
        ...SNIP...

    MariaDB>

<br>

    Nota: El puerto MYSQL/MariaDB predeterminado es (3306), pero se puede configurar en otro puerto. Se especifica usando una "P" mayuscula a diferencia de la "p" minuscula que se usa para las contraseñas.

<br>

## CREANDO UNA BASE DE DATOS ##

<br>

Una vez que iniciamos sesion en la base de datos usando el mysql, podemos comenzar a realizar consultas SQL para interactuar con el DBMS. Por ejemplo, se puede crear una nueva base de datos dentro de MYSQL DBMS usando la instruccion "CREATE DATABASE".

<br>

    mariadb> CREATE DATABASE users;

    Query OK, 1 row affected (0.02 sec)

<br>

MYSQL espera que las consultas de la linea de coandos terminen con un punto y coma. El ejemplo anterior creo una base de datos llamada USERS. Podemos ver la lista de base de datos con "SHOW DATABASE", y podemos camviar a la base de datos USERS con la declaracion "USE".

    mariadb> SHOW DATABASES;

    +--------------------+
    | Database           |
    +--------------------+
    | information_schema |
    | mysql              |
    | performance_schema |
    | sys                |
    | users              |
    +--------------------+

    mariadb> USE users;

    Database changed

<br>

## TABLAS ##

<br>

Los DBMS almacenan los datos en formato de tablas. Una tabla se compone de FILAS horizontales y COLUMNAS verticales. La interseccion de una fila y de una columna es llamada CELDA. Cada tabla se crea con un conjunto fijo de columnas, donde cada columna es de un tipo de datos en particular.

Un tipo de datos define que valor debe de tener una columna. Podemos encontrar una lista de estos datos en MYSQL [aqui.](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)

<br>

    CREATE TABLE logins (
    id INT,
    username VARCHAR(100),
    password VARCHAR(100),
    date_of_joining DATETIME
    );

<br>

Como podemos ver el CREATE TABLE primero especificamos el nombre de la tabla y luego (entre parentesis) especificamos cada columna por su nombre y por su tipo de dato, todos separados por comas. Despues del nombre y del tipo podemos especificar sus propiedades especificas.

<br>

    mariadb> CREATE TABLE logins (
    ->     id INT,
    ->     username VARCHAR(100),
    ->     password VARCHAR(100),
    ->     date_of_joining DATETIME
    ->     );
    Query OK, 0 rows affected (0.03 sec)

Las consultas anteriores crean una tabla llamada logins con cuatro columnas. La primera de ella es el "id",  un numero entero. Las siguientes dos son el "username" y la "password" que se establecen en cadenas de 100 caracteres cada una. Cualquier entrada mas larga que esto nos arrojara un error. La columna "date_of_joining" es de tipo DATETIME que almacena la fecha en la que se agrego al sistema.

<br>

    mariadb> SHOW TABLES;

    +-----------------+
    | Tables_in_users |
    +-----------------+
    | logins          |
    +-----------------+
    1 row in set (0.00 sec)

<br>

Se puede obtener una lista de tablas en la base de datos actual usando el SHOW TABLES. Demas la palabra DESCRIBE se usa para listar la estructura de la tabal con sus campo y su tipo de datos.

    mariadb> DESCRIBE logins;

    +-----------------+--------------+
    | Field           | Type         |
    +-----------------+--------------+
    | id              | int          |
    | username        | varchar(100) |
    | password        | varchar(100) |
    | date_of_joining | date         |
    +-----------------+--------------+
    4 rows in set (0.00 sec)

<br>

## PROPIEDADES DE LA TABLA ##

<br>

Dentro de la consulta CREATE TABLE, hay muchas propiedades qye se pueden establecer para la tabla y cada columna. Por ejemplo, podemos configurar la columna ID para auto-incrementanr de manera automatica cada que se inserta un registro a la tabla con la palabra clave AUTO-INCREMENT.

<br>

    id INT NOT NULL AUTO_INCREMENT,

<br>

La restriccion NOT NULL se asegura que una columna nunca se quede vacia, viene siendo como un "campo obligatorio", tambien podemos usar las restricciones UNIQUE que garantizan que un registro insertado sea siempre unico, lo vemos ocasionalmente en nombres de usuarios para evisar que existan dos iguales.

<br>

    username VARCHAR(100) UNIQUE NOT NULL,

<br>

Otra palabra clave importante es la DEFAULT, palabra clave que es usada para especificar un valor predeterminado. con el parametro "Now()" indicamos la hora actual del sistema.

    date_of_joining DATETIME DEFAULT NOW(),

Finalmente, una de las propiedades mas importantes es PRIMARY KEY, que vamos a utilizar para identificar de manera unica cada registro de una tabla.

<br>

    PRIMARY KEY (id)

<br>

Visto todo nuestra consulta de CREATE TABLE nos quedaria de la siguiente manera.

    CREATE TABLE logins (
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    date_of_joining DATETIME DEFAULT NOW(),
    PRIMARY KEY (id)
    );
