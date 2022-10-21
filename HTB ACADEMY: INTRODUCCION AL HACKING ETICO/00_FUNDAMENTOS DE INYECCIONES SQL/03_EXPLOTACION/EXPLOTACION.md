# ENUMERACION DE BASE DE DATOS #

<br>

En las secciones anteriores, aprendimo sobre diferentes consultas SQL en MySQL e inyecciones de SQL y como usarlas. Esta seccion pondra en uso todo la aprendido con el objetvo de recopilar datos usando consultas SQL dentro de inyecciones SQL.

<br>

## HUELLA DIGITAL DE MYSQL ##

<br>

Antes de enumerar la base de datos, generalmente necesitamos identificar el tipo de DBMS con el que estamos tratando. Esto se debe a que cada DBMS tiene consultas diferentes, sabiendo a que DBMS nos enfrentamos nos ayudara a saber que consultas usar.

Como suposicion inicial, si el servidor web que vemos en la respuesta HTTP es Apache o Nginx, es una buena suposicion de que el servidor web que se esta ejecutando en Linux, por lo que es probable que el DBMS sea MYSQL. Lo mismo aplica a Microsoft DBMS si el servidor web es un IIS, por lo que probablemente sea MSSQL. Sin embargo, esta es una suposicion descabellada ya que muchas otras bases de datos se pueden usar para el sistema operativo o el servidor web. Entonces, hay diferentes consultas que podemos probar para identificar el tipo de base con la que estamos tratando.

Mientras cubrimos MYSQL vamos a ver su huella digital. Las siguientes consultas y salidas nos diran que estamos tratando con MYSQL.

<br>

    *---------------------------------------------------------------------------------------------------------------------------------------------------------------------*
    | CARGA UTIL 	    | CUANDO USAR 	                                  | RENDIMIENTO ESPERADO 	                                  | SALIDA INCORRECTA                 |
    *-------------------*-------------------------------------------------*-----------------------------------------------------------------------------------------------* | SELECT@@version   | Cuando tenemos la salida de consulta completa   | Versión de MySQL 'es decir 10.3.22-MariaDB-1ubuntu1'      | En MSSQL devuelve la version      |
    |                   |                                                 |                                                           | Error en otros DBMS.              |
    *-------------------*-------------------------------------------------*-----------------------------------------------------------*-----------------------------------*
    | SELECT POW(1,1)   | Cuando solo tenemos salida numerica             | 1                                                         | Error con otros DBMS              |
    *-------------------*-------------------------------------------------*-----------------------------------------------------------*-----------------------------------*
    | SELECT SLEEP(5)   | Ciego / Sin Salida                              | Retrasa la respuesta de la pagina por 5 segundos          | No retrasa la salida en otro DBMS |
    *-------------------*-------------------------------------------------*-----------------------------------------------------------*-----------------------------------*

<br>

Como