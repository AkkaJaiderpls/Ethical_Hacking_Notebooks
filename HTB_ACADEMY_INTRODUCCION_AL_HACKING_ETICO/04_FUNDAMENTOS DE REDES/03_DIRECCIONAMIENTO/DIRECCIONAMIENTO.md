# CAPA DE RED #

<br>

Las capas de Red (Capa 3) de OSI controla el intercambio de paquetes de datos, ya que estos no pueden enrutarse directamente y, por lo tanto, deben estar provistos de nodos de enrutamiento. Luego estos paquetes de datos se transfieren de un nodo a otro hasta que alcanzan su destino. Por lo general, no hay procesamiento de los datos en las capas por encima de la L3. En base a las direcciones se realiza el enrutamiento y la construccion de las tablas de enrutamient.

En definitiva, se encarga de las siguientes funciones:

<br>

    * Logical Addressing

    * Routing

<br>

Los protocolos se definen en cada capa de OSI, y estos representan una coleccion de reglas para la comunicacion en la capa respectiva. Son transparentes a los protocolos de las capas superiores o inferiores. Algunos protocolos cumplen tareas de varias capas extendiendose a mas de una. Los protocolos mas usados en estas capas son:

<br>

    * IPv4 / IPv6

    * IPsec

    * ICMP

    * IGMP

    * RIP

    * OSPF

<br>

Asegura el enrutamiento de paquetes desde el origen hasta el destino dentro o fuera de una subred. Estas dos subredes pueden tener diferentes esquemas de direccionamiento o tipos de direccionamiento incompatibles. Dado que la comunicacion entre emisor y receptor no siempre es directa es posible debido a las subredes.

<br>

## DIRECCIONES IP ##

<br>

Cada host ubicado en la red puede ser identificado por la llamada direccion Media Acces Control (MAC). Esto permitiria el intercambio de datos dentro de esa red. Si el host remoto esta ubicado en otra red, el conocimiento de la MAC no es suficiente para establecer la conexion. El direccionamiento en internet se realiza a traves del IPv4 y/o IPv6, que compone el Network Addres y el Host Addres.

No importa si se trata de una red mas pequeña, ya sea una red informatica domestica, o de todo internet. La direccion IP asegura la entrega de datos al receptor correcto. POdemos imaginar la representacion de MAC, IPv4 e IPv6 de la siguiente manera:

<br>

    * IPv4 / IPv6, describen la direccion postal unica y el distrito del edificio del destinatario.

    * MAC describe el piso y apartamento exactos del receptor.

<br>

Es posible que una sola direccion IP se dirija a multiples receptor (transmision) o que un dispositivo responda a multiples direcciones IP. Sin embargo, se debe de asegurar que cada direccion IP se asigne solo una vez adentro de la red.

<br>

## ESTRUCTURA IPv4 ##

<br>

El metodo mas comun para asignar direcciones IP es con IPv4, que consiste en un numero binario de 32 bits, combinado en 8 grupos de bits (octetos) que van de 0 a 255. Estos se convierten en numeros decimales mas faciles de leer, separados por puntos y representados como notacion decimal con puntos.

Por lo tanto, una direccion IPv4 puede verse asi:

<br>

| NOTACION    | PRESENTACION                             |
| ----------- | ---------------------------------------- |
| Binario     | 0111 1111.0000 0000.0000 0000.0000 0001  |
| Decimal     | 127.0.0.1                                |

<br>

A cada interfaz de red (tarjeta de red, impresora de red o enrutadores) se les asigna una direccion IP unica.

El formato IPv4 permite 4.294.967.296 direcciones unicas. La direccion IP se divide en un host part y un network part. Los router asignan el host part de la direccion IP en casa o por un administrador. El respectivo network administrador asigna el network part. En internet, lo hace IANA, que asigna y administra las direcciones IP unicas.

En el pasado, aqui se realizaba una clasificacion adicional. Los bloques de red de IP se dividideron en classes A - E. Las diferentes clases diferian en las longitufes respectivas de los recursos compartidos de host y red.

<br>

| CLASS | DIRECCION DE RED | PRIMERA DIRECCION | ULTIMA DIRECCION | MASCARA DE SUBRED | CIDR          | SUBREDES      | IP              |
| ----- | ---------------- | ----------------- | ---------------- | ----------------- | ------------- | ------------- | --------------- |
| A     | 1.0.0.0          | 1.0.0.1           | 127.255.255.255  | 255.0.0.0         | /8            | 127           | 16.777.214 + 2  |
| B     | 128.0.0.0        | 128.0.0.1         | 192.255.255.255  | 255.255.0.0       | /dieciseis    | 16,384        | 16.777.214 + 2  |
| C     | 192.0.0.0        | 192.0.0.1         | 223.255.255.255  | 255.255.255.0     | /24           | 2,097,152     | 254 + 2         |
| D     | 224.0.0.0        | 224.0.0.1         | 239.255.255.255  | MULTIDIFUSION     | MULTIDIFUSION | MULTIDIFUSION | MULTIDIFUSION   |
| E     | 240.0.0.0        | 240.0.0.1         | 255.255.255.255  | RESERVAD          | RESERVADO     | RESERVADO     | RESERVADO       |

<br>

## MASCARA DE SUBRED ##

<br>

Se realiza una separacion adicional de estas clases en pequeñas redes con la ayuda de subnetting. Esta separacion se realiza mediante el netmaskks, que es tan largo como una direccion IPv4. Al igual que con las clases, describe que posiciones de bit dentro de la IP actuan como network part o host part.

<br>

| CLASS | DIRECCION DE RED | PRIMERA DIRECCION | ULTIMA DIRECCION | MASCARA DE SUBRED | CIDR          | SUBREDES      | IP              |
| ----- | ---------------- | ----------------- | ---------------- | ----------------- | ------------- | ------------- | --------------- |
| A     | 1.0.0.0          | 1.0.0.1           | 127.255.255.255  | 255.0.0.0         | /8            | 127           | 16.777.214 + 2  |
| B     | 128.0.0.0        | 128.0.0.1         | 192.255.255.255  | 255.255.0.0       | /dieciseis    | 16,384        | 16.777.214 + 2  |
| C     | 192.0.0.0        | 192.0.0.1         | 223.255.255.255  | 255.255.255.0     | /24           | 2,097,152     | 254 + 2         |
| D     | 224.0.0.0        | 224.0.0.1         | 239.255.255.255  | MULTIDIFUSION     | MULTIDIFUSION | MULTIDIFUSION | MULTIDIFUSION   |
| E     | 240.0.0.0        | 240.0.0.1         | 255.255.255.255  | RESERVAD          | RESERVADO     | RESERVADO     | RESERVADO       |

<br>

## DIRECCIONES DE RED Y PUERTAS DE ENLACE ##

<br>

Las dos IPS adicionales agregados a cada columna de IPs estan reservados para los llamados network address y el broadcast address. Otro papel importante juega el default gateway, que es el nombre de la direccion IPv4 del router que acopla redes y sistemas con diferentes protocolos y gestiona direcciones y metodos de transmision. Es comun para el default gateway que se le asigne la primera o la ultima direccion IPv4 asignable en una subred. Este no es un requisito tecnico, pero es un estandar en entornos de red.

<br>

| CLASS | DIRECCION DE RED | PRIMERA DIRECCION | ULTIMA DIRECCION | MASCARA DE SUBRED | CIDR          | SUBREDES      | IP              |
| ----- | ---------------- | ----------------- | ---------------- | ----------------- | ------------- | ------------- | --------------- |
| A     | 1.0.0.0          | 1.0.0.1           | 127.255.255.255  | 255.0.0.0         | /8            | 127           | 16.777.214 + 2  |
| B     | 128.0.0.0        | 128.0.0.1         | 192.255.255.255  | 255.255.0.0       | /dieciseis    | 16,384        | 16.777.214 + 2  |
| C     | 192.0.0.0        | 192.0.0.1         | 223.255.255.255  | 255.255.255.0     | /24           | 2,097,152     | 254 + 2         |
| D     | 224.0.0.0        | 224.0.0.1         | 239.255.255.255  | MULTIDIFUSION     | MULTIDIFUSION | MULTIDIFUSION | MULTIDIFUSION   |
| E     | 240.0.0.0        | 240.0.0.1         | 255.255.255.255  | RESERVAD          | RESERVADO     | RESERVADO     | RESERVADO       |

<br>

## DIRECCION DE DIFUSION ##

<br>

La tarea de una direccion IP es la de conectar todos los dispositivos en una red entre si. En una red Broadcast existe un mensaje que se transmite a todos los participantes de una red y no requiere de ninguna respuesta. De esta forma, un host encia un paquete de datos a todos en simultaneo, y al hacerlo, comunica la IP que los receptores pueden usar para contactarlo.

<br>

| CLASS | DIRECCION DE RED | PRIMERA DIRECCION | ULTIMA DIRECCION | MASCARA DE SUBRED | CIDR          | SUBREDES      | IP              |
| ----- | ---------------- | ----------------- | ---------------- | ----------------- | ------------- | ------------- | --------------- |
| A     | 1.0.0.0          | 1.0.0.1           | 127.255.255.255  | 255.0.0.0         | /8            | 127           | 16.777.214 + 2  |
| B     | 128.0.0.0        | 128.0.0.1         | 192.255.255.255  | 255.255.0.0       | /dieciseis    | 16,384        | 16.777.214 + 2  |
| C     | 192.0.0.0        | 192.0.0.1         | 223.255.255.255  | 255.255.255.0     | /24           | 2,097,152     | 254 + 2         |
| D     | 224.0.0.0        | 224.0.0.1         | 239.255.255.255  | MULTIDIFUSION     | MULTIDIFUSION | MULTIDIFUSION | MULTIDIFUSION   |
| E     | 240.0.0.0        | 240.0.0.1         | 255.255.255.255  | RESERVAD          | RESERVADO     | RESERVADO     | RESERVADO       |

<br>

## SISTEMA BINARIO ##

<br>

El sistema binario es un sistema numerico que usa solo dos estados diferentes que se representan en dos numeros (0 y 1) opuestos al sistema decimal (0 a 9).

Una direccion IPv4 se divde en 4 octetos, como ya hemos visto. Cada octeto consiste en 8 bis. Cada posicion de un bit en un octeto tiene un valor decimal especifico. Tomemos como ejemplo la siguiente direccion IPv4:

<br>

    * Direccion IPv4: 192.168.10.39

<br>

Aqui hay un ejemplo de como se veria el primer octeto:

<br>

    Values:         128  64  32  16  8  4  2  1
    Binary:           1   1   0   0  0  0  0  0

<br>

Si calculamos la suma de todos estos valores para cada octeto donde el bit se establece en 1, obtenemos la suma:

<br>

| OCTETO | VALORES                          | SUMA |
| ------ | -------------------------------- | ---- |
| 1RO    | 128 + 64 + 0 + 0 + 0 + 0 + 0 + 0 | 192  |
| 2DO    | 128 + 0 + 32 + 0 + 8 + 0 + 0 + 0 | 168  |
| 3RO    | 0 + 0 + 0 + 0 + 8 + 0 + 2 + 0    | 10   |
| 4TO    | 0 + 0+ 32 + 0 + 0 + 4 + 2 + 1    | 39   |

<br>

La representacion completa de binario a decimal se veria asi:

<br>

## IPv4 - NOTACION BINARIA ##

<br>

    Octet:             1st         2nd         3rd         4th
    Binary:         1100 0000 . 1010 1000 . 0000 1010 . 0010 0111
    Decimal:           192    .    168    .     10    .     39

<br>

    * Direccion IPv4: 192.168.10.39

<br>

Esta suma tiene lugar para cada octeto, lo que nos da como resultado una representacion decimal del IPv4 address. La mascara de subred se calcula de la mimsma manera.

<br>

## IPv4 - DE DECIMAL A BINARIO ##

<br>

    Values:         128  64  32  16  8  4  2  1
    Binary:           1   1   1   1  1  1  1  1

<br>

## MASCARA DE SUBRED ##

<br>

    Octet:             1st         2nd         3rd         4th
    Binary:         1111 1111 . 1111 1111 . 1111 1111 . 0000 0000
    Decimal:           255    .    255    .    255    .     0

<br>

    * Direccion IPv4: 192.168.10.39

    * Mascara de Subred: 255.255.255.0

<br>

## CIDR ##

<br>

Classless Inter-Domain Routing (CIDR) es un metodo de representacion y reemplaza la asignacion fija entre la direccion IPv4 y las clases de re (A, B, C, D, E). La division se basa en la mascara de subred o el llamado CIDR Suffix, que permite la division bit a bit del espacio de direcciones IPv4, el CIDR Suffix indica cuantos bits desde el principio del IPv4 pertenecen a la red.

Centremonos en la siguiente direccion IPv4 y mascara de subred como ejemplo:

<br>

    * Direccion IPv4: 192.168.10.39

    * Mascara de Subred: 255.255.255.0

<br>

Ahora toda la representacion de la direccion IPv4 y la mascara de subred se veria asi:

<br>

    * CIDR: 19.168.10.39/24

<br>

El sufijo de CIDR es, por lo tanto, la suma de todos los unos en la mascara de subred.

<br>

    Octet:             1st         2nd         3rd         4th
    Binary:         1111 1111 . 1111 1111 . 1111 1111 . 0000 0000 (/24)
    Decimal:           255    .    255    .    255    .     0

<br>

# DIVISION EN SUBREDES #

La division en un rango de direcciones IPv4 en varios rangos de direcciones mas pequeños se denomina subnetting.

Una subred es un segemtno logico de una red que utiliza direcciones IP con la misma direccion de red. POdemos pensar en una subred como una entrada etiquetada en un pasillo de un edificio grande. POr ejempl, podria ser una puerta de vidrio que separa varios departamentos del edificio de una empresa. Con la ayuda de la division en subredes, podemos crear una subred especifica por nosotros mismos o encontrar el siguiente esquema de la red respectiva:

<br>

    * Network Address

    * Broadcast Address

    * First Host

    * Last Host

    * Number of Hosts

<br>

Tomemos como ejemplo la siguiente direccion IPv4 y mascara de subred:

<br>

    * Direccion IPv4: 192.168.12.160

    * Mascara de Subred: 255.255.255.192

    * CIDR: 192.168.12.160/26

<br>

Ya sabemos que una direccion IP se divide en network part y el host part.

<br>

PARTE DE LA RED

| DETALLES DE       | 1ER OCTETO | 2DO OCTETO | 3ER OCTETO | 4TO OCTETO | DECIMAL |
| ----------------- | ---------- | ---------- | ---------- | ---------- | ------- |
| IPv4              | 1100 0000  | 1010 1000  | 0000 1100  | 1010 0000  | 192.168.12.160/26 |
| Mascara de Subred | 1111 1111  | 1111 1111  | 1111 1111  | 1100 0000  | 255.255.255.192    |
| Bits              | /8         | /16        | /24        | /32        ||

<br>

En la division en subredes, usamos la mascara de subred como plantilla para la direccion IPv4. Desde el primer bit en la mascara de subred, sabemos que bits en la direccion IPv4 no deben de ser cambiados. Estos son fijos y por lo tanto determina la "red principal" en la que se encuentra la subred.

<br>

PARTE AFITRIONA

| DETALLES DE       | 1ER OCTETO | 2DO OCTETO | 3ER OCTETO | 4TO OCTETO | DECIMAL |
| ----------------- | ---------- | ---------- | ---------- | ---------- | ------- |
| IPv4              | 1100 0000  | 1010 1000  | 0000 1100  | 1010 0000  | 192.168.12.160/26 |
| Mascara de Subred | 1111 1111  | 1111 1111  | 1111 1111  | 1100 0000  | 255.255.255.192    |
| Bits              | /8         | /16        | /24        | /32        ||

<br>

Los bits en el host part se pueden cambiar a la primera y ultima direccion. La primera direccion es la network address, y la ultima es la broadcast address para la subred respectiva.

Los network address son vitales para la entrega de paquetes. Si el network address es el mismo para direccion de origen y de destino, el paquete de datos se entrega dentro de la misma subred. Si las direcciones de red son diferentes, el paquete de datos debe enrutarse a otra a traves del default gateway.

<br>

Las mascaras de subred determinan donde se produce esta separacion.

<br>

SEPARACION DE PARTES DE RED Y HOSTS

| DETALLES DE       | 1ER OCTETO | 2DO OCTETO | 3ER OCTETO | 4TO OCTETO | DECIMAL |
| ----------------- | ---------- | ---------- | ---------- | ---------- | ------- |
| IPv4              | 1100 0000  | 1010 1000  | 0000 1100  | 1010 0000  | 192.168.12.160/26 |
| Mascara de Subred | 1111 1111  | 1111 1111  | 1111 1111  | 1100 0000  | 255.255.255.192    |
| Bits              | /8         | /16        | /24        | /32        ||

<br>

Direccion de Red

Entonces, si ahora establecemos todos los bits en 0 en el host part de la direccion IPv4, obtenemos las respectivas subredes network address.

<br>

| DETALLES DE       | 1ER OCTETO | 2DO OCTETO | 3ER OCTETO | 4TO OCTETO | DECIMAL |
| ----------------- | ---------- | ---------- | ---------- | ---------- | ------- |
| IPv4              | 1100 0000  | 1010 1000  | 0000 1100  | 1010 0000  | 192.168.12.160/26 |
| Mascara de Subred | 1111 1111  | 1111 1111  | 1111 1111  | 1100 0000  | 255.255.255.192    |
| Bits              | /8         | /16        | /24        | /32        ||

<br>

DIRECCION DE DIFUSION

Si configuramos todos los bits en el host part de la direccion IPv4 a 1, obtenemos el broadcast address.

<br>

| DETALLES DE       | 1ER OCTETO | 2DO OCTETO | 3ER OCTETO | 4TO OCTETO | DECIMAL |
| ----------------- | ---------- | ---------- | ---------- | ---------- | ------- |
| IPv4              | 1100 0000  | 1010 1000  | 0000 1100  | 1010 0000  | 192.168.12.160/26 |
| Mascara de Subred | 1111 1111  | 1111 1111  | 1111 1111  | 1100 0000  | 255.255.255.192    |
| Bits              | /8         | /16        | /24        | /32        ||

<br>

Como ahora sabemos que las direcciones IPv4 192.168.12.128 y 192.168.12.191 estan asignadas, todas las demas direcciones IPv4 estan en consecuencia entre 192.168.12.129-190. Ahora sabemos que esta subred nos ofrece un total de 64 - 2 (direccion de red y direccion de transmision) o 32 Direcciones IPv4 que podemos asignar a nuestro hosts.

<br>

| HOSPEDADORES          | IPv4           |
| --------------------- | -------------- |
| Direccion de Red      | 192.168.12.128 |
| Primer Anfitrion      | 192.168.12.129 |
| Otros Anfitriones     | ...            |
| Ultimo Anfitrion      | 192.168.12.190 |
| Direccion de Difusion | 192.168.12.191 |

<br>

Division en Subredes mas Pequeñas

Supongamos ahora que nosotros, como administradores, nos han dado la tara de dividir la subred que se nos ha asignado en 4 subredes adicionales. Por lo tanto, es fundamental saber que solo podemos dividir las subredes en funcion del sistema binario.

<br>

| EXPONENTE  | VALOR          |
| ---------- | -------------- |
| 2^0        | = 1            |
| 2^1        | = 2            |
| 2^2        | =4             |
| 2^3        | = 8            |
| 2^4        | = 16           |
| 2^5        | = 32           |
| 2^6        | = 64           |
| 2^7        | = 128          |
| 2^8        | = 256          |

<br>

Por lo tanto podemos dividir en 64 hosts. El exponente de 2^2 en el sistema binario es 4, por lo que averiguamos el numero de bits de la mascara de subred que tenemos que ampliarla. Entonces conocemos los siguientes parametros:

<br>

    * Subred: 192.168.12.128/26

    * Subredes Requeridas: 4

<br>

Ahora aumentamos/expandimos nuestra mascara de subred por 2 bits de /26 a /28 y se ve asi:

<br>

| DETALLES DE       | 1ER OCTETO | 2DO OCTETO | 3ER OCTETO | 4TO OCTETO | DECIMAL |
| ----------------- | ---------- | ---------- | ---------- | ---------- | ------- |
| IPv4              | 1100 0000  | 1010 1000  | 0000 1100  | 1010 0000  | 192.168.12.160/28 |
| Mascara de Subred | 1111 1111  | 1111 1111  | 1111 1111  | 1111 0000  | 255.255.255.240    |
| Bits              | /8         | /16        | /24        | /32        ||

<br>

A continuacion, podemos dividir las 64 direcciones IPv4 que estan disponibles para nosotros en 4 partes:

| NRO DE SUBRED | DIRECCION DE RED | PRIMER ANFITRION | ULTIMO ANFITRION | DIRECCION DE DIFUSION | CIDR |
| ------------- | ---------------- | ---------------- | ---------------- | --------------------- | ---- |
| 1 | 192.168.12.128 | 192.168.12.129 | 192.168.12.142 | 192.168.12.143 | 192.168.12.128/28 |
| 2 | 192.168.12.144 | 192.168.12.145 | 192.168.12.158 | 192.168.12.159 | 192.168.12.144/28 |
| 3 | 192.168.12.160 | 192.168.12.161 | 192.168.12.174 | 192.168.12.175 | 192.168.12.160/28 |
| 4 | 192.168.12.176 | 192.168.12.177 | 192.168.12.190 | 192.168.12.191 | 192.168.12.176/28 |

<br>

## DIVISION MENTAL EN SUBREDES ##

<br>

Puede parecer que hay mucha matematica involucrada en la division de subredes, pero cada octeto se repite y todo es una potencia de dos, por lo que no tiene que haber mucha memorizacion. Lo primero que hay que hacer es identificar que octeto cambia.

<br>

| 1ER OCTETO | 2DO OCTETO | 3ER OCTETO | 4TO OCTETO |
| ---------- | ---------- | ---------- | ---------- |
| /8         | /16        | /24        | /32        |

<br>

Es posible identificar que octeto de la direccion IP puede cambiar recordando estos 4 numeros. Dada que la direccion de red: 192.168.1.1/25, es inmediatamente evidente que 192.168.2.4 no estaria en la misma red porque el /25 significa que solo el cuarto octeto puede cambiar.

La siguiente parte identifica que tan grande puede ser cada subred pero dividiendo ocho por la red y observando el ramainder. Esto tambien se llama Modulo Operation (%) y se utiliza mucho en criptologia. Dado nuestro ejemplo anterior de /25, (25 % 8) seria 1. Esto se debe a que ocho cabe tres veces en 25 (8 * 3 + 24). Queda 1 sobrante, que es el bit de red reservado para la mascara de red.

<br>

| 1ER OCTETO | 2DO OCTETO  | 3ER OCTETO | 4TO OCTETO               |
| ---------- | ----------  | ---------- | ------------------------ |
| 0          | 256         | 2^8        | 256                      |
| 1          | 128         | 2^7        | 256/2                    |
| 2          | 64          | 2^6        | 256/2/2                  |
| 3          | 32          | 2^5        | 256/2/2/2                |
| 4          | 16          | 2^4        | 256/2/2/2/2              |
| 5          | 8           | 2^3        | 256/2/2/2/2/2            |
| 6          | 4           | 2^2        | 256/2/2/2/2/2/2          |
| 7          | 2           | 2^1        | 256/2/2/2/2/2/2/2        |

<br>

Al recordad las potencias de dos a ocho, puede convertirse en un calculo instantaneo. Sin embargo, si se olvida, puede ser mas rapido recordad dividir 256 por la mtad del numero de veces del resto.

La parte complcada de esto es obtener el rango real de direcciones IP porque 0 es un numero y no es nulo en la red. Asi que en nuestro /25 con 128 direcciones IP el primer rango es 192.168.1.0-127. La primera direccion es la red y la ultima es la direccion de transmision, lo que significa que el espacio IP utilizable se convertiria en 192.168.1.1-126. Si nuestra direccion IP cae por encima de 128, entonces el USABLE IP SPACE seria 192.168.129-254(128 IPS es la red y 255 el broadcast).

<br>

# DIRECCIONES MAC #

<br>

Cada host en una red tiene su propio Media Acces Control (MAC) representada en hexadecimal. MAC es la direccion fisica para nuestras interfaces de red. Hay varios estandares para la direccion MAC.

<br>

    * Ethernet (IEEE 802.3)

    * Bluetooth (IEEE 802.15)

    * WiFi (IEEE 802.11)

<br>

Esto se debe a que el MAC address aborda la conexion fisica (tarjetas de red, bluetooth o adpatador WLAN) de un host. Cada tarjeta de red tiene su direccion MAC individual, que se configura una vez en el lado del hardware del fabricante pero siempre se puede cambiar, al menos temporalmente.

Echemos un vistazo a un ejemplo de una direccion MAC de este tipo:

DIRECCION MAC:

<br>

    * DE:AD:BE:EF:13:37

    * DE-AD-BE-EF-13-37

    * DEAD.BEEF.1337

<br>

| REPRESENTACION | 1ER OCTETO | 2DO OCTETO | 3ER OCTETO | 4TO OCTETO | 5TO OCTETO | SEXTO OCTETO |
| -------------- | ---------- | ---------- | ---------- | ---------- | ---------- | ------------ |
| BINARIO        | 1101 1110  | 1010 1101  | 1011 1110  | 1110 1111  | 0001 0011  | 0011 0111    |
| HEXADECIMAL      | DE         | AD         | BE         | EF         | 13         | 37           |

<br>

Cuando se entrega un paquete IP, se debe direccionar en capa 2 a la direccion fisica del host de destino o al ROUTER/NAT, que es el responsable del enrutamiento. Cada paquete tiene una direccion de envio y una direccion de destino.

La primera mitad (3 bytes / 24 bit) es el llamado Organization Unique Identifier (OUI) definida por el Institute of Electrical and Electronics Engineers (IEEE) para los respectivos fabricantes.

<br>

| REPRESENTACION | 1ER OCTETO | 2DO OCTETO | 3ER OCTETO | 4TO OCTETO | 5TO OCTETO | SEXTO OCTETO |
| -------------- | ---------- | ---------- | ---------- | ---------- | ---------- | ------------ |
| BINARIO        | 1101 1110  | 1010 1101  | 1011 1110  | 1110 1111  | 0001 0011  | 0011 0111    |
| HEXADECIMAL      | DE         | AD         | BE         | EF         | 13         | 37           |

<br>

La ultima mitad de la direccion MAC se llama Individual Addres Part o Network Interface Controller (NIC), que asignan los fabricantes. El fabricante establece esta secuencia de bits solo una vez, y por lo tanto, garantiza que la direccion completa sea univoca.

<br>

| REPRESENTACION | 1ER OCTETO | 2DO OCTETO | 3ER OCTETO | 4TO OCTETO | 5TO OCTETO | SEXTO OCTETO |
| -------------- | ---------- | ---------- | ---------- | ---------- | ---------- | ------------ |
| BINARIO        | 1101 1110  | 1010 1101  | 1011 1110  | 1110 1111  | 0001 0011  | 0011 0111    |
| HEXADECIMAL      | DE         | AD         | BE         | EF         | 13         | 37           |

<br>

Si un host con la direccion IP de destino se encuentra en la misma subred, la entrega se realiza directamente a la direccion fisica de la computadora de destino, Sin embargo, si este host pertenece a una subred diferente, la trama de Ethernet se dirige al MAC ADDRESS del router responsable (default gateway). Si la direccion de destino de la trama ETHERNET coincide con la propia capa 2, el enrutador enviara el marco a las capas superiores. Address Resolution Protocol (ARP) se utiliza en IPv4 para determinar las direcciones MAC asociadas con las direcciones IP.

Al igual que con las direcciones IPv4, tambien existen ciertas areas reservadas para la direccion MAC. Estos incluyen, por ejemplo, el rango local para el MAC.

<br>

| ALCANCE LOCAL      |
| ------------------ |
| O 2:00:00:00:00:00 |
| O 6:00:00:00:00:00 |
| O A:00:00:00:00:00 |
| O E:00:00:00:00:00 |

<br>

Ademas, los dos ultimos bits del primer octeto pueden desempeñar otro papel esencial. El ultimo bit puede tener dos estados, 0 o 1 como ya lo sabemos. El ultimo bit identificar la direccion MAC como Unicast(0) o Multicast(1). Con unicast, significa que el paquete enviado llegara solo a un host especifico.

<br>

UNIDIFUSION DE MAC:

| REPRESENTACION | 1ER OCTETO | 2DO OCTETO | 3ER OCTETO | 4TO OCTETO | 5TO OCTETO | SEXTO OCTETO |
| -------------- | ---------- | ---------- | ---------- | ---------- | ---------- | ------------ |
| BINARIO        | 1101 1110  | 1010 1101  | 1011 1110  | 1110 1111  | 0001 0011  | 0011 0111    |
| HEXADECIMAL      | DE         | AD         | BE         | EF         | 13         | 37           |

<br>

Con multicast, el paquete se envia solo una vez a todos los hosts de la red local, que luego deciden si aceptan o no el paquete en funcion de su configuracion. Los multicast address son igual una direccion unica, al igual que la direccion broadcast, que tiene valor de ocho octetos. Broadcast es una red que representa una llamada transmitida, donde los paquetes de datos sse transmiten simultaneamente desde un punto a todos los miembtos de una red. se utiliza principalmente si aun no se conoce la direccon de recepcion del paquete.

<br>

MULTIDIFUSION MACS

| REPRESENTACION | 1ER OCTETO | 2DO OCTETO | 3ER OCTETO | 4TO OCTETO | 5TO OCTETO | SEXTO OCTETO |
| -------------- | ---------- | ---------- | ---------- | ---------- | ---------- | ------------ |
| BINARIO        | 0000 0001  | 0000 0000  | 0101 1110  | 1110 1111  | 0001 0011  | 0011 0111    |
| HEXADECIMAL      | FF         | FF         | FF         | FF         | FF         | FF           |

<br>

El penultimo bit del primer octeto identifica si se trata de un global OUI, definido por el IEEE o una direccion MAC locally administred.

<br>

GLOBAL SI

| REPRESENTACION | 1ER OCTETO | 2DO OCTETO | 3ER OCTETO | 4TO OCTETO | 5TO OCTETO | SEXTO OCTETO |
| -------------- | ---------- | ---------- | ---------- | ---------- | ---------- | ------------ |
| BINARIO        | 1101 1100  | 1010 1101  | 1011 1110  | 1110 1111  | 0001 0011  | 0011 0111    |
| HEXADECIMAL      | DC         | AD         | BE         | EF         | 13         | 37           |

<br>

ADMINISTRADO LOCALMENTE

| REPRESENTACION | 1ER OCTETO | 2DO OCTETO | 3ER OCTETO | 4TO OCTETO | 5TO OCTETO | SEXTO OCTETO |
| -------------- | ---------- | ---------- | ---------- | ---------- | ---------- | ------------ |
| BINARIO        | 1101 1110  | 1010 1101  | 1011 1110  | 1110 1111  | 0001 0011  | 0011 0111    |
| HEXADECIMAL      | DE         | AD         | BE         | EF         | 13         | 37           |

<br>

# IPv6 Addresses #

<br>

Es el sucesor de IPv4. A diferencia de IPv4 la direccion de IPv6 es de 128, un poco latfo a los prefix que identifican las partes del host y de la red. La IANA es responsable de asignar direcciones IPv4 e IPv6 y sus partes de red asociadas. A largo plazo, se espera que IPv6 reemplace completamente a IPv4, que todavia se usa predominantemente en internet, sin embargo IPv4 e IPv6 pueden estar disponibles simultaneamente.

IPv6 sigue consistentemente el principio end-to-end y proporciona direcciones IP de acceso publico para cualquier dispositivo sin necesidad de NAT. En consecuencia, una interfaz puede tener varias direcciones IPv6 y existen direcciones IPv6 especiales a las que se le asigna varias interfaces.

<br>

IPv6 es un protocolo con muchas novedades, que ademas tiene muchas otras ventajas frente a IPv4:

<br>

    * Espacio de direcciones mas grandes

    * Autoconfiguracion de direcciones (SLAAC)

    * Multiples direcciones IPv6 por interfaz

    * Enrutamiento mas rapido

    * Cifrado de extremo a extremo (IPsec)

    * Paquete de datos de hasta 4 GByte

<br>

| CARACTERISTICAS           | IPv4               | IPv6                         |
| ------------------------- | ------------------ | ---------------------------- |
| Longitud de Bits          | 32 bits            | 128 bits                     |
| Capa OSI                  | Capa de Red        | Capa de Red                  |
| Rango de Direccionamiento | ~4.3 mil trillones | ~340 undecillones            |
| Representacion            | Binario            | Hexadecimal                  |
| Notacion de Prefijo       | 10.10.10.0/24      | fe80::dd80:b1a9:6687:2d3b/64 |
| Direccionamiento Dinamico | DHCP               | SLAAC/DHCPv6                 |
| IPsec de                  | Opcional           | Obligatorio                  |

<br>

Hay cuatro tipos de diferentes direcciones IPv6:

<br>

| TIPO | DESCRIPCION |
| ---- | ----------- |
| UNICAST | Direcciones para una unica interfaz |
| ANYCAST | Direcciones para multiples interfaces, donde solo una de ellas recibe el paquete
| MULTICAST | Direcciones para multiples interfaces, donde todas reciben el mismo paquete
| BROADCAST | No existen y se realiza con direcciones multicast.

<br>

# SISTEMA HEXADECIMAL #

<br>

El sistema hexadecimal se utiliza para hacer que la representacion binaria sea mas legible y comprendible. Solo podemos mostrar 10 (0-9) estados con el decimal y 2 (0/1) con el sistema binario usando un solo caracter. A diferencia del sistema binario y decimal, podemos usar el sistema hexadecimal para mostrar 16 (0-F) estados con un solo caracter.

| DECIMAL | HEXADECIMAL | BINARIO |
| ------- | ----------- | ------- |
| 1       | 1           | 0001    |
| 2       | 2           | 0010    |
| 3       | 3           | 0011    |
| 4       | 4           | 0100    |
| 5       | 5           | 0101    |
| 6       | 6           | 0110    |
| 7       | 7           | 0111    |
| 8       | 8           | 1000    |
| 9       | 9           | 1001    |
| 10      | A           | 1010    |
| 11      | B           | 1011    |
| 12      | C           | 1100    |
| 13      | D           | 1101    |
| 14      | E           | 1110    |
| 15      | F           | 1111    |

<br>

Veamos un ejemplo con un IPv4, como la direccion IPv4 (192.168.12.160) se veria en representacion hexadecimal.

<br>

| REPRESENTACION | 1ER OCTETO | 2DO OCTETO | 3ER OCTETO | 4TO OCTETO |
| -------------- | ---------- | ---------- | ---------- | ---------- |
| Binario | 1100 0000 | 1010 1000 | 0000 11000 | 1010 0000 |
| Hexadecimal | C0 | A8 | 0C | A0 |
| Decimal | 192 | 168 | 12 | 160 |

<br>

Por su longitud, la direccion de un IPv6 esta representada en notacion hexadecimal. Por lo tanto, los 128 bits estan dividios en 8 bloques de 16 bits (o 4 Hexadecimales). Los 4 numeros hexadecimales estan agrupados y separados por dos puntos (:) en lugar de un simple punto (.) como en IPv4. Para simplificar la notacion, dejamos de lado al menos 4 ceros en los bloques y los representamos con dos puntos (::).

Una direccion IPv6 puede verse asi:

<br>

    * IPv6 completo: fe80:0000:0000:0000:dd80:b1a9:6687:2d3b/64

    * IPv4 corto: fe80::dd80:b1a9:6687:2d3b/64

<br>

Una direccion IPv6 consta de dos partes:

<br>

    * Network Prefix (Parte de la Red)

    * Interface Identifier (tambien llamado suffix, parte del host)

<br>

Los prefijos de red idntifican a la red, subred o rango de direcciones. Las interfaces de red se forman a partir de las 48 bit MAC direcciones de la interfaz y se convierten en una direccion de 64 bit en el proceso. La longitud del prefijo determinado es de /64. Sin embargo, otros prefijos tipicos son /32, /48 y /56. Si queremos usar nuestras redes, obtenemos un prefijo mas corto (por ejemplo /56) que los /64 de nuestro proveedor.

En RFC 5952, se definio la notacion de IPv6 antes mencionada:

    * Todos los caracteres alfabeticos se escriben en minusculas.

    * Todos los ceros inciales de un bloque siempre se omiten

    * Uno o mas bloques consecutivos de 4 ceros se pueden acortar con ::

    * El acortamiento a dos puntos (::) solo se puede realizar comenzando desde la izquierda.
