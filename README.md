# Ejercicios de Probabilidad Resueltos

A continuación se presentan los enunciados de los ejercicios resueltos en este repositorio. Cada ejercicio tiene su propio script de Python (`ejercicio_XX.py`) donde se desarrolla la solución paso a paso.

## Unidad 5: Experimentos aleatorios y espacio muestral

**Ejercicio 1**  
Se lanzan tres monedas justas al aire.  
a) Determine el espacio muestral del experimento.  
b) ¿Cuál es la probabilidad de obtener exactamente dos caras?  
c) ¿Cuál es la probabilidad de obtener al menos una cruz?

**Ejercicio 2**  
En una urna hay 5 bolas rojas, 3 azules y 2 verdes. Se extraen dos bolas sin reemplazo.  
a) ¿Cuántos elementos tiene el espacio muestral?  
b) Calcule la probabilidad de que ambas bolas sean del mismo color.

**Ejercicio 3**  
Un código de acceso consta de 4 dígitos (del 0 al 9) que pueden repetirse.  
a) ¿Cuántos códigos diferentes son posibles?  
b) ¿Cuál es la probabilidad de que un código elegido al azar tenga todos sus dígitos diferentes?  
c) ¿Cuál es la probabilidad de que el código termine en un número par?

## Unidad 6: Conceptos y axiomas de probabilidad

**Ejercicio 4**  
En una facultad, el 60% de los estudiantes estudia Ingeniería de Datos, el 30% estudia Ingeniería de Sistemas y el resto otra carrera. Además, se sabe que el 40% de los estudiantes de Ingeniería de Datos usa transporte público, el 50% de los de Sistemas lo usa y el 20% de los de otras carreras también.  
a) Si se selecciona un estudiante al azar, ¿cuál es la probabilidad de que use transporte público?  
b) ¿Cuál es la probabilidad de que sea de Ingeniería de Datos dado que usa transporte público?

**Ejercicio 5**  
Se lanza un dado justo de 6 caras dos veces. Sea A el evento “la suma de los dos lanzamientos es 7” y B el evento “el primer lanzamiento es 4”.  
a) Calcule P(A), P(B) y P(A ∩ B).  
b) Verifique si A y B son independientes usando los axiomas de probabilidad.

## Unidad 7: Probabilidad condicional y eventos independientes

**Ejercicio 6**  
En una empresa, el 70% de los empleados tiene computador portátil, el 40% tiene tableta y el 25% tiene ambos dispositivos.  
a) Si se elige un empleado al azar y se sabe que tiene portátil, ¿cuál es la probabilidad de que también tenga tableta?  
b) ¿Los eventos “tener portátil” y “tener tableta” son independientes? Justifique.

**Ejercicio 7**  
Una máquina produce piezas. La probabilidad de que una pieza sea defectuosa es 0.05. Se toman tres piezas al azar (con independencia).  
a) Calcule la probabilidad de que exactamente una sea defectuosa.  
b) Calcule la probabilidad de que al menos una sea defectuosa.

## Unidad 8: Teorema de Bayes y ejercicios 2° corte

**Ejercicio 8**  
Tres máquinas (M1, M2, M3) producen el 50%, 30% y 20% de la producción total de una fábrica, respectivamente. Los porcentajes de piezas defectuosas de cada máquina son 2%, 3% y 5% respectivamente.  
a) Si se selecciona una pieza al azar y resulta defectuosa, ¿cuál es la probabilidad de que haya sido producida por la máquina M1?  
b) ¿Cuál es la probabilidad de que una pieza no sea defectuosa?

**Ejercicio 9**  
Una prueba para detectar una enfermedad tiene una sensibilidad del 95% (detecta correctamente a los enfermos) y una especificidad del 90% (detecta correctamente a los sanos). La prevalencia de la enfermedad en la población es del 1%. Si una persona da positivo en la prueba, ¿cuál es la probabilidad de que realmente esté enferma?

## Unidad 9: Variable aleatoria, media y varianza

**Ejercicio 10**  
Sea X una variable aleatoria discreta con función de probabilidad:  
P(X=1)=0.2, P(X=2)=0.3, P(X=3)=0.4, P(X=4)=0.1.  
a) Calcule la media (esperanza) de X.  
b) Calcule la varianza de X.  
c) Calcule P(1 ≤ X ≤ 3).

**Ejercicio 11**  
Una variable aleatoria continua Y tiene función de densidad f(y) = k·y para 0 ≤ y ≤ 2, y 0 en otro caso.  
a) Determine el valor de k para que f sea una función de densidad válida.  
b) Calcule P(Y ≤ 1).  
c) Calcule la media y la varianza de Y.

## Unidad 10: Distribuciones discretas (Binomial, Multinomial, Binomial Negativa)

**Ejercicio 12**  
Un examen tiene 10 preguntas de opción múltiple, cada una con 4 opciones (solo una correcta). Un estudiante responde al azar todas las preguntas.  
a) ¿Cuál es la probabilidad de que acierte exactamente 6 preguntas?  
b) ¿Cuál es la probabilidad de que acierte al menos 8 preguntas?  
c) ¿Cuál es el número esperado de aciertos y su desviación estándar?

**Ejercicio 13**  
En una votación, el 40% de los electores favorece al candidato A, el 35% al B y el 25% al C. Se seleccionan 8 votantes al azar con reemplazo.  
a) ¿Cuál es la probabilidad de que exactamente 4 favorezcan a A, 2 a B y 2 a C?  
b) ¿Cuál es la probabilidad de que ninguno favorezca a C?

**Ejercicio 14**  
La probabilidad de que un cliente compre un producto en una tienda en línea es 0.3. Se observan los clientes hasta encontrar el quinto que compra.  
a) ¿Cuál es la probabilidad de que se necesiten exactamente 10 clientes?  
b) ¿Cuál es el número esperado de clientes que se deben observar?

## Unidad 11: Distribuciones Hipergeométrica, Geométrica y Poisson

**Ejercicio 15**  
En una caja hay 12 bombillos, de los cuales 4 están defectuosos. Se seleccionan 5 bombillos al azar sin reemplazo.  
a) ¿Cuál es la probabilidad de que exactamente 2 estén defectuosos?  
b) ¿Cuál es el número esperado de bombillos defectuosos en la muestra?

**Ejercicio 16**  
La probabilidad de que una página web tenga un error de carga es 0.02. Cada página es independiente.  
a) ¿Cuál es la probabilidad de que la primera página con error sea la décima que se visita?  
b) ¿Cuál es la probabilidad de que se necesiten más de 5 páginas para encontrar el primer error?

**Ejercicio 17**  
El número de llamadas que recibe un call center por minuto sigue una distribución de Poisson con media 4 llamadas por minuto.  
a) ¿Cuál es la probabilidad de que en un minuto dado se reciban exactamente 3 llamadas?  
b) ¿Cuál es la probabilidad de que en un minuto se reciban 2 o menos llamadas?  
c) ¿Cuál es la probabilidad de que en 2 minutos se reciban al menos 10 llamadas?

## Unidad 12: Distribución Normal

**Ejercicio 18**  
Los puntajes de una prueba de admisión se distribuyen normalmente con media 500 y desviación estándar 100.  
a) ¿Qué porcentaje de estudiantes obtiene un puntaje entre 400 y 600?  
b) Si un estudiante obtuvo 650, ¿en qué percentil se encuentra aproximadamente?  
c) Determine el puntaje mínimo necesario para estar en el 10% superior de la distribución.

**Ejercicio 19**  
El diámetro de un rodamiento producido por una máquina sigue una distribución normal con media 2.5 cm y desviación estándar 0.05 cm. Las especificaciones requieren que el diámetro esté entre 2.4 cm y 2.6 cm.  
a) ¿Qué proporción de rodamientos cumple con las especificaciones?  
b) Si se toma una muestra de 4 rodamientos, ¿cuál es la probabilidad de que los cuatro cumplan?
