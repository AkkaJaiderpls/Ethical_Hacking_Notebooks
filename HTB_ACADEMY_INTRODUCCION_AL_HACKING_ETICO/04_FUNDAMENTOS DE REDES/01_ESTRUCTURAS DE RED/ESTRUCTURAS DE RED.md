# TIPOS DE REDES #

<br>

Cada red es estructurada de manera diferente y puede configurarse individualmente. Por esta razon, los desarrollados TYPES y TOPOLOGIES se pueden utilizar para categorizar estas redes. Al leer sobre todos los tipos de redes, puede ser un poco sobrecargado de informacion, ya que algunos tipos de redes incluyen hasta el rango geografico. Rara vez escuchamos algunas de las terminologias en la practica, por lo que solo nos centraremos en Terminos Comunes y Terminos de Libros.

<br>

TERMINOLOGIA COMUN

| TIPOS DE REDES                         | DEFINICION                                         |
| -------------------------------------- | ---------------------------------------------------|
| Red de Area Amplia (WAN)               | Internet                                           |
| Red de Area Local (LAN)                | Redes Internas (Ej: Hogares u Oficinas)            |
| Red de Area Local Inalambrica (WLAN)   | Redes Internas accesibles a traves de Wi-Fi        |
| Red Privada Virtual (VPN)              | Conecta Multiples sitios de red a uno LAN          |

<br>

## WAN ##

<br>

La WAN (red de area amplia) se conoce como EL INTERNET. Cuando se trata de equipos de red, a menudo tendremos una direccion WAN y una direccion LAN. La WAN es la direccion a la que generalmente se accede por internet. Dicho esto, no es inclusivo solo para internet; Una WAN es solo una gran cantidad de LAN unidas. Muchas empresas grandes o agencias gubernamentales tendran una "WAN Interna" (Tambien conocida como INTRANED, Red Airgap, etc). En terminos generales, la forma principal de identificar si una red es una WAN es usar un protocolo de enrutamiento , especifico de WAN como BGP y si el squema IP en uso no esta dentro de RFC 1918 (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16).

<br>

## LAN/WLAN ##

<br>

Las LAN (red de area local) y las WLAN (red de area local inalambrica) normalmente asignaran direcciones IP para el uso local (RFC 1918, 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16). En algunos casos, como algunas universidades u hoteles, es posible que se le asigne una IP enrutable (Internet) al unirse a su LAN, pero eso es mucho menos comun. No nada diferente entre una LAN o WLAN, aparte de que las WLAN introducen la capacidad de transmitir datos sin cables. Es principalmente una designacion de seguridad.

<br>

## VPN ##

<br>

Hay tres tipos de Virtual Private Network (VPN), pero los tres tienen el mismo objetivo de hacer que el usuario se sienta como si estuviera conectado a una red diferente.

<br>

## VPN DE SITIO A SITIO ##

<br>

Tanto el cliente como el servidor son dispositivos de red, normalmente Routers o Firewalls y comparten rangos de red completos. Eso se usa mas comunmente para unir las redes de la empresa a traves de internet, lo que permite que varias ubicaciones se comuniquen a traves de internet como si fueran locales.

<br>

## VPN DE ACCESO REMOTO ##

<br>

Esto implica que la computadora del cliente crea una interfaz que se comporta como si estuviera en la red de un cliente. Hack The Box utiliza OpenVPN, que hace un adaptador TUN que permite acceder a los laboratorios. Al analizar estas VPN, una pieza importante a considerar es la tabla de enrutamiento que se crea al unirse a la VPN. Si la VPN solo crea rutas para redes especificas (por ejemplo, 10.10.10.0/24), esto se denomina como Split-Tunnel VPN, lo que significa que la conexion a internet no sale de la VPN. Esto es excelente para Hack The Box porque vrinda acceso al laboratorio sin la preocupacion de privacidad de monitorear su conexion a Internet. Sin embargo, para una empresa, por lo general las VPN no son ideales porque si la maquina se infecta con malware, es probable que los metodos de deteccion basados en red no funcionen a medida que ese trafico sale de internet.

<br>

## VPN SSL ##

<br>

Esta es esenciamente una VPN que se realiza adentro de nuestro navegador web y se esta volviendo cada vez mas comun a medida de que los navegadores se hacen capaz de cualquier cosa. Por lo general, estos transmitiran aplicaciones o sesiones escritorio completas al navegador web.

<br>

TERMINOLOGIA DE LIBROS

| TIPOS DE REDES                            | DEFINICION                                         |
| ----------------------------------------- | ---------------------------------------------------|
| Red de Area Global (GAN)                  | Red Mundial (Internet)                             |
| Red de Area Metropolitana (MAN)           | Redes Regional (Multiples LAN)                     |
| Red de Area Personal Inalambrica (WPAN)   | Redes Personal                                     |

<br>

## SIN EMBARGO... ##

<br>

Una red mundial como la Internet es conocida como un Global Area Network (GAN). Sin embargo, Internet no es la unica red informatica de este tipo. Las empresas internacionales tambien mantienen redes aisladas que abarcan varios WAN.

GAN utiliza la infraestructura de fibra de vidrio de las redes de area amplia para interconectarlas mediante cables submarionos internacionales o la transmisiones por satelite.

<br>

## MAN ##

<br>

Metropolitan Area Network (MAN) es una red de telecomunicaciones de banda ancha que conecta varios LAN en la proximidad geografica. Por lo general, se trata de sucursales individuales de una empresa conectadas a una MAN a taves de lineas arrendadas. Se utilizan enrutadores de alto rendimiento y conexiones de alto rendimiento basadas en fibras de vidrio que permiten un rendimiendo de datos significativamente mayor que internet. La velocidad de transmision entre dos nodos remotos es comparable a la comunicacion dentro de una LAN.

<br>

## PAN/WPAN ##

<br>

Los dispositivos finales modernos como telefonos inteligentes, tabletas, computadoras o portatiles de escritorios se pueden conectar ad hoc para formar una red que permita el intercambio de datos. Esto se puede hacer por cable en forma de Personal Area Network (PAN).

La variante inalambrica Wireless Personal Area Network (WPAN) se basa en tecnologias Bluetooth o USB inalambrico. Una WPAN que se establece a traves de Bluetooth se llama Piconet. Las PAN y WPAN generalmente se extienden solo unos metros, y por lo tanto, no son adecuados para conectar dispositivos en habitaciones separadas o incluso edificios.

En el contexto del Interner de las Cosas (IoT), los dispositivos usan WPAN para comunicarse con aplicaciones de control. Protocolos como Insteon, Z-Wave y ZigBee se diseñaron explicitamente para hogares inteligentes y domotica.

<br>

## TOPOLOGIA DE REDES ##

<br>

Una topologia de red es un arreglo tipico fisico o logico de dispositivos. Las computadoras son hosts como clientes y servidores, que utilizan activamente la red. Tambien incluyen componentes de red como Switches, Bridges y Routers, que veremos mas adelante.

Tienen una funcion de distribucion y aseguran que todos los hosts de la red puedan establecer una conexion logica entre si. La topologia de la red determina los componentes a utilizar y los metodos de acceso a los medios de transmision.

La topologia fisica define como se conectan los dispositivos.
Para medios conductivos o de fibra de vidrio, esto se refiere al plan de cableado, las posiciones de los nodos, y las conexiones entre nodos.

Por lo contrario, la topologia logica es como actuan las señales en los medios de la red o como se transmiten los datos a traves de de la red desde un dispositivo hasta la conexion fisica de los dispositivos.

<br>

Podemos dividir toda el area de topologia de la red tres areas:

<br>

1. Conexiones

<br>


| WIRED CONNECTIONS                         | WIRELESS CONNECTIONS                               |
| ----------------------------------------- | ---------------------------------------------------|
| Cableado Coaxial                          | WiFi                                               |
| Cableado de Fibra de Vidrio               | Celular                                            |
| Cableado de Par Trenzado                  | Satelite                                           |
| y otros                                   | y otros                                            |

<br>

2. Nodos - Controlador de Interfaz de Red (NIC)

<br>

| REPETIDORES       | CONCENTRADORES   | REPETIDORES    | INTERRUPTORES |
| ------------------| -----------------| -------------- | ------------- |
| Enrutador/Modem   | Pasarelas        | Cortafuegos    |               |

<br>

Los nodos de red son los "Transmission Medium's Connection Points", aquellos transmisores y receptores de señales electricas, opticas o de radio en el medio. Un nodo puede estar conectado a una computadora.

<br>

3. Clasificaciones

<br>

Podemos imaginar una topologia como una forma virtual o estructura de la red. Esta forma no corresponde necesariamente a la disposicion fisixa real de los dispositivos en la red. Por lo tanto, estas topologias puede ser fisicas o logicas. Por ejemplo, las computadoras en una LAN pueden estar en un circulo en un dormitorio, pero es muy poco probable que tenga una topologia de anillo real.

Las topologias de red se dividen en los siguientes ocho tipos:

<br>

    * Punto a Punto

    * Estrella

    * Malla

    * Hibrido

    * Autobus

    * Anillo

    * Arbol

    * Cadena de Margaritas

<br>

## PUNTO A PUNTO ##

<br>

La topolia de red mas simple con una conexion dedicada entre dos hosts es la point-to-point. En esta topologia solo existe un vinculo fisico directo entre dos hosts. Estos dos dispositivos pueden utilizar estas conexiones para la comunicacion mutua,

La topologia punto a punto es el modelo mas basico de la telefonia traficional y no debe confundirse con P2P (Peer-to-Peer).

<br>

![](https://academy.hackthebox.com/storage/modules/34/redesigned/topo_p2p.png)

<br>

## AUTOBUS ##

<br>

En la topologia de bus todos los hosts estan conectados a traves de un medio de transmision. Cada host tiene acceso al medio de transmision y las señales que se transmiten a traves de el. No hay un componente de red central que controle los procesos en el. El medio de transmision para eso puede ser por ejemplo un cable coaxial.

<br>

![](https://academy.hackthebox.com/storage/modules/34/redesigned/topo_bus.png)

<br>

## ESTRELLA ##

<br>

La topologia en estrella es un componente de red que mantiene una conexion con todos los hosts. Cada host esta conectado a un "Central Network Component" a traves de un enlace separado. Suele ser un router, un hub o un switch. Estos manejan el una funcion de tipo forwarding donde los paquetes de datos son recibidos y enviados a quien le corresponde. El trafico de datos en el componente de red central puede ser alto, ya que todos los datos y conexiones pasan por el.

<br>

![](https://academy.hackthebox.com/storage/modules/34/redesigned/topo_star.png)

<br>

## ANILLO ##

<br>

La topologia de anillo fisica es tal que cada host o nodo esta conectado al anillo con dos cables:

<br>

    * Uno para las señales que entran

    * El otro para las señales que salen

<br>

Esto significa que llega un cable a cada host y sale otro. La topologia de anillo normalmente no requiere de un componente de red activo. El control y el acceso al medio de transmision esta regulado por un protocolo al que se adhieren todas las estaciones.

<br>

## MALLA ##

<br>

Las estructuras malladas no tienen una topologia fija. Posee dos estructuras basicas, el fully meshed y el partially meshed.

Cada host esta conectadoa a todos los demas en una fully meshed. Esto significa que cada host esta entrelazados entre si. Esta tecnica se utiliza principalmente en WAN o MAN para garantizar una alta fiabilidad y ancho de banda.

En esta configuracion, los nodos de red importantes, como los enrutadores, podrian conectarse en red. Si un enrutador falla, los demas pueden seguir operando sin problema.

En el partially meshed structure, los puntos finales estan conectados por una sola conexion. En este tipo de topologia de red, los nodos especificos se conectan exactamente a otro nodo y algunos se conectan a dos o mas nodos en una conexion de punto a punto.

<br>

![](https://academy.hackthebox.com/storage/modules/34/redesigned/topo_mesh.png)

<br>

## ARBOL ##

<br>

La topologia de arbol es una topologia de estrella extendida. Es especialmente util cunado se combinan varias topologias. Esta topologia se usa a menido, por ejemplo, en edificios de empresas grandes.

<br>

![](https://academy.hackthebox.com/storage/modules/34/redesigned/topo_tree.png)

<br>

## HIBRIDO ##

<br>

Las redes hibiridas combinan dos o mas topologias para que la red resultante no presente ninguna topologia estandar.

<br>

![](https://academy.hackthebox.com/storage/modules/34/redesigned/topo_hybrid.png)

<br>

## CADENA DE MARGARITAS ##

<br>

En la topologia de cadena margarita, varios hosts se conectan colocando un cable de un nodo a otro.

Dado que esto crea una cadena de conexiones, tambien se conoce como configuracion de conexion en cadena en la que varios componentes de hardware estan conectados en serie. Este tipo de red se encuentra a menudo en la tecnologia de automatizacion (CAN).

<br>

![](https://academy.hackthebox.com/storage/modules/34/redesigned/topo_daisy-chain.png)

<br>

# PROXIES #

<br>

Muchas personas tienen diferentes opiniones sobre lo que es un proxy:

<br>

    * Los profesionaes de seguridad saltan a HTTP Proxies (BurpSuite) o pivotean con un SOCKS/SSH Proxy (Chisel, Ptunnel, Sshuttle).

    * Los desarrolladores web utilizan proxies como Cloudflare o ModSecurity para bloquear el trafico malicioso.

    * La gente promedio puede pensar que se utiliza para ocultar su ubicacion y acceder al catalogo de Netflix de otro pais.

    * Las fuerzas del orden a menudo atribuyen a los proxies a actividades ilegales.

<br>

No todos los ejemplo anteriores son correctos. Un proxy es cuando un dispositivo o servicio se encuentra en medio de una conexion y actua como mediador. Los mediadores ven la informacion critica, porque al estar en medio pueden ver el contenido del trafico.

Volviendo a la pregunta anterior, la persona promedio tiene una idea equivocada de los que es un proxy, ya que lo mas probable es que este usando un VPN para ofuscar su ubicacion, que tecnicamente no es un proxy.

Si tienes problemas para recordar esto, los proxies casi siempre operan en la capa 7 del modelo OSU. Hay muchos tipos de servicios proxy, pero los principales son:

<br>

    * Dedicated Proxy / Forward Proxy

    * Reverse Proxy

    * Transparent Proxy

<br>

## PROXY DEDICADO / PROXY DE REENVIO ##

<br>

Los Forward Proxy, es lo que la mayoria de la gente imagina que es un proxy. Un proxy de reenvio es cuando un cliente realiza una solicitud a una computadora y esa computadora lleva acabo la solicitud.

Por ejmplo, en una red corporativa, es posible que las computadoras confidenciales no tengan acceso a internet. Para que puedan acceder a un sitio web estas deben pasar por un proxy (o filtro web). Esta puede ser una linea de defensa increiblemente poderosa contra el malware, ya que no solo necesita eludir el filtro web (facil), sino que tambien deben usar un C2 no tradicional (una forma en el que el malware recibe informacion de tareas). Si la organizacion solo utiliza Firefox, la probabilidad de obtener malware compatible con proxy es improbable.

Los navegadores web como Internet Explorer, Edge o Chrome obedecen la configuracion de "Proxy del Sistema" de manera predeterminada. Si el malware utiliza WinSock (API nativa de Windows), es probable que reconozca el proxy sin codifiacion adicional. Firefox no utiliza WinSock y en su lugar utiliza libcurl, lo que le permite usar el mismo codigo en cualquier sistema operativo. esto significa que el malware tendria que entrar a firefox y ectraer a configuracion del proxy, lo que es muy poco probable que haga el malware.

Alternativamente, el malware podria usar DNS como un mecanismo c2, poero si una organizacion esta monitoreando DNS (lo que se hace facilmente usando Sysmon), este tipo de trafico es detectado rapidamente.

Otro ejemplo de Forward Proxy es BurpSuite, ya que la mayoria de las personas lo utilizan para reenviar solicitudes HTTP. Sin embargo, esta aplicacion es la navaja suiza de los Proxies HTTP y se puede configurar incluso para ser un proxy inverso o transparente.

<br>

![](https://academy.hackthebox.com/storage/modules/34/redesigned/forward_proxy.png)

<br>

## PROXY INVERSO ##

<br>

Como habras adivinado, un reverse proxy, es el reverso de un Forward Proxy. en lugar de estar diseñado para filtrar las solicitudes salientes, filtra las entrantes. El objetivo mas comun con un Reverse Proxy, es escuchar una direccion y reenviarla a una red cerrada.

Muchas organizaciones usan Cloudflare porque tiene una red robusta que soporta la mayoria de los ataques DDOS. Al usar Cloudflare, las organizaciones tienen una forma de filtrar la cantidad (y el tipo) de trafico que se envia a sus servidores.

Los pentesters configuran proxies inversos en los puntos finales infectados. El punto final infectado escuchara un puerto y enviara a cualquier cliente que se conecte al puerto de regreso del atacante a traves del punto final infectado. Esto es util para eludir los firewalls o evadir el registro. Las organizaciones pueden tener un IDS (Intrusion Detection System), viendo solicitudes web externas. Si el atacante obtiene acceso a la organizacion a traves de SSH el atacante puede enviar solicitues a trabes de SSH y avadir el IDS.

Otro proxy inverso comun es ModSecurity un Web Aplication Firewall (WAF). Los firewalls de aplicaciones web inspeccionan las solicitudes en busca de contenido malicioso y blqouean la la solicitud en el caso de que sea maliciosa. Cloudflare tambien puede actuar como un WAF, pero para ello requiere de permitirle el acceso al trafico HTTPS, lo que es posible que algunas organizaciones no deseen.

<br>

![](https://academy.hackthebox.com/storage/modules/34/redesigned/reverse_proxy.png)

<br>

## PROXY (NO) TRANSPARENTE ##

<br>

Todos estos servicios de proxy actuan de manera transparente o no transparente.

Con un proxy transparente, el cliente no sabe de su existencia. El proxy transparente intercepta las solicitudes de comunicación del cliente a Internet y actua como una instancia sustituta.

Si es un proxy no transparente, debemos ser infromados sobre su existencia. Para este proposito, nosotros y el software que queremos usar debe de tener una configuracion especial que garantiza que el trafico de internet se dirija primero al proxy.