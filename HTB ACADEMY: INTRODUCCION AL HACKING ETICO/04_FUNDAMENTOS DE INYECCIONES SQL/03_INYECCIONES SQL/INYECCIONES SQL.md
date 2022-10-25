# INTRODUCCION A LAS INYECCIONES SQL #

<br>

Ahora que tenemos una idea general de como funcionan las consultas de MYSQL y SQL, aprendamos sobre las inyecciones SQL.

<br>

## USO DE SQL EN LAS APLICACIONES WEB ##

<br>

Primero, veamos como las aplicaciones web usan bases de datos MYSQL, en este caso para almacenar y recuperar datos.

Por ejemplo, dentro de una aplicacion PHP podemos conectarnos a nuestra base de datos, y comenzar a usar MYSQL.

<br>

    $conn = new mysqli("localhost", "root", "password", "users");
    $query = "select * from logins";
    $result = $conn->query($query);

<br>

Luego, la salida de la consulta se almacenara en "$result", y podemos imprimirla en la pagina o usarla de cualquier otra forma. El siguiente codigo PHP imprimira todos los resultados devueltos de la consulta SQL en lineas nuevas.

<br>

    while($row = $result->fetch_assoc() ){
	echo $row["name"]."<br>";
    }

<br>

Las aplicaciones web tambien suelen utilizar la entrada del usuario para recuperar datos. Por ejemplo, cuando un usuario usa la funcion de busqueda. Su entrada se pasa a la aplicacion web que usara este parametro para buscar dentro de la base de datos.

<br>

    $searchInput =  $_POST['findUser'];
    $query = "select * from logins where username like '%$searchInput'";
    $result = $conn->query($query);

<br>

## ¿QUE ES UNA INYECCION? ##

<br>

En el ejemplo anterior, aceptamos la entrada del usuario y la pasamos directamente a la consulta SQL sin desinfeccion.

<br>

    La desinfeccion se refiere a la eliminacion de cualquier caracter especial de la entrada del usuario, para interrumpir cualquier intento de inyeccion.

<br>

La inyeccion ocurre cuando una aplicacion malinterpreta la entrada del usuario como codigo real en lugar de una cadena, cambiando el flujo del codigo y ejecutandolo. Esto puede ocurrir escapando de los limites de la entrada del usuario mediante la inyeccion de algun caracter especial como (') y a continuacion, escribir codigo para ejecutarlo.

<br>

## INYECCION SQL #

<br>

Una inyeccion SQL ocurre cuando la entrada del usuario se ingresa en en la cadena de consulta SQL sin desinfectar o filtrar adecuadamente la entrada. El ejemplo anterior nos mostro como se puede usar la entrada del usuario dentro de una consulta SQL.

<br>

    $searchInput =  $_POST['findUser'];
    $query = "select * from logins where username like '%$searchInput'";
    $result = $conn->query($query);

<br>

En casos tipicos, el searchInput se ingresaria para completar la consulta, devolviendo el resultado esperado.

<br>

    select * from logins where username like '%$searchInput'

<br>

Entonces, si ingresamos "admin" se vuelve "%admin". En este caso si nosotros ejecutamos cualquier codigo SQL solo sera considerado como un termino de busqueda. POr ejemplo si ingresamos SHOW DATABASES; se ejecutaria como "%SHOW DATABASES;". La aplicacion web buscara nombres de usuarios similares a SHOW DATABASES;, Sin embargo, como no existe una desinfeccion nostros podemos agregar una comilla simple que finalizaria el campo de entrada del usuario para luego permitirnos ejecutar codigo SQL real.

<br>

    '%1'; DROP TABLE users;'

<br>

    Observemos cono agregar una simple comilla despues del 1 nos permite escapar de los limites de la entrada de usuarios.

<br>

Entonces, nuestra consulta SQL final ejecutada seria la siguiente:

<br>

    select * from logins where username like '%1'; DROP TABLE users;'

<br>

## ERRORES DE SINTAXIS ##

<br>

El ejemplo anterior de inyeccion SQL devuelve un error:

<br>

    Error: near line 1: near "'": syntax error

<br>

Esto se debe al ultimo caracter final, donde tenemos una sola comilla adicional (') que no esta cerrrada, lo que provoca un error de sintaxis SQL cuando se ejecuta.

<br>

    select * from logins where username like '%1'; DROP TABLE users;'

<br>

Para tener una inyeccion exitosa, debemos asegurarnos de que la consulta SQL recien modificada siga siendo valida y no tenga ningun error de sintaxis despues de nuestra inyeccion. Nosotros podemos evitar estos errores comentando el resto de la consulta en funcion de que DBMS este utilizando el objetivo.

<br>

## TIPOS DE INYECCIONES DE SQL ##

<br>

Las inyecciones de SQL se clasifican en funcion de como y donde recuperamos su salida.

<br>

![](https://academy.hackthebox.com/storage/modules/33/types_of_sqli.jpg)

<br>

En casos simples de inyecciones, la salida prevista de las consultas tanto previa como nueva puede leerse directamente en el front-end causando que podamos leerla directamente, este tipo de inyecciones se conocen como "Inyecciones SQL IN-BAND", y tiene dos tipos, "UNION BASED" y "ERROR BASED".

Con una inyeccion SQL Union Based, es posible que tengamos que especificar la ubicacion exacta, es decir, "columnna exacta" que podemos leer, por lo que vamos a dirigir la consulta para que se imprima ahi.

Para las inyecciones de tipo Error Based vamos a esperar obtener los errores de PHP o MYSQL en el front-end para hacer que intensionalmente el error de SQL devuelva el resultado de nuestra consulta.

En casos mucho mas complicados es posible que no obtengamos la salida impresa, por lo que vamos a usar un poco la logica SQL para recuperar la salida caracter por caracter. Esto se conoce como inyecciones SQL de tipo Blind, y tambien tiene dos tipos, "BOOLEAN BASED" o "TIME BASED".

Con una inyeccion de tipo Boolean Based, vamos a usar declaraciones condicionales SQL para controlar si la pagina devuelve algun resultado, es decir, una respuesta a la consulta original. Para las inyecciones SQL Time Based, vamos a usar declaraciones condicionales donde si recibimos true haremos que la pagina "duerma" con sleep().

Finalmente en algunos casos, es posible que no tengamos acceso directo a la salida, por lo que es posible que tengamos que dirigir la salida a una ubicacion remota, "es decir, un registro de DNS" para intentar recuperarla desde alli. Esto se conoce como Inyeccion SQL de tipo Out-Of-Band.

<br>

## SUBVERTIR LA LOGICA DE UNA CONSULTA ##

<br>

Ahora que tenemos la idea de como funcionan teoricamente las inyecciones vamos con los ejemplos.

Antes de realizar consultas SQL completas primero vamos a aprender a modificar la consulta inyectando el operador OR y usando comentarios SQL para subvertir la consulta original. Un ejemplo comun de esto es para eldir o "by passear" una autenticacion web.

<br>

## BY PASSING U OMISION DE AUTENTICACION ##

<br>

Imaginemos la siguiente pagina de inicio de sesion del administrador.

<br>

![](https://academy.hackthebox.com/storage/modules/33/admin_panel.png)

<br>

Podemos iniciar sesion con las credenciales de administrador "admin/password".

<br>

![](https://academy.hackthebox.com/storage/modules/33/admin_creds.png)

<br>

Podemos ver que la pagina nos muestra la consulta SQL que estamos ejecutando para comprender mejor como vamos a subvertir la logica de la consulta. Nuestro objetivo va a ser iniciar sesion con el usuario administrador sin conocer la contraseña existente. Como podemos ver la consulta SQL que se esta ejecutando es:

<br>

    SELECT * FROM logins WHERE username='admin' AND password = 'p@ssw0rd';

<br>

La pagina tomas las credencicales y luega usa el operador AND para seleccionar registros que coincidan con la contraseña y el usuario proporcionado. Si la base de datos devuelve registros coincidentes, significa que las credenciales son validas y se da el acceso.

<br>

![](https://academy.hackthebox.com/storage/modules/33/admin_incorrect.png)

<br>

Cuando la consulta no devuelve nada, el inicio de sesion falla negando el acceso.

<br>

## DESCUBRIMIENTO DE SQLi ##

<br>

Antes de comenzar a subvertir la logica de la aplicacion web e intentar eludir la autenticacion, primero debemos pribar si el formulario de inicio de sesion es vulnerable a las inyecciones SQL. Para ello, al final de la consulta vamos a agregar un payload y veremos si causamos algun eror o cambiamos el comportamiento de la pagina.

<br>

| PAYLOAD     | URL CODIFICADA |
| ----------- | -----------    |
| '           | %27            |
| "           | %22            |
| #           | %23            |
| ;           | %3b            |
| )           | %29            |

<br>

    NOTA: En algunos casos, es posible que tengamos que usar la version codificada de URL en la payload.

<br>

Entonces comenamos inyectando una comilla simple:

<br>

![](https://academy.hackthebox.com/storage/modules/33/quote_error.png)

<br>

Veamos que se lanzo un error de SQL en lugar de un mensaje de "Login Failed". La pagina nos arrojo un error porque la consulta resultante fue:

    SELECT * FROM logins WHERE username=''' AND password = 'something';

<br>

Generamos un error debido a que tenemos una comilla fuera de lugar.

<br>

## INYECCION OR ##

<br>

Necesitariamos que la consulta regrese true, independientemenre del nombre de usuario y la contraseña ingresada, para omitir la autenticacion. Para ello, vamos a abusar del operador OR en nuestra inyeccion SQL.

Como vimos anteriormente en la precedencia de operadores, el operador AND sera evaluado antes que el operador OR. Esto signifca que si hay al menos una condicion de TRUE en toda la consulta con un operador OR, toda la consulta sera evaluada como TRUE devolviendo que toda la consulta es verdadera.

Un ejemplo de una condicion que siempre nos devolvera TRUE es '1'='1'. Sin embargo para que nosotros podamos mantener la consulta funcionando debemos mantener un numero par de comillas, por ejemplo en lugar de usar ('1'='1'), vamos a eliminar la ultima comilla y usaremos ('1'='1), con esto generaremos de que la consulta este en su lugar.

Entonces, si inyectamos la condicion podemos forzar a recibir un true.

La consulta final debe ser la siguiente

<br>

    SELECT * FROM logins WHERE username='admin' or '1'='1' AND password = 'something';

<br>

Esto significa lo siguiente:

* Si el nombre de usuario es admin
OR
* Si 1=1 develve true (que siempre lo hace)
AND
* Si la contraseña es something.

<br>

![](https://academy.hackthebox.com/storage/modules/33/or_inject_diagram.png)

<br>

El operador AND sera evaluado primero y devolvera false. Entonces el operador OR se evaluara y si alguna de las declaraciones es true se volveria toda la condicion devolvera true. Ya que 1 = 1 siempre es true tendremos el acceso.

<br>

    NOTA: El payload que usamos anteriormente es una de las muchisimas cargas utiles de omision de autenticacion de SQLi en PayloadAllTheThings, cada una de las cuales funciona en un determinado tipo de consultas SQL.

<br>

## BYPASSING DE AUTENTICACION CON OPERADOR OR ##

<br>

Intentemos esto como nombre de usuario y veamos al respuesta.

<br>

!["https://academy.hackthebox.com/storage/modules/33/inject_success.png"]

<br>

Pudimos iniciar correctamente porque conociamos el nombre de usuario, pero ¿Y si no conocieramos un nombre de usuario valido? Probemos la misma solicitud con un nombre de usuario diferente esta vez.

<br>

![](https://academy.hackthebox.com/storage/modules/33/notadmin_fail.png)

El inicio de sesion fallo porque NotAdmin no existe en la tabla y resulto en una consulta falsa en general.

<br>

![](https://academy.hackthebox.com/storage/modules/33/notadmin_diagram_1.png)

<br>

Para iniciar sesion con exito una vez mas necesitamos una consulta que devuelva true consulta. Esto se puede lograr inyectando una condicion OR en el campo de contraseña por lo que siempre nos devolveria true. Intentemos con "somethin or '1'='1'" como la contraseña.
https

<br>

![](https://academy.hackthebox.com/storage/modules/33/password_or_injection.png)

<br>

El or adicional resulto en una consulta genera de true,] por lo que ya no tendriamos que conocer la contraseña ni el usuario.

<br>

![](https://academy.hackthebox.com/storage/modules/33/basic_auth_bypass.png)

<br>

# USANDO COMENTARIOS #

<br>

Vamos a aprender a utilizar comentarios para subvertir la logica de consultas SQL mas avanzadas terminando en una consulta SQL funcional que nos va a permitir evadir el proceso de autenticacion de inicio de sesion.

<br>

## COMENTARIOS ##

<br>

Al igual que cualquier otro lenguaje, SQL tambien permite el uso de comentarios. Los comentarios se utilizan para documentar consultas o ignorar una determinada parte de la consulta. Podemos usar dos tipos de comentarios con MySQL "--" y "#", ademas de un comentario en linea "/**/" (aunque este por lo general no se usa en inyecciones SQL). Los -- se pueden usar de la siguiente manera.

<br>

    MariaDB> SELECT username FROM logins; -- Selects usernames from the logins table

    +---------------+
    | username      |
    +---------------+
    | admin         |
    | administrator |
    | john          |
    | tom           |
    +---------------+
    4 rows in set (0.00 sec)

<br>

    NOTA: En SQL, usar solo dos guiones no es sufiente para comenzar un comentario. Entonces tiene que haber un espacio vacio despues de ellos, por lo que el comentario que comienza con (--), con un espacio al final. Esto a veces se codifica en una URL como (--+), ya que los espacios en las URL se codifican como (+). Para que quede claro, agregamos otro (-) al final para mostrar que existe un espacio.

<br>

El simbolo "#" tambien se puede utilizar.

<br>

    MariaDB> SELECT * FROM logins WHERE username = 'admin'; # You can place anything here AND password = 'something'

    +----+----------+----------+---------------------+
    | id | username | password | date_of_joining     |
    +----+----------+----------+---------------------+
    |  1 | admin    | p@ssw0rd | 2020-07-02 00:00:00 |
    +----+----------+----------+---------------------+
    1 row in set (0.00 sec)

<br>

    SUGERENCIA: Si estas ingresando una payload en la URL dentro de un navegador, un simbolo (#) generalmente se considera una etiquea y no se pasara como parte de la URL. Para usar el (#) como comentario dentro de un navegador, podemos usar el '%23' que es un simbolo de "#" codificado en URL.

<br>

El serviro ignorara la parte de la consulta con AND password = 'something' durante la evaluacion.

<br>

## BYPASS DE AUTENTICACION CON COMENTARIOS ##

<br>

Volvamos a nuestro ejemplo anterior e inectemos admin'-- como nuestro nombre de usuario, la consulta final seria:

    SELECT * FROM logins WHERE username='admin'-- ' AND password = 'something';

<br>

Como podemos ver en el resaltado de sintaxis, el nombre de usuario ahora es admin, y el resto de la consulta ahora se ignora como un comentario. Ademas, de esta manera, podemos asegurar de que la consulta no tenga un problema de sintaxis.

Intentemos usarlo en la pagina de inicio de sesion con el nombre de usuario admin'-- y cualquier cosa como la contraseña.

<br>

![](https://academyhackthebox.com/storage/modules/33/admin_dash.png)

<br>

Como vemos, pudimos omitir la autenticacion, ya que la nueva consulta modificada verifica el nombre de usuario, sin otras condiciones.

<br>

## OTRO EJEMPLO ##

<br>

SQL admite el uso de parentesis si la aplicacion necesita evaluar una condicion antes que otra. Las expresiones entre parentesis tiene prioridad sobre otros operadores y se evaluan primero. Veamos un escenario como este:

<br>

![](https://academy.hackthebox.com/storage/modules/33/paranthesis_fail.png)

<br>

La consulta anterior garantiza que la identificacion del usuario sea siempre mayor que 1, lo que evitar que alguien inicie sesion como administrador. Ademas, tambien vemos que la contraseña fue codificada antes de usarse en la consulta. Esto evitara que inyectemso a traves del campo de contraseña porque la entrada se cambia a un hash.

Intentemos iniciar sesion con credenciales validasd como admin/password para ver la respuesta.

<br>

![](https://academy.hackthebox.com/storage/modules/33/paranthesis_valid_fail.png)

<br>

Como era de esperarse, el inicio de sesion falla a pesar de que proporcionemos credenciales validos porque la identificacion del administrador es igual a 1. Asi qeu intentemos iniciar sesion con las credenciales de otro usuario como tom.

<br>

![](https://academy.hackthebox.com/storage/modules/33/tom_login.png)

<br>

El inicio de sesion con un identificador mayor a 1 fue exitoso. Entonces, ¿Como podemos iniciar sesion como un administrador? Sabemos que por la seccion anterior que podemos comentar el resto de la consulta, entonces, usando admin'-- podriamos evitarlo.

<br>

![](https://academy.hackthebox.com/storage/modules/33/paranthesis_error.png)

<br>

El inicio de sesion fallo debido a un error de sintaxis, ya que tenemos un parentesis abierto que no es cerrado. Para ejecutar la consulta correctamente añadiremos un parentesis de cierre con admin')--.

<br>

![](https://academy.hackthebox.com/storage/modules/33/paranthesis_success.png)

<br>

La consulta fue exitosa e iniciamos sesion como administrador. La consulta final de nuestra entrada es:

<br>

    SELECT * FROM logins where (username='admin')

<br>

# CLAUSULAS DE UNION #

<br>

Hasta ahora, solo hemos estado manipulando la consulta original para subvertir la lpgica de la aplicacion web y eludir la autenticacion usando el operador de OR y un comentario. Sin embargo, otro tipo de inyeccion SQL es la de consultas completas ejecutadas junto a la consulta original. Esta seccion demostrara esto mediante el uso de la consulta UNION de MYSQL para hacer "SQL Union Injection".

<br>

## UNION ##

<br>

Antes de comenzar a aprender sobre Union Injection, primero debemos aprender sobre la clasula SQL Union. La clausula de union se utiliza para combinar los resultados multiples SELECT. Esto significa que a traves de una inyeccion de UNION podremos usar la cantidad de SELECT para volcar datos de todo el DBMS, desde multiples tablas y bases de datos. Intentemos usar el operador UNION en una base de datos de ejemplo. En primer lugar veamos en contenido de la tabla ports.

<br>

    MariDB> SELECT * FROM ports;

    +----------+-----------+
    | code     | city      |
    +----------+-----------+
    | CN SHA   | Shanghai  |
    | SG SIN   | Singapore |
    | ZZ-21    | Shenzhen  |
    +----------+-----------+
    3 rows in set (0.00 sec)

<br>

A continuacion, veamos la salida de la tabla ships.

<br>

    mysql> SELECT * FROM ships;

    +----------+-----------+
    | Ship     | city      |
    +----------+-----------+
    | Morrison | New York  |
    +----------+-----------+
    1 rows in set (0.00 sec)

<br>

Ahora intentemos usar UNION para combinar ambos resultados:

<br>

    mysql> SELECT * FROM ports UNION SELECT * FROM ships;

    +----------+-----------+
    | code     | city      |
    +----------+-----------+
    | CN SHA   | Shanghai  |
    | SG SIN   | Singapore |
    | Morrison | New York  |
    | ZZ-21    | Shenzhen  |
    +----------+-----------+
    4 rows in set (0.00 sec)

<br>

Como podemos ver, UNION nos combino la salida de ambos SELECt en una sola, por lo que las entradas de ports y ships se combinaron en una sola tablad e 4 fulas. Como podemos ver, algunas de las filas pertenecen a la tabla ports mientras que otra a ships.

<br>

    NOTA: Los tipos de datos de las columnas seleccionadas en todas las posiciones deben de ser los mismos.

<br>

## COLUMNAS PARES ##

<br>

Las declaraciones de uniones solo pueden operar en aquellos SELECT que tengan el mismo numero de columnas. Por ejemplo, si intentamos dos consultas de UNION que tiene diferentes numero de columnas obtendremos el siguiente error.

<br>

    MariaDB> SELECT city FROM ports UNION SELECT * FROM ships;

    ERROR 1222 (21000): The used SELECT statements have a different number of columns

<br>

La consulta anterior da como resultado un error ya que la primera tabla devuelve una columna mientras que al segunda devuelve dos. Una vez tenemos dos consultas que devuelven el mismo numero de columnas podemos usar la declaracion de UNION para extraer datos de otras tablas y bases de datos.

Por ejemplo, si la consulta es:

<br>

    SELECT * FROM products WHERE product_id = 'user_input'

<br>

Podemos inyectar un consulta de UNION en la entrada, de modo que se devuelvan filas de otras tablas.

<br>

    SELECT * from products where product_id = '1' UNION SELECT username, password from passwords-- '

<br>

La consulta anterior devolveria username y password de las tablas suponiendo que la tabla products tiene dos columnas.

<br>

## COLUMNAS DESIGUALES ##

<br>

Descubriremos que la consulta anterior no tendra la misma cantidad de columnas que la consulta SQL que queremos ejecutar, por lo que tendremos que solucionarlo. Por ejemplo, supongamos que solo tenemos una columna. En ese caso nosotros podemos colocar datos no deseados con el objetivo de que la inyeccion devuelva la misma cantidad de columnas que las consulta original.

Por ejemplo, podemos usar cualquier cadena como nuestros datos no deseados y la consulta devulvera la cadena como salida para esa consulta. Tambien es posible uar numeros, por ejemplo SELECT 1 FROM passwords, siempre devolvera un 1 como salida.

<br>

    NOTA: Al llenar otras columnas con datos no deseados, debemos asegurarnos de que el tipo de datos coincida con loso datos de las columnas, de lo contrario nos devolvera un error. En aras de la simplicidad usaremos numeros ocmo datos basuras que tambien seran utiles para rastrear la posicion donde inyectaremos nuestro payload.

<br>

    SUGERENCIA: Para inyecciones SQL avanzadas, es posible que queramso simplemente usar NULL para llenar otras columnas, ya que NULL se adapta a todos los tipos de datos.

<br>

La tabla products tuene dos columnas, por lo que debemos realizar un union con tambien dos columnas. Si solo quisieramos obtener una columnas, por ejemplo username, tenemos que hacer "username, 2" de tal modo que tendremos el mismo numero de columnas.

<br>

    SELECT * from products where product_id = '1' UNION SELECT username, 2 from passwords

<br>

Debemos colocar la cantidad de columnas a la union que requiera la consulta, por ejemplo para cuatro columnas seria:

<br>

    UNION SELECT username, 2, 3, 4 from passwords-- '

<br>

Esta consulta nos devolveria:

    mysql> SELECT * from products where product_id UNION SELECT username, 2, 3, 4 from passwords-- '

    +-----------+-----------+-----------+-----------+
    | product_1 | product_2 | product_3 | product_4 |
    +-----------+-----------+-----------+-----------+
    |   admin   |    2      |    3      |    4      |
    +-----------+-----------+-----------+-----------+

<br>

Como podemos ver, nuestra salida deseada del :UNION SELECT username from passwords" se encuentra en la segunda fila de la primera colimnas, mientras que el resto de datos se llena con lo restante.

<br>

# INYECCIONES UNION #

<br>

Ahora que sabemos como se usa la clausula de union, vamos a aprender como usarla en nuestras inyecciones de SQL. Tomemos el siguiente ejemplo:

<br>

![](https://academy.hackthebox.com/storage/modules/33/ports_cn.png)

<br>

Veamos una posible inyeccion de SQL dentro de los parametros de busqueda. Aplicamos los pasos de SQLi Discovery inyectanod una comilla simple ('), y obteniendo un error:

![](https://academy.hackthebox.com/storage/modules/33/ports_quote.png)

<br>

Dado que causamos un error, esto puede significar que la pagina es vulnerable a la inyeccion SQL. Este escenario es ideal para la explotacion de una inyeccion basada en union, ya que podemos ver los resultados de nuestas consultas.

<br>

## DETECTAR EL NUMERO DE COLUMNAS ##

<br>

Antes de seguir adelante y explotar consultas basadas en UNION, necesitamos encontrar la cantidad de columnas seleccionadas por el servidor. Existen dos metodos para detectas el numero de columnas:

<br>

*   Usando ORDER BY

*   Usando UNION

<br>

## USANDO ORDER BY ##

<br>

La primera forma de detectar el numero de columas es a traves de la funcion de ORDER BY. Tenemos que inyectar una consulta que ordene los resultados por una columnas que vamos a especificar, es decir: 'Columna 1, Columna 2, etc' hasta que veamos in error quenos diga que la columnas especificada no existe.

Por ejemplo. podemos empezar con order by 1, ordenando solo la primera columnas, al no tener un error sabemos de que la tabla tiene al menos una columna. Entonces haremos un order by 2, y order by 3, hasta que llegemos a un numero de columnas que nos devuelva un error o la pagina no muestren nada, lo que significa que esa cantidad de columnas no existe. Usaremos la ultima columna que no nos dio error.

Si fallamos en order by 4, esto significa que la tabla tiene trs columnas. Volvemos a nuestro ejemplo anterior e intenmos con la payload:

<br>

    ' order by 1-- -

<br>

    RECORDATORIO: Agregamos un guion adicional al final (-) para mostrarle de que existe un espacio despues de los (--).

<br>

Como vemos, obtenemos un resultado normalmente:

<br>

![](https://academy.hackthebox.com/storage/modules/33/ports_cn.png)

<br>

A continuacion, intentemos ordenar por la segunda columna con la siguiente payload.

<br>

    ' order by 2-- -

<br>

Todavia tenemos el resultado. notamos de que estan ordenados de manera diferente como era de esperarse.

<br>

![](https://academy.hackthebox.com/storage/modules/33/order_by_2.jpg)

<br>

Hacemos lo mismo para las columnas 3 y 4 recuperando los datos, sin embargo, cuando intentamos con order by 5 obtenemos el siguiente error:

<br>

![](https://academy.hackthebox.com/storage/modules/33/order_by_5.jpg)

<br>

Esto significa que esta tabla tiene exactamente 4 columnas.

<br>

## USANDO UNION ##

<br>

El otro metodo es intentar una inyeccion de union con diferentes numeros de columnas hasta que obtengamos lso resultados con exito. Podemos intentar con una columnas de 3 consultas de UNION:

<br>

    cn' UNION select 1,2,3-- -

<br>

Recibimos un error que dice que el numero de columnas no coincide:

<br>

![](https://academy.hackthebox.com/storage/modules/33/ports_columns_diff.png)

<br>

Entonces probamos con cuatro columnas y veamos las respuesta.

<br>

    cn' UNION select 1,2,3,4-- -

<br>

![](https://academy.hackthebox.com/storage/modules/33/ports_columns_correct.png)

<br>

Esta vez obtuvimos con exito los resultados, lo que significa una vez mas que la tabla tiene 4 columnas. Podemos usar cualquier metodo para obtener el numero total de las columnas. Una vez que conocemos el numero de columnas, sabemos como formar nuestro payload y podemos continuar.

<br>

## UBICANDO LA INYECCION ##

<br>

Si bien una consulta puede devolver varias columnas, es posible que la aplicacion solo muestre alguna de ellas. Entonces, si inyectamos nuestra consulta en una columna que no esta impresa en la pagina, no obtendremos su salida. Es por eso que necesitamos determinar que columnas se imprimen en la pagina, para determinar donde colocar nuestra inyeccion. En el ejemplo anterior, mientras que la consulta inyectada devolvia 1, 2, 3, 4 y 5 solo vimos el 2, 3, y 4 en la pagina como datos de salida.

<br>

![](https://academy.hackthebox.com/storage/modules/33/ports_columns_correct.png)

<br>

Es muy comun que no todas las tablas se muestren al usuario. Por ejemplo, el campo ID a mendo se utiliza para vincular diferentes tablas, pero el usuario no necesita verlo. Esto nos indica que podemos colocar nuestra inyeccion en la columnas 2, 3 y 4.

Este es el beneficio de usar numeros como nuestros datos no deseados, ya que facilita el seguimiento de las columnas qeu se imprimen, para que sepamos en que columnas colocar nuestra inyeccion. Para probar que podemos obtener datos reales de la base de datos en lugar de solo numeros podemos usar la conuslta "@@versio@ como prueba y colocarla en lugar del numero 2.

<br>

    cn' UNION select 1,@@version,3,4-- -

<br>

![](https://academy.hackthebox.com/storage/modules/33/db_version_1.jpg)

<br>

Como podemos ver, podemos mostrar la version de la base de datos. Ahora sabemos como formar nuestras cargas utilies para obtener con exitp el resultado de nuestras consultas impresa en la pagina. En la siguiente seccion, discutiremos el como ennumerar la base de datos y obtener datos de otras tablas y bases de datos.