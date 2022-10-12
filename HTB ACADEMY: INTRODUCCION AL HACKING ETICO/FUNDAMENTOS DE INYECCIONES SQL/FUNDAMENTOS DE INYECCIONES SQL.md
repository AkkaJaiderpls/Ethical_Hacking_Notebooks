# INTRODUCCION #

<br>

La mayoria de las aplicaciones web modernas usan una estructura de base de datos en el back-end. Dichas bases de datos se utilizan para almacenar y recuperar datos relacionados con la aplicacion web.

Para que las aplicaciones web sean dinamicas, la aplicacion web debe interactuar con la base de datos en tiempo real. A medida que llegan solicitudes HTTP(S) del usuario, el back-end de la aplicacion emitira consultas a la base de datos para generar respuestas.

<br>

![](https://academy.hackthebox.com/storage/modules/33/db_request_3.png)

<br>

Cuando la informacion proporcionada por el usuario se usa para construir la consulta a la base de datos, los usuarios malintencionado pueden engañar a la consulta para que se use para algo diferente a lo que pretendia el programador original.

La inyeccion SQL se refiere a ataques contra bases de datos relacionales como MySQL (mientras que las inyecciones contra bases de datos no relacionales, como MongoDB, son inyecciones NoSQL).

<br>

## INYECCION SQL (SQLi) ##

<br>

Muchos tipos de vulnerabilidades de inyeccion son posibles dentro de las aplicaciones web, como la inyeccion HTTP, la inyeccion de codigo y la inyeccion de comandos. El ejemplo mas comun, sin embargo, es la inyeccion SQL. Una inyeccion SQL ocurre cuando un usuario malintencionado intenta pasar una entrada que cambia la consulta SQL final enviada por la aplicacion web a la base de datos. lo que permite realizar otras consultas SQL no deseadas.

Hay muchas formas de lograr esto. Para que funcione una inyeccion SQL, el atacante debe inyectar codigo SQL y luego subvertir la logica de la aplicacion web cambiando la consulta original o ejecutando una completamente nueva. Primero, el atacante tiene que inyectar codigo fuera de los limites esperados de entrada del usuario. En el caso mas basico, eso se hace inyectando una comilla simple (') o una comilla doble (") para escapar de los limites de la entrada del usuario e inyectar datos directamente en la consulta SQL.

Una vez que un atacante puede inyectar, debe buscar una forma de ejecutar una consulta SQL diferente. Esto se puede hacer usando codigo SQL para crear una consulta funcional que ejecute tanto la consulta SQL prevista como la nueva. Hay muchas formas de lograr esto, como usar consultas apiladas o consultas de union. Finalmente, para recuperar el resultado de nuestra nueva consulta. debemos interpretarlo o capturarlo en el front-end de la aplicacion web.

<br>

## CASOS DE USO E IMPACTO ##

<br>

Una inyeccion SQL puede tener un impacto tremendo, especialmente si los privilegios en el servidor back-end y la base de datos son muy laxos.

Primer. podemos recuperar informacion secreta/sensible qie no deberia ser visible para nosotros como inicios de sesion y contraseñas de usuarios o informacion de tarjetas de credito, que luego se pueden usar para fines maliciosos. Las inyecciones SQL provocan muchas filtraciones de contraseñas y datos contra sitios web, que luego se reutilizan para robar cuentas de usuario, acceder a otros servicios o realizar otras acciones nefastas.

Otro caso de uso de la inyeccion SQL es subvertir la logica de la aplicacion web prevista. El ejemplo mas comun de esto es omitir el inicio de sesion sin pasar un par valido de credenciales. Los atacantes tambien pueden leer y escribir archivos directamente en el servidor de back-end, lo que puede llevar a colocar puertas traseras en el servidor de back-end y obteer control directo sobre el, y finalmente, tomar el control de todo el sitio web.

<br>

## PREVENCION ##

<br>

Las inyecciones de SQL generalmente son causadas por aplicaciones web mal codificadas o privilegios de bases de datos y servidores back-end mal asegurados. Mas adelante, veremos metodos de codificacion seguros, como la desinfeccion y validacion de la entrada del usuario y los privilegios y el control adecuado del usuario de back-end.
