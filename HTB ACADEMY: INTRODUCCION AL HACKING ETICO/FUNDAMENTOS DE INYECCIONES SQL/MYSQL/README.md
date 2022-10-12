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

## LINEA DE COMANDOS

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

## CREANDO UNA BASE DE DATOS

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

