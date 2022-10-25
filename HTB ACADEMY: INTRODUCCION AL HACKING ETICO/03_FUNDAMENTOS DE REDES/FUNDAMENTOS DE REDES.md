# RESUMEN DE REDES #

<br>

Una red permite que dos computadoras se comuniquen entre si. Hay una amplia gama de topologias(mesh/tree/stars), medios (Ethernet/fibra/coaxial/inalambrico), y protocolos (TCP/UDP/IPX) que se puede utilizar para facilitar el acceso a la red. Como profesionales de la seguridad, es importante comprender las redes porque cuando la red falla, el error puede ser silencioso, lo que hace que nos podamos perder de algo.

Configurar una red grande y plana no es extremadamente dificil y puede ser confiable, al menos, operativamente. Sin embargo, una red plana es como construir una casa en un terreno y considerarla segura solo porque tiene una cerradura en la puerta.

Al crear muchas redes mas pequeñas y hacer que se comuniquen podemos agregar algunas capas de defensa. Moverse alrededor de una red no es dificil, pero hacerlo de forma rapida y silenciosa si lo es, estas capas de defensa puedem llegar a ralentizar a los atacantes. Volviendo al escenrio de la casa, veamos los siguientes ejemplos:

<br>

## EJEMPLO NUMERO 1 ##

<br>

La creacion de redes mas pequeñas y la colocacion de listas de control de acceso a su alrededor es como colocar una valla alrededor de los limites de la propiedad, creando pundos de entrada y salida especificos. Si, un atacante podria saltar la cerca, pero esto parece muy sospechoso y no es comun, lo que nos permite detectarlo rapidamente como actividad maliciosa. ¿Por que la red de la impresora se esta comunicando con los servidores a traves de HTTP?

<br>

## EJEMPLO NUMERO 2 ##

<br>

Tomarse el tiempo para mapear y documentar el proposito de cada red es como colocar luces alrededor de la propiedad, asegurandose de que podamos ver toda actividad. ¿Por que la red de la impresora se comunica con internet?

<br>

## EJEMPLO NUMERO 3 ##

<br>

Tener arbustos alrededor de las ventanas es un elemento disuasorio para las personas que intentan abrir las ventanas. Al igual que los sistemas de deteccion de intrusos como Suricata o Snort son un impedimento para ejecutar un escaneo de redes. ¿Por que se origino un escaneo de puertos desde la red de la impresora?

Estos ejemplo pueden llegar a sonar tontos y es de sentido comun impedir que una impresora haga todo lo anterior. Sin embargo, si la impresora esta en una "red plana/24" y obtiene una direccion DHCP, puede ser un desafio el poder imponerle algun tipo de restriccion.

<br>

## STORY TIME: UNA SUPERVISION DE PENTESTERS ##

<br>

La mayoria de las redes utilizan una subred /24, tanto que muchos Pentesters van a buscar configurar directo a esta mascara (255.255.255.0) casi sin verificar.

La red /24 permitr que las computadoras se comuniquen entre si siempre que los primeros tres octetos de una direccion IP sean iguales (por ejemplo, 192.168.1.xxx). Establecer la mascara de subred en /25 divide este rango por la mitad, y la computadora podra hablar solo con las computadoras en "su mitad". Hemos visto informes de pruebas donde el pentester afirmo que un controlador de dominio estaba fuera de linea cuando en realidad este estaba en una red diferente. La estructura de la red era algo como esto:

<br>

    * Puerta de enlace del servidor: 10.20.0.1/25

    * Controlador de dominio: 10.20.0.10/25

    * Puerta de enlace del cliente: 10.20.0.129/25

    * Estación de trabajo del cliente: 10.20.0.200/25

    * Pentester IP: 10.20.0.252/24 (Configurada la puerta de enlace en 10.20.0.1)

<br>

## INFORMACION BASICA ##

<br>

Veamos el siguiente diagrama de alto nivel de como puede funcionar una configuracion de trabajo desde casa.

<br>

![](https://academy.hackthebox.com/storage/modules/34/redesigned/net_overview.png)

<br>

Todo internet se basa en muchas redes subdivididas, tal como se muestra en el ejemplo tenemos nuestra "Home Network" y la "Company Network". Podemos imaginar el NETWORKING como la entrega de correos o paquetes enviados por una computadora y recibidos por otra.

<br>

Supongamos que imaginamos como escenario que queremos visitar el sitio web de una empresa desde nuestra casa. En ese caso, intercambiaremos datos con el sitio web de la empresa ubicado en sus servidores.

Al igual que con el envio de cartas de correspondencia, nosotros conocemos la direccion del domicilio a donde deben de llegar estas cartas.

En este caso la direccion del domicilio hace referencia a la direccion del sitio web o URL (Uniform Resource Locator) que ingresamos en nuestro navegador, esta direccion es conocida tambien FQDN (Fully Qualified Domain Name).

La URL y la FQDN cuentan con una diferencia:

<br>

    * Un FQDN (www.hackthebox.eu) solo especifica la direccion principal.

    * Una URL ("https://www.hackthebox.eu/example?floor=2&office=dev&employee=17") tambien especifica el piso, la oficina, el buazon y el correspondiente empleado a quien va destinado el paquete.

<br>

El hecho es que conocemos la direccion, pero no la ubicacion geografica exacta. En esta situacion, la oficina de correos (o sea, nuestro ROUTER) puede determinar la ubicacion exacta con ayuda de nuestro proveedor de internet, para luego reenviar los paquetes a la ubicacion deseada.

El proceso es sencillo, nuestra oficina de correos reenvia nuestros paquetes a la oficina de correos principal, que es representada por nuestro Proveedor de Internet o Internet Service Provider (ISP).

Tan pronto como enviemos nuestro paquete y este llega a la oficina de correos principal. Esta oficina tiene el tabajo traducir el Domain Service Name (DNS) a las coordeanadas geografica correspondientes (IP). Finalizada esta cadena ahora ya conocemos la ubicacion exacta de la direccion, por tanto nuestro paquete se enviara directamente alli mediante un vuelo directo a traves de nuestra oficina postal principal.

Despues de que el servidor web haya recibido nuestro paquete con la solicitud de como es que se ve su sitio web, el servidor nos devuelve un paquete con los datos para la respectiva presentacion del sitio web a traves de nuestro router con la direccion de retorno (nuestra IP).

<br>

## PUNTOS EXTRAS  TOMAR EN CUENTA ##

<br>

En el diagrama anterior, esperamos que la red de la empresa que se muestra consista en cinco redes separadas.

    1. El servidor web debe de estar en una DMZ (Zona Desmilitarizada) porque los clientes pueden iniciar comunicaciones con su sitio web, lo que hace que sea mas probable que se vea comprometido. Si este estuviera colocado en una red separada, los administradorres puede colocar protecciones de red entre el servidor web y otros dispositivos.

    2. Las estaciones de trabajo deben de estar en su propia red, y en un mundo perfecto, cada estacion de trabajo deberia tener una regla de firewall basada en hosts que le impida comunicarse con otras estaciones de trabajo. Si una estacion de trabajo esta en la misma red que un servidor, los ataquees de red como spoofing o man in the middle pueden convertirse en un problema mucho mayor.

    3. El Switch y el Router deben de estar en una "red de administracion". Esto evita que las estaciones de trabajo husmeen en cualquier comunicacion entre estos dispositivos. A menudo, en pruebas de penetracion se puede llegar a ver un OSPF (Open Shortest Path First). Dado que el router no tenia una Trusted Network, basicamente, cualquiera en la red interna podria haber enviado un anuncion malicioso y realizado un man in the middle contra cualquier red,

    4. Los telefonos IP deben de estar en su propia red. En cuanto a la seguridad, esto es para evitar que las computadoras puedan espiar la comunicacion. Ademas de la seguridad, los telefonos son unicos en el sentido de que su latencia/retraso no es significativa. Incluso ubicarlos en su propia red puede ser de ayuda para que los administradores de red prioricen su trafico para evitar una alta latencia mas facilmente.

    5. Las impresoras deben de estar en su propia red. Esto puede llegar a sonar extraño, pero es casi imposible asegurar a una impresora. Debido a vomo funciona windows, si una impresora le dice a una computadora que se requiere una autenticacion durante un trabajo de impresion, esa computadora intentara una autenticacion NTLMv2, lo que puede conducir a un secuestro de contraseñas. Ademas, estos dispositivos son excelentes para la persistencia y, en general, se les envia toneladas de informacion confidencial.