# TIPS PARA RESOLUCIONES DE CRIPTOGRAFIA

<br>

Leer detenidamente el enunciado en busqueda de alguna pista sobre el tipo de cifrado que se puede estar usando.

Identificar el tipo de cifrado, comparandolo con los tipos mas comunes o usando herramientas externas.


	“Un famoso emperador nos ha dejado un mensaje, ¿Puedes ver de que se trata?"

        MENSAJE: Crod.
		=

Leyendo el enunciado nos damos cuenta que cuando hablamos de la palabra “emperador” estamos hablando de tiempos muy antiguos, por lo que podemos suponer que estamos tratando con un cifrado de cesar.
Podemos resolverlo a mano o apoyarnos de herramientas como ser [dCode.](https://www.dcode.fr/caesar-cipher)

Solo basta con colocar la palabra a decifrar y por fuerza bruta nos va mostrar las 26 posibles rotaciones.

En caso busquemos codificar solo colocamos las palabras y el numero de separaciones.

<br>

•		Numeros 1-26 	    →			Abecedario

•		Numeros 1/0	        →			Binario

•		Numeros/Letras 	    →			Hexadecimal

•		Mensaje y Llave   	→			Vigenere

•		BASE32/64 	        →			==, =

<br>

Generalmente cuando vemos un igual puede ser base 32 o 64, pero si vemos dos iguales es casi seguro que es un BASE64.

<br>