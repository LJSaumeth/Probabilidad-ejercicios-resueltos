enunciado <- "
=========================================================
EJERCICIO 1 (R)
Se lanza un dado de 6 caras tres veces consecutivas.
a) ¿Cuántos resultados elementales tiene el espacio muestral?
b) Calcule la probabilidad de obtener una suma total de 10.
c) Calcule la probabilidad de que el primer lanzamiento sea mayor que el segundo y el segundo mayor que el tercero.
=========================================================
"
cat(enunciado)

cat("--- SOLUCIÓN a) ---\n")
cat("Explicación: Cada lanzamiento tiene 6 resultados posibles. Como son 3 lanzamientos independientes, usamos el principio multiplicativo: 6 * 6 * 6.\n")
resultados_totales <- 6^3
cat(sprintf("-> Resultados elementales: %d\n\n", resultados_totales))

cat("--- SOLUCIÓN b) ---\n")
cat("Explicación: Generamos el espacio muestral completo usando expand.grid y filtramos las combinaciones cuya suma sea 10.\n")
espacio <- expand.grid(d1=1:6, d2=1:6, d3=1:6)
suma_10 <- subset(espacio, d1 + d2 + d3 == 10)
casos_favorables_b <- nrow(suma_10)
prob_b <- casos_favorables_b / resultados_totales
cat(sprintf("-> Combinaciones que suman 10: %d\n", casos_favorables_b))
cat(sprintf("-> Probabilidad de suma 10 = %d / %d = %.4f\n\n", casos_favorables_b, resultados_totales, prob_b))

cat("--- SOLUCIÓN c) ---\n")
cat("Explicación: Buscamos combinaciones donde el primer dado sea mayor al segundo y este mayor al tercero (d1 > d2 > d3). Contamos los casos y dividimos por el total.\n")
mayor_estricto <- subset(espacio, d1 > d2 & d2 > d3)
casos_favorables_c <- nrow(mayor_estricto)
prob_c <- casos_favorables_c / resultados_totales
cat(sprintf("-> Combinaciones con d1 > d2 > d3: %d\n", casos_favorables_c))
cat(sprintf("-> Probabilidad = %d / %d = %.4f\n", casos_favorables_c, resultados_totales, prob_c))
