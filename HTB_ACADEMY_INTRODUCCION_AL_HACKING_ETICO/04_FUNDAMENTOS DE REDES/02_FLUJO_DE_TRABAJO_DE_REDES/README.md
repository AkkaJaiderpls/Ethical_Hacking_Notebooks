# MODELOS DE REDES #

<br>

Existen dos modelos de redes que describen la comunicación y la transferencia de datos de un host a otro, llamados ISO/OSI model y el TCP/IP model.

Esta es una representacion simplificada de los llamados layers o capas que representan los bits transferidos en contenido legible para nosotros.

<br>

![](https://academy.hackthebox.com/storage/modules/34/redesigned/net_models4.png)

<br>

## EL MODELO OSI ##

<br>

El modelo OSI, a menudo se denomina modelos de capas ISO/OSI, es un modelo de referencia que se puede usar para describir y definir la comunicacion entre sistemas. El modelo de referencia tiene 7 capas individuales, cada una con tareas claramente separadas.

El termino OSI representa al modelo Open Systems Interconnection, publicada por la International Telecommunication Union (ITU) y el International Organization for Standarization (ISO). Por lo tanto, los modelos OSI tambien se conocen como modelo de capas ISO/OSI.

<br>

## EL MODELO TCP/IP ##

<br>

TCP/IP (Transmission Control Protocol / Internet Protocol) es un termino generico para muchos protocolos de red. Los protocolos son responsables de la comunicación y el transporte de datos en internet. Internet se basa enteramente en la familia de protocolos TCP/IP. Sin embargo, TCP/IP no solo se refiere a esos dos protocolos, sino que generalmente se usa como un termino generico para toda una familia de protocolos.

Por ejemplo, ICMP (Internet Control Message Protocol) o UDP (User Datagram Protocol) pertenecen a la familia de protocolos. La familia de protocolos proporciona las funciones necesarias para transportar y conmutar paquetes de datos en una red privada o publica.

<br>

## ISO/OSI FRENTE A TCP/IP ##

<br>

TCP/IP es un protocolo de comunicación que permite a los hosts conectarse a Internet. Se refiere a la Transmission Control Protocol utilizada en y por apliaciones en internet. En contraste con OSI, permite aligerar las reglas que se deben de seguir, siempre que se sigan pautas generales.

OSI, por otro lado, es una puerta de enlace de comunicación entre la red y los usuarios finales. El modelo OSI generalmente se denomina modelo de referencia porque es mas antiguo. Tambien es conocido por su estricto protocolo y limitaciones.

<br>

## TRANSFERENCIA DE PAQUETES ##

<br>

En un sistema en capas, los dispositivos en una capa intercambian datos en un formato diferente llamado PROTOCOL DATA UNIT (PDU). Por ejemplo, cuando queremos navegar por un sitio web en la computadora, el software del servidor remoto primero pasa los datos solicitados a la capa de aplicacion.

<br>

![](https://academy.hackthebox.com/storage/modules/34/redesigned/net_models_pdu2.png)

<br>

Durante la transmision, cada capa agrega un header hacia la capa PDU superior, que controla e identifica el paquete, Este proceso se conoce como encapsulation. El encabezado y los datos juntos forman la PDU para la siguiente capa. El proceso continua hasta la Capa Fisica o la capa de Red, donde los datos se transmiten al receptor. El receptor invierte el proceso y desempaqueta los datos en cada capa con la informacion del encabezado. Despues de eso, la aplicacion finalmente usa los datos. Este proceso continuda hasta que todos los datos hayan sido enviados y recibidos.

<br>

![](https://academy.hackthebox.com/storage/modules/34/packet_transfer.png)

<br>

Para nosotros, como pentesters, ambos modelos de referencia son utiles. Con TCP/IP podemos entender rapidamente como se establece toda la conexion, y con OSI, podemos desmontarlo pieza por pieza y analizarlo en detalle. Esto sucede a menudo cuando podemos escuchar e interceptar trafico de red especifico.

Entonces tenemos que analizar este trafico en consecuencia, entrando mas a detalle en el modulo de Analisis de Trafico de Red. Por tanto, debemos de familiarizarnos con ambos modelos de referencia y entenderlos de la mejor manera posible.

<br>

El objetivo en la definicion de ISO/OSI estandar fue crear un modelo de referencia que permita la comunicacion de diferentes sistemas tecnicos a traves de varios dispositivos y tecnologias proporcionando compatibilidad.

El uso del modelo OSI se basa jeraquicamente entre si para lograr este objetivo. Estas capas representan fases en el establecimiento de cada conexion por donde pasaran los paquetes enviados.

<br>

| CAPA                                  | FUNCION                                            |
| ------------------------------------- | ---------------------------------------------------|
| 7. Aplicacion                         | Entre otras cosas, esta capa controla la entrada y salida de datos y proporciona las funciones de la aplicación.                              |
| 6. Presentacion                       | La tarea de la capa de presentación es transferir la presentación de datos dependiente del sistema a una forma independiente de la aplicación.|
| 5. Sesion                             | La capa de sesión controla la conexión lógica entre dos sistemas y previene, por ejemplo, fallas en la conexión u otros problemas.            |
| 4. Transporte                         | La capa 4 se utiliza para el control de extremo a extremo de los datos transferidos. La capa de transporte puede detectar y evitar situaciones de congestión y segmentar flujos de datos.      |
| 3. Red                                | En la capa de red, las conexiones se establecen en redes de conmutación de circuitos y los paquetes de datos se reenvían en redes de conmutación de paquetes. Los datos se transmiten a través de toda la red desde el remitente hasta el receptor.                                     |
| 2. Enlace de Datos                    | La tarea central de la capa 2 es permitir transmisiones confiables y sin errores en el medio respectivo. Para ello, los flujos de bits de la capa 1 se dividen en bloques o tramas.  Personal                                     |
| 1. Fisica                             |Las técnicas de transmisión utilizadas son, por ejemplo, señales eléctricas, señales ópticas u ondas electromagnéticas. A través de la capa 1, la transmisión se realiza en líneas de transmisión alámbricas o inalámbricas.                                      |

<br>

Las capas 2-4 son orientadas a transporte, y las capas 5-7 son orientadas a la apliacion. En cada capa, se realizan tareas definidas con precision y las interfaces con las capas vecinas se describen con precision. Cada capa ofrece servicios para el uso de la capa directamente encima de ella. Pra que estos servicios esten disponibles, la capa utiliza los servicios de la de la capa anterior y luego realiza las tareas de su capa.

Si dos sistemas se comunican las 7 capas del modelo OSI se ejecutan 2 veces, ya que tanto el emisor como el receptor deben tener en cuenta el modelo de capas.

Cuando una aplicacion envia un paquete al otro sistema, el sistema trabaja las capas que se muestran desde la 7 hasta la 1, y el sistema receptor desmapquete el paquete recibido de la capa 1 hasta las 7.

<br>

# EL MODELO TCP/IP #

<br>

El modelo TCP/IP tambien es un modelo de referencia en capas, representa los dos protocolos Transmission Control Protocol (TCP) e Internet Protocol (IP). IP se encuentra dentro de la capa de red en el modelo OSI, mientras que TCP se encuentra en la capa de transporte.

<br>

| CAPA             | FUNCION                     |
| ---------------- |-----------------------------|
| 4. Aplicacion    | La capa de aplicacion permite que las aplicaciones accedan a los servicios de otras capas y define los protocolos que utilizan las aplicaciones para intercambiar datos.
| 3. Transporte    | La capa de transporte es responsable de proporcionar servicios de sesion (TCP) y datagramas (UDP) para la capa de aplicacion.
| 2. Internet    | La capa de internet es responsable de las funciones de direccionamiento, empaquetado y enrutamiento del host.
| 1. Link    | La capa de enlace es responsable de colocar los paquetes TCP/IP en el medio de la red y recibir los paquetes correspondientes del medio de la red. TCP/IP esta diseñado para funcionar independiente del metodo de acceso a la red, el formato de la trama y el medio.

<br>

Con TCP/IP, cada aplicacion puede transferir e intercambiar datos a traves de cualquier red, y no importa donde se encuenre el receptor. IP asegura que el paquete de datos llegue a su destino, y TCP controla la trasnferencia de datos y asegura la conexion entre el flujo de datos y la aplicacion. La principal diferencia entre TCP/IP y OSI es el numero de capas, donde algunas se han combinado.

<br>

![](https://academy.hackthebox.com/storage/modules/34/redesigned/net_models4.png)

<br>

Las tareas mas importantes de TCP/IP son:

<br>

| TAREA                | PROTOCOLO         | DESCRIPCION |
| -------------------- | ------------------| ----------- |
| Logical Addressing   | IP                | Debido a que hay muchos hosts en diferentes redes, es necesario estrucutrar la topologia de la red y el direccionamiento logico. Dentro de TCP/IP, IP asume el direcconamiento logico de redes y nodos. Los paquetes de datos solo llegan a la red donde se supone que deben de estar. Los metodos para hacerlo son network classes, subnetting y CIDR.            |
| Routing              | IP                | Para cada paquete de datos, el siguiente nodo se determina de camino desde el emisor hasta ek receptor. De esta menera, un paquete de datos se enruta a su receptor, incluso si el remitente desconce su ubicacion .            |
| Error & Control Flow | TCP               | El remitente y el receptor estan frecuentemente en contacto entre si a traves de una conexion virtual. Por lo tanto, los mensajes de control se envian continuamente para verificar si la conexion aun esta establecida.             |
| Application Support  | TCP               | Los puertos TCP y UDP forman una abstraccion de software para distinguir aplicaciones especificas y sus enlaces de comunicacion.              |
| Name Resolution      | TCP               | DNS proporciona la resolucion de nombre a traves de nombres de dominios totalmente certificados (FQDN) en direcciones IP, lo que nos permite llegar al host deseado con el nombre especificado en internet.             |