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

El encapsulamiento es el proceso de ocultar o no dejar usar, ver o setear valores o functions dentro de las clases. 
Esto con la finalidad de evitar diferentes problemas al realizar el código y hacer una programación defensiva.

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

## Herencia

Es la técnica de reutilizar código en la que nos permite crear una jerarquia de clases, con la mayor o la padre llamada SUPER clase y 
sus hijos llamada sub clases.

Estas van a poder compartir las mismas caracteristicas con variaciones menores en cada subclase. Permitiendonos, dependiendo del 
encapsulamiento, acceder a los metodos y atributos de la SUPER clase

Para hacer herencia en Python es solo hacer uso de:

class name_class (SUPER_class):
	# class content

En el constructor __init__, vamos a tener que declarar los valores que necesite la SUPER clase, ya que si no lo hacemos nos va a 
dar error. Esto se hace usando la función super() y accediendo a el constructor:

def __init__ (param):
	super().__init__(param)

con Super() podemos acceder diferectamente a las propiedades y metodos de la Super Clase, pero no es tan necesario ya que, pues somos el 
hijo o subclase de esa misma clase, es mas que obvio que podemos acceder a esas cosas ya.

Se puede hacer diferentes tipos de herencias:

- Directa:
	Super Clase tiene una o varias sub Clases
- Multinivel:
	Sub Clase se convierte en una Super Clase y tiene una o varias sub Clases
- Multiple:
	Una Sub Clase es hecha apartir de dos o más Super Clases

## Polimorfismo

Es una extención de la herencia, en donde las subclases pueden cambiar su comportamiento, o más especificamente, los 
metodos. Generalmente los más módificados con los metodos Getter, Setter, ... etc. 

En python solo se debe rescribir el metodo. Pero en otros lenguajes se debe declarar con 
@override. Cómo en Java.

## Intro Complejidad Algoritmica
Que es?

- comparación de la eficiencia de un algoritmo.
	Poder aproximar y desarrollar un algoritmo que nos de un resultado de un problema.
- complejidad temporal vs complejidad espacial
	Poder determinar si el algoritmo tiene una complejidad de tiempo o de memoria. Generalmente es temporal.
- Podemos definirla cómo T(n)
	Para definir la complejidad simplemente vamos a tener que hacer nuestra function T, con un input n y el resultado 
	es su complejidad

Para medir la complejidad temporal vamos a hacer aproximaciones:
- Cronometrar el tiempo que se demora en correr el algoritmo.
	Esto depende del computador, de lo que este haciendo el computador, no es lo mejor pero es un aproximamiento
- Contar los pasos del algoritmo.
	Contar cada paso de cada operacion del algoritmo
- Contar los pasos del algoritmo, cuando nos estemos acercando a el infinito.
	Esto es lo más viable para la mayoria de algoritmos

## Conteo Abstracto de una Operación

Es la sola acción de contar los pasos de un algoritmo. Contando cada operación y así. 
En los loops vamos a contar los pasos de este y multiplicarlos por el número de veces que 
el loop se repite. 

Cuando tenemos un loop dentro de otro loop, es lo mismo que si ocurriera una potenciación. 

Cuando contemos esto, vamos a poder formar un polinomio, ya sea con varias o ninguna variables mátematicas (x, y, z).

Pero esto nos va a dar las bases para pensar y contar los pasos cuando estos se acercen a lo infinito, haciendo uso de...

## Big O Notation

El crecimiento asintótico o Big O Notation es una notación mátematica que nos va a permitir mirar que va a ser 
el comportamiento de cualquier algoritmo que nosotros lleguemos a hacer.

Tambien para optimizar nuesto analisis del algoritmo al usar el Big O Notation:
- No importan las variaciones pequeñas, loops con números pequeños no nos van a importar tanto.
- Debemos enfocarnos en lo que le pasa a el problema cuando su tamaño se acerca a el infinito
- Podemos reviar el mejor de los casos, promedio y el peor de los casos
- Cuando realizamos el proceso de Big O Notation, siempre vamos a elegir a el resultado mayor

Para hacer el proceso de Big O Notation, vamos a tomar el algoritmo, 
mirar que loops o iteraciones tiene. Pueden ser con while, for, recursivity. 
Generalmente estos algoritmos tienen uno o más inputs.

Mirar cual va a ser el comportamiento de esté input. Este comportamiento puede que sea:
- Constante (2): 
	El valor es igual durante todo el algoritmo, TOP tier de algoritmo
- Lineal (n): 
	El valor avanza en linea recta, proporcionalmente crece el input. Buen Tier, pero puede mejorar
- Logaritmico (log n):
	El valor avanza en una forma logaritmica, primero mucho pero luego se estabiliza su crecimiento. TOP Tier de algoritmo
- Log. Lineal (n log n):
	El valor avanza en una forma logaritmica con una constante. Empieza a ser malo.
- Polinomial (n ** 2):
	El valor es potenciado por 2. Es malo
- Exponencialmente (2 ** n): 
	El valor avanza en potencias de 2. Es muy malo
- Factorialmente (n!):
	El valor avanza en su factorial. Literalmente infinito
	
Algunas de las iteraciones pueden interactuar entre sí, para eso se 
debe hacer diferentes operaciones cómo la suma o multiplicación de estas.
Del resultado de estas solo vamos a tomar el mayor.

Simplemente wow, esto me encanta, aunque no lo he probado aún.

## Por que Graficar?

El graficar es una excelente herramienta que nos va a poder ayudar en direfentes cosas, cómo:
- Reconocimeinto de Patrones
- Predicción de una serie
- Simplifica la interpretación y las conclusiones acerca de los datos
- Presentar datos de una mejor forma
- Poder ver si nuestro programa esta funcionando bien
- El tener los datos de una forma visual nos ayuda a entenderlos mejor

Para hacer graficas en Python podemos usar la libreria de Bokeh.
Bokeh es una libreria que nos va a permitir hacer mil y un tipos de graficas 
con los datos que tengamos.

Aunque deberiamos ver primero que tipo de grafica deberiamos usar para 
nuestros datos.

Bokeh nos permite convertir nuestras graficas cómo archivos HTML, png, u otros, pero 
en algunos debemos hacer más pasos que en otros.
