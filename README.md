# Ejercicios de Probabilidad Resueltos

A continuación se presentan los enunciados de los ejercicios resueltos en este repositorio. Los ejercicios están separados en dos secciones, dependiendo del lenguaje en el que fueron implementados.

## Sección 1: Ejercicios en Python

Los siguientes ejercicios se encuentran resueltos en Python y se ubican en la carpeta `Python/`.

### Unidad 5: Experimentos aleatorios y espacio muestral

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

### Unidad 6: Conceptos y axiomas de probabilidad

**Ejercicio 4**  
En una facultad, el 60% de los estudiantes estudia Ingeniería de Datos, el 30% estudia Ingeniería de Sistemas y el resto otra carrera. Además, se sabe que el 40% de los estudiantes de Ingeniería de Datos usa transporte público, el 50% de los de Sistemas lo usa y el 20% de los de otras carreras también.  
a) Si se selecciona un estudiante al azar, ¿cuál es la probabilidad de que use transporte público?  
b) ¿Cuál es la probabilidad de que sea de Ingeniería de Datos dado que usa transporte público?

**Ejercicio 5**  
Se lanza un dado justo de 6 caras dos veces. Sea A el evento “la suma de los dos lanzamientos es 7” y B el evento “el primer lanzamiento es 4”.  
a) Calcule P(A), P(B) y P(A ∩ B).  
b) Verifique si A y B son independientes usando los axiomas de probabilidad.

### Unidad 7: Probabilidad condicional y eventos independientes

**Ejercicio 6**  
En una empresa, el 70% de los empleados tiene computador portátil, el 40% tiene tableta y el 25% tiene ambos dispositivos.  
a) Si se elige un empleado al azar y se sabe que tiene portátil, ¿cuál es la probabilidad de que también tenga tableta?  
b) ¿Los eventos “tener portátil” y “tener tableta” son independientes? Justifique.

**Ejercicio 7**  
Una máquina produce piezas. La probabilidad de que una pieza sea defectuosa es 0.05. Se toman tres piezas al azar (con independencia).  
a) Calcule la probabilidad de que exactamente una sea defectuosa.  
b) Calcule la probabilidad de que al menos una sea defectuosa.

### Unidad 8: Teorema de Bayes y ejercicios 2° corte

**Ejercicio 8**  
Tres máquinas (M1, M2, M3) producen el 50%, 30% y 20% de la producción total de una fábrica, respectivamente. Los porcentajes de piezas defectuosas de cada máquina son 2%, 3% y 5% respectivamente.  
a) Si se selecciona una pieza al azar y resulta defectuosa, ¿cuál es la probabilidad de que haya sido producida por la máquina M1?  
b) ¿Cuál es la probabilidad de que una pieza no sea defectuosa?

**Ejercicio 9**  
Una prueba para detectar una enfermedad tiene una sensibilidad del 95% (detecta correctamente a los enfermos) y una especificidad del 90% (detecta correctamente a los sanos). La prevalencia de la enfermedad en la población es del 1%. Si una persona da positivo en la prueba, ¿cuál es la probabilidad de que realmente esté enferma?

### Unidad 9: Variable aleatoria, media y varianza

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

### Unidad 10: Distribuciones discretas (Binomial, Multinomial, Binomial Negativa)

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

### Unidad 11: Distribuciones Hipergeométrica, Geométrica y Poisson

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

### Unidad 12: Distribución Normal

**Ejercicio 18**  
Los puntajes de una prueba de admisión se distribuyen normalmente con media 500 y desviación estándar 100.  
a) ¿Qué porcentaje de estudiantes obtiene un puntaje entre 400 y 600?  
b) Si un estudiante obtuvo 650, ¿en qué percentil se encuentra aproximadamente?  
c) Determine el puntaje mínimo necesario para estar en el 10% superior de la distribución.

**Ejercicio 19**  
El diámetro de un rodamiento producido por una máquina sigue una distribución normal con media 2.5 cm y desviación estándar 0.05 cm. Las especificaciones requieren que el diámetro esté entre 2.4 cm y 2.6 cm.  
a) ¿Qué proporción de rodamientos cumple con las especificaciones?  
b) Si se toma una muestra de 4 rodamientos, ¿cuál es la probabilidad de que los cuatro cumplan?

---

## Sección 2: Ejercicios en R

Los siguientes ejercicios se encuentran resueltos utilizando el lenguaje R y se ubican en la carpeta `R/`.

### Unidad 5: Experimentos aleatorios y espacio muestral

**Ejercicio 1**  
Se lanza un dado de 6 caras tres veces consecutivas.  
a) ¿Cuántos resultados elementales tiene el espacio muestral?  
b) Calcule la probabilidad de obtener una suma total de 10.  
c) Calcule la probabilidad de que el primer lanzamiento sea mayor que el segundo y el segundo mayor que el tercero.

**Ejercicio 2**  
De una baraja española de 40 cartas (4 palos: oros, copas, espadas, bastos; cada palo con números 1 al 7, sota, caballo, rey) se extraen dos cartas sin reemplazo.  
a) ¿Cuál es la probabilidad de que ambas sean del mismo palo?  
b) ¿Cuál es la probabilidad de que al menos una sea figura (sota, caballo o rey)?

### Unidad 6: Conceptos y axiomas de probabilidad

**Ejercicio 3**  
En una ciudad, el 55% de los hogares tiene conexión a internet de fibra óptica, el 40% tiene televisión por cable y el 25% tiene ambos servicios.  
a) Si se elige un hogar al azar, ¿cuál es la probabilidad de que tenga al menos uno de los dos servicios?  
b) ¿Cuál es la probabilidad de que tenga exactamente uno de los dos servicios?

**Ejercicio 4**  
Se lanzan dos dados justos (de 6 caras). Sean los eventos:  
A = “la suma de los dados es 8”,  
B = “el producto de los dados es 12”.  
Calcule P(A), P(B), P(A∪B) y P(A∩B). ¿Son A y B mutuamente excluyentes?

### Unidad 7: Probabilidad condicional y eventos independientes

**Ejercicio 5**  
Una urna contiene 3 bolas blancas y 2 negras. Se extraen dos bolas sucesivamente sin reemplazo.  
a) Calcule la probabilidad de que la segunda bola sea blanca dado que la primera fue negra.  
b) Calcule la probabilidad de que ambas sean blancas.  
c) ¿Los eventos “la primera es blanca” y “la segunda es blanca” son independientes?

**Ejercicio 6**  
Se sabe que el 20% de las personas tiene alergia al polen. Una prueba de alergia tiene una tasa de falsos positivos del 5% y de falsos negativos del 10%. Si una persona se somete a la prueba y da positivo, ¿cuál es la probabilidad de que realmente tenga alergia? (Use probabilidad condicional).

### Unidad 8: Teorema de Bayes

**Ejercicio 7**  
En una empresa, el 60% de los empleados trabaja en la oficina principal, el 30% en una sucursal y el 10% en teletrabajo. La probabilidad de llegar tarde es 0.01 para los de oficina principal, 0.04 para los de sucursal y 0.02 para los de teletrabajo.  
a) Si un empleado llega tarde, ¿cuál es la probabilidad de que trabaje en la oficina principal?  
b) ¿Cuál es la probabilidad global de que un empleado llegue tarde?

**Ejercicio 8**  
Tres laboratorios (L1, L2, L3) producen el 50%, 30% y 20% de las vacunas de un lote. Los porcentajes de vacunas defectuosas son 0.5%, 1% y 1.5% respectivamente. Se selecciona una vacuna al azar y resulta defectuosa. ¿Qué laboratorio tiene la mayor probabilidad de haberla producido?

### Unidad 9: Variable aleatoria, media y varianza

**Ejercicio 9**  
Sea X una variable aleatoria discreta con función de masa de probabilidad:  
P(X = x) = c·x para x = 1, 2, 3, 4; y 0 en otro caso.  
a) Determine el valor de c.  
b) Calcule E(X) y Var(X).  
c) Calcule P(X > 2).

**Ejercicio 10**  
Una variable aleatoria continua Y tiene función de densidad f(y) = (3/2)·y² para -1 ≤ y ≤ 1, y 0 en otro caso.  
a) Verifique que es una densidad.  
b) Calcule P(0 ≤ Y ≤ 0.5).  
c) Obtenga la media y la varianza de Y.

### Unidad 10: Distribuciones discretas (Binomial, Multinomial, Binomial Negativa)

**Ejercicio 11**  
Un examen tipo test consta de 15 preguntas, cada una con 5 opciones (una correcta). Un estudiante responde completamente al azar.  
a) ¿Cuál es la probabilidad de que acierte exactamente 5 preguntas?  
b) ¿Cuál es la probabilidad de que acierte 3 o menos?  
c) ¿Cuál es el número esperado de aciertos y la desviación típica?

**Ejercicio 12**  
En una población, el 45% prefiere la marca A, el 35% la marca B y el 20% la marca C. Se encuesta a 10 personas al azar (con reemplazo).  
a) ¿Cuál es la probabilidad de que 5 prefieran A, 3 B y 2 C?  
b) ¿Cuál es la probabilidad de que ninguna prefiera C?

**Ejercicio 13**  
La probabilidad de que una máquina produzca una pieza defectuosa es 0.1. Se inspeccionan piezas una por una hasta encontrar la tercera defectuosa.  
a) ¿Cuál es la probabilidad de que se necesiten inspeccionar exactamente 8 piezas?  
b) ¿Cuál es el número esperado de inspecciones necesarias?

### Unidad 11: Distribuciones Hipergeométrica, Geométrica y Poisson

**Ejercicio 14**  
En un lote de 20 artículos, 6 son defectuosos. Se seleccionan 4 artículos al azar sin reemplazo.  
a) ¿Cuál es la probabilidad de que exactamente 2 sean defectuosos?  
b) ¿Cuál es la probabilidad de que a lo sumo 1 sea defectuoso?  
c) ¿Cuál es el valor esperado y la varianza del número de defectuosos en la muestra?

**Ejercicio 15**  
La probabilidad de que una persona compre un boleto de lotería en una tienda es 0.05. Cada persona actúa independientemente.  
a) ¿Cuál es la probabilidad de que la primera compra ocurra en la quinta persona que entra?  
b) ¿Cuál es la probabilidad de que se requieran más de 8 personas para encontrar la primera compra?

**Ejercicio 16**  
El número de accidentes diarios en una fábrica sigue una distribución de Poisson con media 2.5 accidentes por día.  
a) ¿Cuál es la probabilidad de que un día dado ocurran exactamente 3 accidentes?  
b) ¿Cuál es la probabilidad de que ocurran 2 o menos accidentes en un día?  
c) ¿Cuál es la probabilidad de que en una semana laboral (5 días) ocurran al menos 10 accidentes en total?

### Unidad 12: Distribución Normal

**Ejercicio 17**  
Los tiempos de reparación de un equipo siguen una distribución normal con media 45 minutos y desviación estándar 8 minutos.  
a) ¿Qué proporción de reparaciones duran entre 40 y 50 minutos?  
b) ¿Cuál es el tiempo máximo que dura el 90% de las reparaciones más cortas?  
c) Si se toman 6 reparaciones al azar, ¿cuál es la probabilidad de que todas duren menos de 50 minutos?

**Ejercicio 18**  
El peso de un paquete de café etiquetado como “500 g” tiene una distribución normal con media 502 g y desviación estándar 3 g. La normativa permite que a lo sumo el 5% de los paquetes pese menos de 500 g. ¿Cumple el proceso con esta normativa? Calcule la probabilidad de que un paquete pese menos de 500 g.

### Unidad 13: Introducción a herramientas TIC (aplicable a R)

**Ejercicio 19**  
Simule en R el lanzamiento de 1000 veces de dos dados justos y calcule la frecuencia relativa de que la suma sea 7. Compare con la probabilidad teórica.

**Ejercicio 20**  
Genere 500 valores aleatorios de una distribución normal con media 100 y desviación 15. A partir de esos datos, calcule la media muestral, la desviación estándar muestral y el porcentaje de valores que caen dentro de una desviación estándar de la media. Compare con los valores teóricos de la regla empírica.
