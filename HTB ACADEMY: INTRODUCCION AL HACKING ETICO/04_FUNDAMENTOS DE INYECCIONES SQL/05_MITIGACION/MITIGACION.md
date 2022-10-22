# MITIGACION DE INYECCIONES SQL #

<br>

Hemos aprendido sobre las inyecciones SQL, por que ocurren y como podemos explotarlas. Tambien deberiamos aprender como evitar este tipo de vulnerabilidades en nuestro codigo y parchearlas cuando las encontremos. Veamos algunos ejemplo de como podemos mitifar la inyeccion de SQL.

<br>

## DESINFECCION DE ENTRADA ##

<br>

Aqui esta el fragmento de codigo de cuando vimos la omision de autenticacion.

<br>

    <SNIP>
    $username = $_POST['username'];
    $password = $_POST['password'];

    $query = "SELECT * FROM logins WHERE username='". $username. "' AND password = '" . $password . "';" ;
    echo "Executing query: " . $query . "<br /><br />";

    if (!mysqli_query($conn ,$query))
    {
            die('Error: ' . mysqli_error($conn));
    }

    $result = mysqli_query($conn, $query);
    $row = mysqli_fetch_array($result);
    <SNIP>

<br>

Como podemos ver, el guion toma en cuenta la solicitud POST de username y password y lo pasa directamente a la consulta, esto permte que un atacante inyecte lo que desee y explote la aplicacion. La inyeccion se puede evitar desinfectando cualquier entrada del usuario, lo que hace que las consultas inyectadas sean inutiles. Las bibliotecas proporcionan multiples funciones para lograr esto un ejemplo de ellas es la funcion de "mysql_real_escape_sring()". Esta funcion escapa de caracteres como ' y ", por lo que no seran tomadas en cuenta.

<br>

    <SNIP>
    $username = mysqli_real_escape_string($conn, $_POST['username']);
    $password = mysqli_real_escape_string($conn, $_POST['password']);

    $query = "SELECT * FROM logins WHERE username='". $username. "' AND password = '" . $password . "';" ;
    echo "Executing query: " . $query . "<br /><br />";
    <SNIP>

<br>

El fragmento anterior muestra como se puede utilizar la funcion.

<br>

![](https://academy.hackthebox.com/storage/modules/33/mysqli_escape.png)

<br>

Como era de esperar, la inyeccion ya no funciona debido al escape de las comillas simples. Un ejemplo similar es "pg_escape_string()" que solia escapar de las consultas de PostgreSQL.

## VALIDACION DE ENTRADA ##

<br>

La entrada del usuario tambien se puede validar en funcion de lso datos utilizados para garantizar que conicida con la entrada esperada. Por ejemplo, al tomar un correo electronico como entrada podemos validar que tenga la forma de "..@gmail.com", y asi.

Veamos un ejemplo de codigo incorrecto.

<br>

    <?php
    if (isset($_GET["port_code"])) {
        $q = "Select * from ports where port_code ilike '%" . $_GET["port_code"] . "%'";
        $result = pg_query($conn,$q);
        
        if (!$result)
        {
            die("</table></div><p style='font-size: 15px;'>" . pg_last_error($conn). "</p>");
        }
    <SNIP>
    ?>

<br>

Veamos el parametro GET de port_code, notamos que esta siendo utilizado en la consulta directamente. Ya se sabe que un codigo de puerto se compone unicamente letras o espacos. Podemos restringir la entrada unicamente a estos caracteres o que evitara una inyeccion de consultas. Para ello vamos a emplear expresiones regulares.

<br>

    <SNIP>
    $pattern = "/^[A-Za-z\s]+$/";
    $code = $_GET["port_code"];

    if(!preg_match($pattern, $code)) {
    die("</table></div><p style='font-size: 15px;'>Invalid input! Please try again.</p>");
    }

    $q = "Select * from ports where port_code ilike '%" . $code . "%'";

<br>

El codigo se modifica para usar la funcion de "preg_match()" que verifica si la entrada coincide o no con el patron dado El patron que estamos usando es [A-Az-z\s]+, que solo coinside con cadenas que contengan letras y espacios. Cualquier otro caracter dara por terminada la entrada.

<br>

![](https://academy.hackthebox.com/storage/modules/33/postgres_copy_write.png)

<br>

Podemos probar la siguiente inyeccion.

<br>

    '; SELECT 1,2,3,4-- -

<br>

![](https://academy.hackthebox.com/storage/modules/33/postgres_copy_write.png)

<br>

Como se ve en las imagenes de arriba, el servidor rechazo la entrada con consultas inyectadas.

<br>

## PRIVILEGIOS DE USUARIO ##

<br>

Como discutimos anteriormente, los softwares DBMS permiten la creacion de usuarios con permisos detallados. Debemos asegurarnos de que el usuario que cosulta a las base de datos tenga permisos minimos.

Los superusuarios y usuarios con privilegios administrativos nunca deben de usarse con aplicaciones web. Estas cuentas tienen acceso a funciones y caracteristicas delicadas que podrian llegar a comprometer el servidor.

<br>

    MariaDB [(none)]> CREATE USER 'reader'@'localhost';

    Query OK, 0 rows affected (0.002 sec)


    MariaDB [(none)]> GRANT SELECT ON ilfreight.ports TO 'reader'@'localhost' IDENTIFIED BY 'p@ssw0Rd!!';

    Query OK, 0 rows affected (0.000 sec)

<br>

Los comandos anteriores agregan un nuevo usuario de MariaDB llamado reader, a quien se concede solamente los privilegios de SELECT en la tabla ports. Podemos verficar los permisos de este usuario iniciando sesion.

<br>

    xJplz@htb[/htb]$ mysql -u reader -p

    MariaDB [(none)]> use ilfreight;
    MariaDB [ilfreight]> SHOW TABLES;

    +---------------------+
    | Tables_in_ilfreight |
    +---------------------+
    | ports               |
    +---------------------+
    1 row in set (0.000 sec)


    MariaDB [ilfreight]> SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA;

    +--------------------+
    | SCHEMA_NAME        |
    +--------------------+
    | information_schema |
    | ilfreight          |
    +--------------------+
    2 rows in set (0.000 sec)


    MariaDB [ilfreight]> SELECT * FROM ilfreight.credentials;
    ERROR 1142 (42000): SELECT command denied to user 'reader'@'localhost' for table 'credentials'

<br>

El fragmento anterior confirma que el usuario reader no puede consultar otras tablas.

<br>

## CORTAFUEGOS DE APLICACIONES WEB WAF ##

<br>

Los cortafuegos de aplicaciones web (WAF) se utilizan para detectar entradas maliciosas y rechazar cualquier solicitud HTTP que las contenga. Esto ayuda a prevenir inyecciones SQL incluso cuando la logica de la aplicacion esta defectuosa. Los WAF pueden ser de codigo abierto como (ModSecurity) o premium (Cloudflare). La mayoria de ellos tienen reglas predeterminadas. Por ejemplo, cualquier solicitud que contenga INFORMATION_SCHEMA seria rechazada, ya que generalmente se usa al explotar inyecciones SQL.

<br>

## CONSULTAS PARAMETRIZADAS ##

<br>

Otra forma de garantizar que la entrada se desinfecte de una maenra segura es mediante el uso de consultas parametrizadas. Las consultas parametrizadas contienen marcadores de posiciones para los datos de entrada que luego los controladores escapan y transmiten. En lugar de pasar directamente una consulta SQL, usamos marcadores de posicion y luego llenamos con funciones de PHP.

Veamos el codigo.

<br>

    <SNIP>
    $username = $_POST['username'];
    $password = $_POST['password'];

    $query = "SELECT * FROM logins WHERE username=? AND password = ?" ;
    $stmt = mysqli_prepare($conn, $query);
    mysqli_stmt_bind_param($stmt, 'ss', $username, $password);
    mysqli_stmt_execute($stmt);
    $result = mysqli_stmt_get_result($stmt);

    $row = mysqli_fetch_array($result);
    mysqli_stmt_close($stmt);
    <SNIP>

<br>

la consulta se modifica para contener dos marcadores de posicion que marcaremos con un "?" donde se colocara el nomrbe de usuario y la contraseña. Luego vinculamos el nombre de usuario y la contraseña a la consulta usando "mysqli_stmt_bind_param()". Esto escapara de forma segura de las comillas y colocara los valores en la consulta.

<br>

## CONCLUSION ##

<br>

La lista anterior no es exhaustiva y aun podria ser posible explotar la inyeccion SQL en funcion de la logica de la aplicacion. Los ejemplos de codigo que mostramos se banasn en PHP, pero la logica se aplica a todos los lenguajes y bibliotecas comunes.