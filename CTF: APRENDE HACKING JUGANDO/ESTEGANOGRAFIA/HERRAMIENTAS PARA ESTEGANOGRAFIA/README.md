# Herramientas para Esteganografia

<br>

En el caso de esteganografia contamos con muchas herramientas tanto en linea como en GitHub, veamos algunas de ellas.

<br>

## Analisis completo de una Imagen con Forensically

<br>

Forensically es una herramienta en linea para el analisis de imagenes, permite realizar cosas como extraer la metadata, realizar un analisis de errores entre otras funciones.

La parte que mas me gusta de esta herramienta es el Error Level Analysys donde podemos encontrar partes que hayan sido manipuladas de alguna manera, aunque tambien hay muchas funciones que vale la pena ver.

<br>

## Revisar la metadata de una imagen con Metadata2go

<br>

La Exif Data es un tipo de metadata propia de las imagenes, en algunos casos pueden revelar el modelo de telefono celular o camara con la que fue tomada, asi como informacion asociada al dueño del dispositivo.

Comenzaremos dirigiendonos a la pagina		https://www.metadata2go.com/		en ella vamos a adjuntar la foto que querramos analizar, al cabo de un rato podremos ver todos los metadatos que fueron encontrados en la fotografia.

<br>

## Revisar el tipo de archivo original con CheckFileType 

<br>

Una forma comun de ocultar informacion es cambiando la extension de un archivo, de esta manera un archivo puede aparentar por ejemplo ser una imagen corrupta.

Se puede revisar el tipo de archivo original en el siguiente enlace		https://www.checkfiletype.com/		basta con subir el archivo en cuestion y la pagina va determinar la extension original.


<br>

## Revisar cabeceras Hexadecimales con OnlineHexEditor

<br>

Si quiseramos revisar si alguna imagen contiene algun tipo de archivo adjunto podemos apoyarnos de herramientas como		https://www.onlinehexeditor.com/		para ello subimos nuestra imagen y esperamos el resultado, deberiamos ver algo como esto.

<br>

## Encontrar mensajes ocultos en una imagen con OpenStego

<br>

A diferencia de la anterior herramienta con OpenStego podemos extraer informacion sin usar filtros de imagen, basta con colocar la imagen y una contraseña que en la mayoria de los caso esta vacia.

Ademas, podemos ocultar nuestros propios mensajes asi como cifrarlos con contraseñas.

Para instalarlo basta con ir a su repositorio y copiarlo		https://github.com/syvaidya/openstego/releases		

<br>

## Encontrar mensajes ocultos en una imagen con Stegsolve

<br>

Es una herramienta codificada en Java bastante util para esteganografia de imagenes, nos va permitir visualizar los distintos planos de colores de una imagen para descubrir mensaes ocultos. Podemos conseguirla del siguiente repositorio.

https://github.com/eugenekolo/sec-tools/blob/master/stego/stegsolve/stegsolve/stegsolve.jar

Para instalar esta herramienta se requiere instalar Java previamente.

<br>

## Encontrar mensajes ocultos en Audios con Audacity

<br>

Como ya conocemos, la esteganografia tambien puede ser usadas en audios para ocultar mensajes, para este trabajo nostros vamos a utilizar una herramienta gratuita llamada Audacity que nos va permitir revisar las ondas de audios en busqueda de informacion.

Para descargarlo basta con ir a su pagina oficial y seguir los pasos		https://www.audacityteam.org/download/linux/		

<br>

## Comprobar el tamaño de los archivos 

<br>

Mas que una herramienta, revisar el tamaño nos puede hacer darnos cuenta que un archivo de texto que aparenta estar vacio puede contener informacion oculta, es muy importante siempre revisarlo.

<br>