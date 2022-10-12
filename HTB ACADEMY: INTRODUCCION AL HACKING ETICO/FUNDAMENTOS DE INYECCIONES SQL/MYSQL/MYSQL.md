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

    $   mysql -u "usuario" -p
        Enter password:
        ...SNIP...

    MariaDB>

<br>

    Nota: El puerto MYSQL/MariaDB predeterminado es (3306), pero se puede configurar en otro puerto. Se especifica usando una "P" mayuscula a diferencia de la "p" minuscula que se usa para las contraseñas.

<br>

## CREANDO UNA BASE DE DATOS


