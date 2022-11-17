# HERRAMIENTAS PARA ESTEGANOGRAFIA #

<br>

En el caso de esteganografia contamos con muchas herramientas tanto en linea como en GitHub, veamos algunas de ellas.

<br>

## ANALISIS COMPLETO DE UNA IMAGEN CON [Forensically](https://29a.ch/photo-forensics/) ##

<br>

Forensically es una herramienta en linea para el analisis de imagenes, permite realizar cosas como extraer la metadata, realizar un analisis de errores entre otras funciones.

La parte que mas me gusta de esta herramienta es el Error Level Analysys donde podemos encontrar partes que hayan sido manipuladas de alguna manera, aunque tambien hay muchas funciones que vale la pena ver.

<br>

## REVISAR LA METADATA DE UNA IMAGEN CON [Metadata2go](https://www.metadata2go.com/) ##

<br>

La Exif Data es un tipo de metadata propia de las imagenes, en algunos casos pueden revelar el modelo de telefono celular o camara con la que fue tomada, asi como informacion asociada al dueño del dispositivo.

Comenzaremos dirigiendonos a la pagina	en ella vamos a adjuntar la foto que querramos analizar, al cabo de un rato podremos ver todos los metadatos que fueron encontrados en la fotografia.

<br>

## REVISAR EL TIPO DE ARCHIVO ORIGINAL CON [CheckFileType](https://www.checkfiletype.com/) ##

<br>

Una forma comun de ocultar informacion es cambiando la extension de un archivo, de esta manera un archivo puede aparentar por ejemplo ser una imagen corrupta.

Se puede revisar el tipo de archivo original en el siguiente enlace		basta con subir el archivo en cuestion y la pagina va determinar la extension original.


<br>

## Revisar cabeceras Hexadecimales con [OnlineHexEditor](https://www.onlinehexeditor.com/) ##

<br>

Si quiseramos revisar si alguna imagen contiene algun tipo de archivo adjunto podemos apoyarnos de herramientas como para ello subimos nuestra imagen y esperamos el resultado, deberiamos ver algo como esto.

<br>

## ENCONTRAR MENSAJES OUCLTOS EN UNA IMAGEN CON [OpenStego](https://github.com/syvaidya/openstego/releases) ##

<br>

A diferencia de la anterior herramienta con OpenStego podemos extraer informacion sin usar filtros de imagen, basta con colocar la imagen y una contraseña que en la mayoria de los caso esta vacia.

Ademas, podemos ocultar nuestros propios mensajes asi como cifrarlos con contraseñas.

Para instalarlo basta con ir a su repositorio y copiarlo

<br>

## ENCONTRAR MENSAJES OCUTOS EN UNA IMAGEN CON [Stegsolve](https://github.com/eugenekolo/sec-tools/blob/master/stego/stegsolve/stegsolve/stegsolve.jar) ##

<br>

Es una herramienta codificada en Java bastante util para esteganografia de imagenes, nos va permitir visualizar los distintos planos de colores de una imagen para descubrir mensajes ocultos. Podemos conseguirla del siguiente repositorio.

Para instalar esta herramienta se requiere instalar Java previamente.

<br>

## ENCONTRAR MENSAJES OCUTOS EN UNA IMAGEN CON [Steghide](https://github.com/StefanoDeVuono/steghide.git) ##

<br>

Steghide nos va permitir encubrir registros confidenciales dentro de una imagen o sonido con una frase de contraseña.


Podemos encontrar esta herramienta en su repositorio de GitHub.

<br>

## ENCONTRAR MENSAJES OCULTOS EN AUDIOS CON [Audacity](https://www.audacityteam.org/download/linux/) ##

<br>

Como ya conocemos, la esteganografia tambien puede ser usadas en audios para ocultar mensajes, para este trabajo nostros vamos a utilizar una herramienta gratuita llamada Audacity que nos va permitir revisar las ondas de audios en busqueda de informacion.

Para descargarlo basta con ir a su pagina oficial y seguir los pasos.

<br>

## COMPROBAR EL TAMAÑO DE LOS ARCHIVOS ##

<br>

Mas que una herramienta, revisar el tamaño nos puede hacer darnos cuenta que un archivo de texto que aparenta estar vacio puede contener informacion oculta, es muy importante siempre revisarlo.

<br>