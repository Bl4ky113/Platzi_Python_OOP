# OOP y Python

## Objetivos
- Entender cómo funciona la Programación Orientada a Objetos. OOP.
- Entender cómo medir la eficiencia temporal y espacial de nuestros algoritmos
- Enteder cómo y porqué graficar
- Aprender a resolver problemas de búsqueda, ordenación y optimización.

## OOP

El OOP es una metodológia y forma de hacer el código usando forma de datos complejos que nos permitiran simplificar 
el proceso de desarrollo. Esta forma de datos son clases y objetos. 

Estas clases se usan cómo molde para hacer instancias de objetos. Estos objetos tienen en sí dos tipos de 
datos principales.

- Atributos: toda cosa, caracteristica, variable que tiene el obj
- Metodo: toda acción, function que tiene el obj. Que generalmente afecta o usa los mismos Atributos del obj

A los objetos creados mediante una clase se les conoce cómo instancia. Para saber si un objeto es una instancia de una clase, podemos usar 
el metodo: 

isinstance()

## Descompocición

La Descomposición es la técnica de tener que descomponer diferentes elementos en sus atributos y metodos. & si es necesario tambien 
en otros elementos. 

## Abstracción

La Abstracción es la técnica de observar y modelar un objeto, ya sea físico o virtual, y crear o convertirlo en una clase. Tieniendo en 
cuenta si es una categoria, si es un objeto especifico, si este objeto no tiene mismas caracteristicas que otros, entre otros.

## Encapsulamiento

El encapsulamiento es el proceso de ocultar o no dejar usar, ver o setear valores o functions dentro de las clases. Esto con 
la finalidad de evitar diferentes problemas al realizar el código.

El encapsulamiento en Python tiene 3 niveles:

1. Public, se escribe la variable normalmente (self.var):
	Permite usar, ver y setear la variable dentro y fuera de la Clase y sus subclases

2. Protected, se escribe con un underscore (self._var):]
	Permite usar, ver y setear la variable dentro de la Clase y sus subclases

3. Private, se escribe con un dobleUnderscore (self.__var):
	Permite usar, ver y setear la variable solo dentro de la Clase

Aunque cómo python no esta hecho para manejar este tipo de datos, aun en protected y private se puede acceder a los valores.
Sin embargo no es lo recomendado. Para eso se pueden usar los Getters y Setters

## Getters Y Setters 

Los Getters Y Setters son metodos dentro de los objetos que nos permiten obtener y setear las propiedades privadas o protegidas 
de la Clase. 

Sin embargo estos metodos pueden llegar a ser totalmente no muy escalables cuando tenemos que hacer functions de Getters y Setters para 
100 o 1000 propiedades.

Tambien existen las Deletters y las Docs que eliminan y dan la documentación del elemento, que esta generalmente esta en un 
triple String """   """ en la function de Getter. 

Pero para accerder a cada function se tiene que hacer usando el nombre de cada una, cosa teniosa. Para evitar eso 
Python tiene un decorador de clase que nos permitira hacer lo que queramos con la variable dependiendo de cómo la usemos

## @Property

Con @Property vamos a poder hacer un decoramiento a nuestras funciones Getter, Setter y Deleter. Permitiendo 
tener un código más limpio aunque un poco confuso para los iniciantes.

Para usarlo se hace de la siguiente manera:

@property
def function ():
	""" Docs """
	# Aca vamos a hacer la function de get y le vamos a agregar la documentación del valor que estamos usando.

@function.setter
def function ():
	# Aca vamos a hacer la function de set, es importante poner el mismo nombre de la function getter, punto y setter.

@function.deleter
def deleter_function ():
	# Aca vamos a hacer casi lo mismo que con set.

Es muy importante que se tenga el mismo nombre en los 3 metodos, ya que de lo contrario tendremos que hacerlo 
cómo si fuera nomalmente, usando solo los metodos.

La function de docs viene incluida en los docs de la function Getter

Ahora que lo tenemos listo, vamos a usarlos en el código, que es de una forma muy sencilla, teniendo que solo 
usar normalmente el atributo cómo si no fuera protegido o privado:

	# para usar Getter solo lo usamos cómo una variable con contenido
	obj.atributo >>> valor
	print(obj.atributo) >>> valor

	# para usar setter, vamos a usar el operador de asignación.
	obj.atributo = "perro" >>> "perro"

	# Si por ejemplo, el atributo en su function setter tiene que el valor lo transforma a mayusculas
	# puede quedar así
	obj.atributo = "perro" >>> "PERRO"

	# para usar el Deleter solo lo eliminamos con del
	del obj.atributo >>> None (Borrado)


	

