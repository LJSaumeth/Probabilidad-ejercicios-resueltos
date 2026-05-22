enunciado <- "
=========================================================
EJERCICIO 19 (R)
Simule en R el lanzamiento de 1000 veces de dos dados justos y calcule la frecuencia relativa de que la suma sea 7. Compare con la probabilidad teórica.
=========================================================
"
cat(enunciado)

cat("--- SOLUCIÓN ---\n")
cat("Explicación: Usaremos la función 'sample()' con reemplazo para simular de forma aleatoria 1000 lanzamientos de un dado de 6 caras y otros 1000 para el segundo dado.\n")
cat("Sumaremos elemento a elemento los resultados, contaremos con una condición lógica (== 7) cuántas veces la suma dio 7 y calcularemos la proporción.\n")
cat("Por último, calculamos la teórica (hay 6 combinaciones sobre 36 posibles que suman 7 = 1/6) y comprobamos la Ley de los Grandes Números.\n\n")

# Fijar semilla para reproducibilidad (opcional, pero útil en simulaciones)
set.seed(123)
n_simulaciones <- 1000

# Simulación
dado1 <- sample(1:6, size=n_simulaciones, replace=TRUE)
dado2 <- sample(1:6, size=n_simulaciones, replace=TRUE)
suma_dados <- dado1 + dado2

# Frecuencia empírica
casos_7_simulados <- sum(suma_dados == 7)
frecuencia_relativa <- casos_7_simulados / n_simulaciones

# Probabilidad teórica
prob_teorica <- 6 / 36

cat(sprintf("-> Número de veces que sumó 7 en las %d simulaciones: %d\n", n_simulaciones, casos_7_simulados))
cat(sprintf("-> Frecuencia relativa (simulada) = %.4f\n", frecuencia_relativa))
cat(sprintf("-> Probabilidad teórica esperada (6/36) = %.4f\n", prob_teorica))
