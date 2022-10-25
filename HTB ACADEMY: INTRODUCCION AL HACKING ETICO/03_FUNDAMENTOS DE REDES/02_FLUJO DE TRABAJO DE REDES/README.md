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

    \begin{table}[]
    \begin{tabular}{lllll}
    dadad & asd   & ada  & ad   & dsad \\
    adsad & adsad & dasd & adad & adsd \\
        &       &      &      &      \\
        &       &      &      &     
    \end{tabular}
    \end{table}