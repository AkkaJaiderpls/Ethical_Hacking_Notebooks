# ¿Que es la Criptografia?

<br>

Basicamente, la criptografia es la tecnica que protege los documentos y datos.  

Funciona mediante la utilizacion de cifras o codigos para escribir algo secreto en documentos y datos confindenciales que circulan en redes locales o incluso en internet.

<br>

## Usos de la Criptografia

<br>

En la antiguedad la criptografia era usada para ocultar proyectos de guerra de personas que no debian conocerlos. Esto con el fin de que solo las personas autorizadas puedan decifrar el mensaje oculto.

<br>

Conforme las computadoras fueron evolucionando tambien lo hizo la criptografia siendo ampliamente divulgada, empleada y modificada constituyendose luego con algoritmos matematicos.

<br>

## Tipos de Encriptacion

<br>

Cuando hablamos de encriptacion es bueno saber que contamos con dos tipos, la encriptacion simetrica y la encriptacion asimetrica.

Es importante que comprendamos las diferencias entre los metodos de encriptacion simetricos y asimetricos. Los sistemas de encriptacion simetrica son mas eficientes y pueden manejar mas datos. Sin embargo, la administracion de claves con sistemas de encriptacion simetrica es mas problematica y dificil de manejar.

La criptografia asimetrica es mas eficiente en la proteccion de la confiencialidad de pequeñas cantidades de datos y su tamaño y velocidad permiten que sea mas segura para tareas como el intercambio de claves electronicas que viene siendo  una pequeña cantidad de datos en lugar de cifrar grande bloques de datos.

<br>

### * Encriptacion Asimetrica

<br>

Se basa en una codificación de información basada en dos claves: una privada y una pública. De esta manera, el remitente conserva la clave privada y la pública puede entregarse a cualquier receptor. La Clave privada permite descifrar todos los mensajes cifrados con la clave pública; con la pública solo podemos descifrar los mensajes cifrados con la clave privada original. Abordemos mejor el tema de las claves:

Claves Públicas: La clave pública puede encriptar mensajes que sólo se descifran con la clave privada. Esto significa que nadie con la clave pública puede descifrar ese mensaje. Por esto surge la confidencialidad, ya que solo el receptor, podrá interpretar el mensaje.

Claves Privadas: Con la clave privada podemos cifrar información mientras la persona posea el par de la clave pública. Este proceso no brinda la misma confidencialidad, ya que cualquiera con la clave pública podría leer el mensaje, pero le otorga autenticidad a los mensajes. Esto se debe a que solo el que tiene la clave privada puede cifrar la información de la forma en que solo el que tiene la clave pública la puede descifrar.

<br>

### * Encriptacion Simetrica

<br>

Es más básica que la asimétrica, pero juega un papel importante en una comunicación cliente-servidor a través del protocolo HTTPS. La diferencia en este caso radica en que el cifrado simétrico se basa en una sola clave, tanto para hacer el cifrado como para el descifrado. La autenticidad y la confidencialidad no se logran, es mucho más barato y solo implica compartir la clave entre el remitente y el receptor.

