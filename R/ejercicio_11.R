enunciado <- "
=========================================================
EJERCICIO 11 (R)
Un examen tipo test consta de 15 preguntas, cada una con 5 opciones (una correcta). Un estudiante responde completamente al azar.
a) ¿Cuál es la probabilidad de que acierte exactamente 5 preguntas?
b) ¿Cuál es la probabilidad de que acierte 3 o menos?
c) ¿Cuál es el número esperado de aciertos y la desviación típica?
=========================================================
"
cat(enunciado)

n <- 15
p <- 1/5

cat("--- SOLUCIÓN a) ---\n")
cat("Explicación: Utilizamos la distribución Binomial. En R, usamos dbinom(x, size, prob) para calcular la probabilidad exacta P(X=5).\n")
prob_5 <- dbinom(5, size=n, prob=p)
cat(sprintf("-> P(X=5) = %.4f\n\n", prob_5))

cat("--- SOLUCIÓN b) ---\n")
cat("Explicación: Para P(X ≤ 3), usamos pbinom(q, size, prob) que calcula la probabilidad acumulada de 0 a 3 aciertos.\n")
prob_3_o_menos <- pbinom(3, size=n, prob=p)
cat(sprintf("-> P(X ≤ 3) = %.4f\n\n", prob_3_o_menos))

cat("--- SOLUCIÓN c) ---\n")
cat("Explicación: En una Binomial, la media es n*p. La varianza es n*p*(1-p) y la desviación típica es su raíz cuadrada.\n")
media <- n * p
varianza <- n * p * (1 - p)
desv_tipica <- sqrt(varianza)
cat(sprintf("-> Número esperado de aciertos (Media) = %d * %.2f = %.4f\n", n, p, media))
cat(sprintf("-> Desviación típica = %.4f\n", desv_tipica))
