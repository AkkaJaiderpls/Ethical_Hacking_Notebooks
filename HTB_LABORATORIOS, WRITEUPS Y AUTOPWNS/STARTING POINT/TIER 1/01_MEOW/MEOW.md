# MEOW #

<br>

## RECONOCIMIENTO ##

<br>

Una vez conectado correctamente nuestro VPN procedemos a hacer un **PING** al objetivo para ver si tenemos conexion.

Luego de obtener respuesta al PING podemos determinar que efectivamente, tenemos una conexion estable.

Ademas de determinar que tenemos una conexion estable, con ayuda del TTL podemos ver que sistema operativo esta corriendo la maquina objetivo

<br>

    - Un TTL inferior a 64 nos indica que estamos ante una maquina LINUX

    - Un TTL inferior a 128 nos indica que estamos ante una maquina WINDOWS

<br>

## ESCANEO ##

<br>

Para proceder al siguiente paso vamos a realizar un escaneo a los puertos abiertos de la maquina para determinar que procesos se estan ejecutando.

Podemos usar la herramienta de **NMAP** acompañada del parametro **-sV** para detectar las versiones y la descripcion de los servicios que puedan estar corriendo, seguido de ello indicamos la IP del objetivo.

<br>

    sudo nmap -sV {IP_OBJETIVO}

<br>

Finalizado el escaneo identificamos que el puerto 23 esta abierto corriendo el servicio de **TELNET**. TELNET es un protocolo antiguo utilizado para el manejo remoto de equipos a traves de la red. Cuando un objetivo esta corriendo este servicio nos indica que esta esperando una peticion de conexion de algun equipo en la red. Usualmente este servicio esta configurado con una combinacion de usuario/contraseña para incrementar la seguridad.

Necesitamos de estos credenciales para poder continuar ya que no existen otros servicios que podamos explotar.

<br>

## OBTENIENDO EL ACCESO ##

<br>

En algunas ocasiones debido a errores en configuracion, algunas cuentas puede llegar a dejar la contraseña en blanco para mas facilidad en el acceso. Esto es un gravisimo error en los dispositivos, ya que deja la puerta a ataques de fuerza-bruta, donde el atacante intenta ingresar usando una lista de nombres de usuario sin contraseñas.

Algunos de los usuarios tipicos en configuraciones incorrectas son:

<br>

    * admin

    * administrator

    * root

<br>

Una manera directa de iniciar es usando estos usuarios y dejando la contraseña en blanco de manera manual cuando el host nos la pida. Si esto no funcionara, podriamos utilizar un script para automatizar este proceso indicando una lista de nombres y contraseñas. Este tipo de procesos se conocen como diccionarios y contienen nombres tipicos de personas, abreviaciones, o datos de filtraciones. Por ahora vamos a intentarlo con nombres de usuario de manera manual.

<br>

No tuvimos suerte con los dos primeros, pero no debemos sentirnos mal, es esencial ser persistente. Intentemos con uno mas.

<br>

Listo! Logramos iniciar sesion en la maquina objetivo. Ahora podemos echar un vistazo a los directorios y movernos por ahi usando el comando **ls**.

<br>

En este caso, nuestro objetivo es la **flag.txt**, y varia de laboratorio en laboratorio.

Podemos leer el archivo usando el comando **cat** y colocar la flag en la plataforma para demostrar que logramos vulnerar la maquina.