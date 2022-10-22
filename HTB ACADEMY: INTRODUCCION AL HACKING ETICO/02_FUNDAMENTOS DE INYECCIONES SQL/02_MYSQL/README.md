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

    MariaDB> CREATE DATABASE users;

    Query OK, 1 row affected (0.02 sec)

<br>

MYSQL espera que las consultas de la linea de coandos terminen con un punto y coma. El ejemplo anterior creo una base de datos llamada USERS. Podemos ver la lista de base de datos con "SHOW DATABASE", y podemos camviar a la base de datos USERS con la declaracion "USE".

    MariaDB> SHOW DATABASES;

    +--------------------+
    | Database           |
    +--------------------+
    | information_schema |
    | mysql              |
    | performance_schema |
    | sys                |
    | users              |
    +--------------------+

    MariaDB> USE users;

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

    MariaDB> CREATE TABLE logins (
    ->     id INT,
    ->     username VARCHAR(100),
    ->     password VARCHAR(100),
    ->     date_of_joining DATETIME
    ->     );
    Query OK, 0 rows affected (0.03 sec)

Las consultas anteriores crean una tabla llamada logins con cuatro columnas. La primera de ella es el "id",  un numero entero. Las siguientes dos son el "username" y la "password" que se establecen en cadenas de 100 caracteres cada una. Cualquier entrada mas larga que esto nos arrojara un error. La columna "date_of_joining" es de tipo DATETIME que almacena la fecha en la que se agrego al sistema.

<br>

    MariaDB> SHOW TABLES;

    +-----------------+
    | Tables_in_users |
    +-----------------+
    | logins          |
    +-----------------+
    1 row in set (0.00 sec)

<br>

Se puede obtener una lista de tablas en la base de datos actual usando el SHOW TABLES. Demas la palabra DESCRIBE se usa para listar la estructura de la tabal con sus campo y su tipo de datos.

    MariaDB> DESCRIBE logins;

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

# DECLARACIONES SQL #

<br>

Ahora que entendemos como utilizar MYSQL, veamos algunas consultas SQL esenciales y su uso.

<br>

## DECLARACION INSERT ##

<br>

La declaracion INSERT se usa para agregar un nuevo registro a una base de datos. Tiene la siguiente sintaxis.

    INSERT INTO table_name VALUES (column1_value, column2_value, column3_value, ...);

<br>

La sintaxis anterior requiere que el usuario complete los valores para todas las columnas presentes en la tabla.

    MariaDB> INSERT INTO logins VALUES(1, 'admin', 'p@ssw0rd', '2020-07-02');

    Query OK, 1 row affected (0.00 sec)

<br>

El ejemplo anteior muestra como agregar un nuevo inicio de sesion a la tabla de inicios de sesion (valga la redundacia), con valores apropiados a cada columna. Sin embargo, poddemos omitir el llenado de columnas que manejan valores predeterminados como "id", y "date_of_joining".

<br>

    INSERT INTO table_name(column2, column3, ...) VALUES (column2_value, column3_value, ...);

<br>

    Nota: Saltar las columnas que tienen restricciones de tipo "NOT NULL" resultara en un error, ya que es un valor obligatorio.

<br>

Tambien podemos insertar mas de un registro a la vez separandolos con una coma.

    MariaDB> INSERT INTO logins(username, password) VALUES ('john', 'john123!'), ('tom', 'tom123!');

    Query OK, 2 rows affected (0.00 sec)
    Records: 2  Duplicates: 0  Warnings: 0

<br>

## DECLARACION SELECT ##

Ahora que hemos insertado registros a las tablas nos toca ver como recuperarlos, para ello usaremos la consulta SELECT, esta consulta vamos a utilizarla mas adelante con otros propositos.

<br>

    SELECT * FROM table_name;

<br>

El simbolo de asterisco nos va permitir seleccionar TODAS LAS COLUMNAS, mientras que la palabra FROM nos va permitir indicar de que tabla queremos seleccionar.

<br>

    SELECT column1, column2 FROM table_name;

<br>

La consulta anterior seleccionara todos los datos presentes en la columna 1 y la columna 2 unicamente.

<br>

    MariaDB> SELECT * FROM logins;

    +----+---------------+------------+---------------------+
    | id | username      | password   | date_of_joining     |
    +----+---------------+------------+---------------------+
    |  1 | admin         | p@ssw0rd   | 2020-07-02 00:00:00 |
    |  2 | administrator | adm1n_p@ss | 2020-07-02 11:30:50 |
    |  3 | john          | john123!   | 2020-07-02 11:47:16 |
    |  4 | tom           | tom123!    | 2020-07-02 11:47:16 |
    +----+---------------+------------+---------------------+
    4 rows in set (0.00 sec)


    MariaDB> SELECT username,password FROM logins;

    +---------------+------------+
    | username      | password   |
    +---------------+------------+
    | admin         | p@ssw0rd   |
    | administrator | adm1n_p@ss |
    | john          | john123!   |
    | tom           | tom123!    |
    +---------------+------------+
    4 rows in set (0.00 sec)

<br>

La primera consulta del ejemplo anterior examina todos los registros de la tabla de inicios de sesion. Podemos ver los cuatro registros que insertamos anteriormente. La segunda consulta selecciona solo las columnas de nombre de usuario y contraseña omitiendo las otros dos.

<br>

## DECLARACION DROP ##

<br>

Podemos usar DROP para eliminar tablas y bases de datos del servidor.

    MariaDB> DROP TABLE logins;

    Query OK, 0 rows affected (0.01 sec)


    mysql> SHOW TABLES;

    Empty set (0.00 sec)

<br>

Como podemos ver la tabla fue eliminada por completo.

    Nota: la declaracion DROP eliminara la tabla completamente sin confirmacion, por lo que debemos usarla con precaucion.

<br>

## DECLARACION ALTER ##

<br>

Finalmente, podemos usar ALTER para cambiar el nombre de cualquier tabla y cualquiera de sus campo o para eliminar o agregar una columna a una tabla ya existente. El siguiente ejemplo agrega una nueva columna a la tabla de logins usando ADD.

<br>

    MariaDB> ALTER TABLE logins ADD newColumn INT;

    Query OK, 0 rows affected (0.01 sec)

<br>

Para renombrar una columna podemos usar el RENAME COLUMN.

<br>

    MariaDB> ALTER TABLE logins RENAME COLUMN newColumn TO oldColumn;

    Query OK, 0 rows affected (0.01 sec)

<br>

Tambien podemos cambiar el tipo de datos de una columna con MODIFY.

<br>

    MariaDB> ALTER TABLE logins MODIFY oldColumn DATE;

    Query OK, 0 rows affected (0.01 sec)

<br>

Finalmente. podemos eliminar columnas usando DROP.

<br>

    MariaDB> ALTER TABLE logins DROP oldColumn;

    Query OK, 0 rows affected (0.01 sec)

<br>

Podemos usar cualquiera de las declaraciones anteriores siempre y cuando tengamos los privilegios para hacerlo.

<br>

## DECLARACION UPDATE

A diferencia de ALTER. con la declaracion UPDATE podemos actualizar registros espeficos dentro de una tabla segun se cumplan ciertas condiciones. Su sintaxis general es:

<br>

    UPDATE table_name SET column1=newvalue1, column2=newvalue2, ... WHERE <condition>;

<br>

Especificamos el nombre de una tabla, cada columna y su nuevo valor, finalmente indicamos una condicion para actualizar registros. Veamos un ejemplo:

<br>

    MariaDB> UPDATE logins SET password = 'change_password' WHERE id > 1;

    Query OK, 3 rows affected (0.00 sec)
    Rows matched: 3  Changed: 3  Warnings: 0


    MariaDB> SELECT * FROM logins;

    +----+---------------+-----------------+---------------------+
    | id | username      | password        | date_of_joining     |
    +----+---------------+-----------------+---------------------+
    |  1 | admin         | p@ssw0rd        | 2020-07-02 00:00:00 |
    |  2 | administrator | change_password | 2020-07-02 11:30:50 |
    |  3 | john          | change_password | 2020-07-02 11:47:16 |
    |  4 | tom           | change_password | 2020-07-02 11:47:16 |
    +----+---------------+-----------------+---------------------+
    4 rows in set (0.00 sec)

<br>

La consulta anterior actualizo todas las contraseñas donde el ID sea mayor a 1.

<br>

    Nota: tenemos que especificar la clausula WHERE con UPDATE para especificar que registros se van a actualizar. Veremos mas adelante a detalle la clausula WHERE.

<br>

# CONTROLAR RESULTADOS DE UNA CONSULTA #

<br>

En esta seccion, aprenderemos como controlar la salida de los resultados de las consultas.

<br>

## CLASIFICACION DE RESULTADOS ##

<br>

Podemos ordenar los resultados de cualquier consulta usando ORDER BY y especificando la columna por la que vamos a ordenar.

<br>

    MariaDB> SELECT * FROM logins ORDER BY password;

    +----+---------------+------------+---------------------+
    | id | username      | password   | date_of_joining     |
    +----+---------------+------------+---------------------+
    |  2 | administrator | adm1n_p@ss | 2020-07-02 11:30:50 |
    |  3 | john          | john123!   | 2020-07-02 11:47:16 |
    |  1 | admin         | p@ssw0rd   | 2020-07-02 00:00:00 |
    |  4 | tom           | tom123!    | 2020-07-02 11:47:16 |
    +----+---------------+------------+---------------------+
    4 rows in set (0.00 sec)

<br>

Por defecto, la ordenacion se realiza de manera ascendente, pero podemos cambiar esto usando ASC o DESC.

<br>

    MariaDB> SELECT * FROM logins ORDER BY password DESC, id ASC;

    +----+---------------+-----------------+---------------------+
    | id | username      | password        | date_of_joining     |
    +----+---------------+-----------------+---------------------+
    |  1 | admin         | p@ssw0rd        | 2020-07-02 00:00:00 |
    |  2 | administrator | change_password | 2020-07-02 11:30:50 |
    |  3 | john          | change_password | 2020-07-02 11:47:16 |
    |  4 | tom           | change_password | 2020-07-02 11:50:20 |
    +----+---------------+-----------------+---------------------+
    4 rows in set (0.00 sec)

<br>

## RESULTADOS POR TIPO LIMIT ##

<br>

En caso de que nuestra consulta devuelva una gran cantidad de registros, podemos LIMITAR los resultados que queremos usando LIMIT y el numero de registros que queremos.

<br>

    MariaDB> SELECT * FROM logins LIMIT 2;

    +----+---------------+------------+---------------------+
    | id | username      | password   | date_of_joining     |
    +----+---------------+------------+---------------------+
    |  1 | admin         | p@ssw0rd   | 2020-07-02 00:00:00 |
    |  2 | administrator | adm1n_p@ss | 2020-07-02 11:30:50 |
    +----+---------------+------------+---------------------+
    2 rows in set (0.00 sec)

<br>

## CLAUSULA WHERE ##

<br>

Para filtrar o buscar datos especificos, podemos usar condicionales con la declaracion SELECT utilizando la clausula WHERE que nos ayudara a ajustar los resultados.

<br>

    SELECT * FROM table_name WHERE <condition>;

<br>

La consulta anterior devolvera los resultados que cumplan una condicion dada. Por ejemplo.

<br>

    MariaDB> SELECT * FROM logins WHERE id > 1;

    +----+---------------+------------+---------------------+
    | id | username      | password   | date_of_joining     |
    +----+---------------+------------+---------------------+
    |  2 | administrator | adm1n_p@ss | 2020-07-02 11:30:50 |
    |  3 | john          | john123!   | 2020-07-02 11:47:16 |
    |  4 | tom           | tom123!    | 2020-07-02 11:47:16 |
    +----+---------------+------------+---------------------+
    3 rows in set (0.00 sec)

<br>

El ejemplo anterior selecciona todos los registros donde el valor del id se mayor que 1, podemos ver como en la salida se elimino la fila 1.

<br>

    MariaDB> SELECT * FROM logins where username = 'admin';

    +----+----------+----------+---------------------+
    | id | username | password | date_of_joining     |
    +----+----------+----------+---------------------+
    |  1 | admin    | p@ssw0rd | 2020-07-02 00:00:00 |
    +----+----------+----------+---------------------+
    1 row in set (0.00 sec)

<br>

La consulta anterior selecciona el registro donde esta el nombre de usuario admin, podemos ademas usar el UPDATE para actualizar ciertos registros que cumplan una condicion.

<br>

    Nota: Los tipos de cadena y fecha deben estar estre comillas simples o dobles, mientras que los numeros no lo necesitan.

<br>

## CLAUSULA LIKE ##

<br>

Otra clausula muy util de SQL es LIKE, que permite seleccionar registros que coincidan con un determinado patron. En el siguiente ejemplo veremos como recuperar aquellos regiostros que su nombre de usuario comiencen con "admin".

<br>

    MariaDB> SELECT * FROM logins WHERE username LIKE 'admin%';

    +----+---------------+------------+---------------------+
    | id | username      | password   | date_of_joining     |
    +----+---------------+------------+---------------------+
    |  1 | admin         | p@ssw0rd   | 2020-07-02 00:00:00 |
    |  4 | administrator | adm1n_p@ss | 2020-07-02 15:19:02 |
    +----+---------------+------------+---------------------+
    2 rows in set (0.00 sec)

<br>

El simbolo de "%" actua como un comodin y conincide con todos los caracteres posteriores. Se utiliza para hacer coincidir cero o mas caracteres. Del mismo modo, el simbolo "_" se utiliza para coincidir exactamente con un caracter. La siguiente consulta va a buscar nombres de usuarios que cuenten con exactamente tres caracteres.

<br>

    MariaDB> SELECT * FROM logins WHERE username like '___';

    +----+----------+----------+---------------------+
    | id | username | password | date_of_joining     |
    +----+----------+----------+---------------------+
    |  3 | tom      | tom123!  | 2020-07-02 15:18:56 |
    +----+----------+----------+---------------------+
    1 row in set (0.01 sec)

<br>

# OPERADORES SQL #

<br>

A veces, las expresiones con una sola condicion no son suficientes para satisfacer el requisito del usuario, es por ello que en SQL podemos usar operadores logicos para utilizar multiples condiciones a la vez. Los mas comunes son AND, OR y NOT.

<br>

## OPERADOR AND ##

<br>

El operador AND toma dos condiciones y devuelve TRUE o FALSE en base a su evaluacion.

<br

    condition1 AND condition2

<br>

El resultado de la operacion AND devuelve TRUE si y solo su ambas condiciones son TRUE.

<br>

    MariaDB> SELECT 1 = 1 AND 'test' = 'test';

    +---------------------------+
    | 1 = 1 AND 'test' = 'test' |
    +---------------------------+
    |                         1 |
    +---------------------------+
    1 row in set (0.00 sec)

    MariaDB> SELECT 1 = 1 AND 'test' = 'abc';

    +--------------------------+
    | 1 = 1 AND 'test' = 'abc' |
    +--------------------------+
    |                        0 |
    +--------------------------+
    1 row in set (0.00 sec)

<br>

En terminos de MySQL, una condicion que devuelve 1 significa TRUE y la que devuelva 0 es FALSE.

<br>

## OPERADOR OR ##

<br>

Los operadores OR toman dos condiciones y devuelve TRUE cuando al menos uno de ellos sea TRUE.

<br>

    MariaDB> SELECT 1 = 1 OR 'test' = 'abc';

    +-------------------------+
    | 1 = 1 OR 'test' = 'abc' |
    +-------------------------+
    |                       1 |
    +-------------------------+
    1 row in set (0.00 sec)

    MariaDB> SELECT 1 = 2 OR 'test' = 'abc';

    +-------------------------+
    | 1 = 2 OR 'test' = 'abc' |
    +-------------------------+
    |                       0 |
    +-------------------------+
    1 row in set (0.00 sec)

<br>

Podemos ver qie la primera condicion se cumple porque al menos una de las opciones es TRUE, mientras que la segunda no se cumple porque ambas son FALSE.

<br>

## OPERADOR NOT ##

<br>

El operador NOT lo usamos para invertit un booleano, es decir TRUE se convierte en FALSE y viceversa.

<br>

    MariaDB> SELECT NOT 1 = 1;

    +-----------+
    | NOT 1 = 1 |
    +-----------+
    |         0 |
    +-----------+
    1 row in set (0.00 sec)

    MariaDB> SELECT NOT 1 = 2;

    +-----------+
    | NOT 1 = 2 |
    +-----------+
    |         1 |
    +-----------+
    1 row in set (0.00 sec)

<br>

Podemos ver que la primera consulta devuelve FALSE  ya que la inversa de la condicion 1=1 que devuelve TRUE es FALSE.

<br>

## OPERADORES DE SIMBOLOS ##

<br>

Los operadores AND, OR y NOT podemos representarlos con "&&, || y !" respectivamente.

<br>

    MariaDB> SELECT 1 = 1 && 'test' = 'abc';

    +-------------------------+
    | 1 = 1 && 'test' = 'abc' |
    +-------------------------+
    |                       0 |
    +-------------------------+
    1 row in set, 1 warning (0.00 sec)

    MariaDB> SELECT 1 = 1 || 'test' = 'abc';

    +-------------------------+
    | 1 = 1 || 'test' = 'abc' |
    +-------------------------+
    |                       1 |
    +-------------------------+
    1 row in set, 1 warning (0.00 sec)

    MariaDB> SELECT 1 != 1;

    +--------+
    | 1 != 1 |
    +--------+
    |      0 |
    +--------+
    1 row in set (0.00 sec)

<br>

## OPERADORES EN CONSULTAS ##

<br>

La siguiente consulta ennumera a todos los usuarios en los que su nombre de usuario no sea "john".

<br>

    MariaDB> SELECT * FROM logins WHERE username != 'john';

    +----+---------------+------------+---------------------+
    | id | username      | password   | date_of_joining     |
    +----+---------------+------------+---------------------+
    |  1 | admin         | p@ssw0rd   | 2020-07-02 00:00:00 |
    |  2 | administrator | adm1n_p@ss | 2020-07-02 11:30:50 |
    |  4 | tom           | tom123!    | 2020-07-02 11:47:16 |
    +----+---------------+------------+---------------------+
    3 rows in set (0.00 sec)

<br>

La siguiente consulta selecciona aquellos usuarios que tengan un id mayor a 1 y su username no sea igual a "john".

<br>

    MariaDB> SELECT * FROM logins WHERE username != 'john' AND id > 1;

    +----+---------------+------------+---------------------+
    | id | username      | password   | date_of_joining     |
    +----+---------------+------------+---------------------+
    |  2 | administrator | adm1n_p@ss | 2020-07-02 11:30:50 |
    |  4 | tom           | tom123!    | 2020-07-02 11:47:16 |
    +----+---------------+------------+---------------------+
    2 rows in set (0.00 sec)

<br>

## PRECEDENCIA DE LOS MULTIPLES OPERADORES ##

<br>

SQL admite varias operaciones, como ser suma, division y operaciones de bit a bit. Por lo tanto, una consulta podria tener multiples expresiones a la vez. El orden de estas operaciones se decide a traves de la precedencia de operadores.

Aqui hay una lista de operaciones comunes y su precedencia.


    * División ( /), Multiplicación ( *), y módulo ( %)
    * Suma ( +) y resta ( -)
    * Comparación ( =, >, <, <=, >=, !=, LIKE)
    * NO ( !)
    * Y ( &&)
    * O ( ||)

<br>

Las operaciones en la parte superior se evaluan antes que las de la parte inferior, veamos un ejemplo.

<br>

    SELECT * FROM logins WHERE username != 'tom' AND id > 3 - 2;

<br>

La consulta anterior tiene cuatro operaciones/ Por la precedencia de operaciones sabemos que la resta viene primero, por lo que primero evaluara 3-2 a 1:

<br>

    SELECT * FROM logins WHERE username != 'tom' AND id > 1;

<br>

A continuacion tenemos dos operaciones de comparación. Ambos tiene la misma precedencia y se evaluaran juntos, por lo tanto devolvera aquellos registros donde el nombre de usuario no sea Tom y todos los registros donde el id sea mayor que 1, luego aplicamos AND para devolver los registros con ambas condiciones.

<br>

    MariaDB> select * from logins where username != 'tom' AND id > 3 - 2;

    +----+---------------+------------+---------------------+
    | id | username      | password   | date_of_joining     |
    +----+---------------+------------+---------------------+
    |  2 | administrator | adm1n_p@ss | 2020-07-03 12:03:53 |
    |  3 | john          | john123!   | 2020-07-03 12:03:57 |
    +----+---------------+------------+---------------------+
    2 rows in set (0.00 sec)

<br>

Veremos algunos otros escenarios de procedencia de operadores en proximas secciones.