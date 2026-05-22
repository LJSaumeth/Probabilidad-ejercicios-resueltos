enunciado <- "
=========================================================
EJERCICIO 9 (R)
Sea X una variable aleatoria discreta con función de masa de probabilidad:
P(X = x) = c·x para x = 1, 2, 3, 4; y 0 en otro caso.
a) Determine el valor de c.
b) Calcule E(X) y Var(X).
c) Calcule P(X > 2).
=========================================================
"
cat(enunciado)

cat("--- SOLUCIÓN a) ---\n")
cat("Explicación: Por definición, la sumatoria de las probabilidades de todos los resultados posibles en una distribución discreta debe ser 1.\n")
cat("Suma de c*x para x en {1,2,3,4} es c*(1+2+3+4) = 10*c. Igualamos a 1.\n")
c <- 1 / 10
cat(sprintf("-> c = 1 / 10 = %.2f\n\n", c))

x_vals <- 1:4
p_x <- c * x_vals

cat("--- SOLUCIÓN b) ---\n")
cat("Explicación: La esperanza E[X] es sum(x * P(X=x)). La Varianza Var(X) es E[X^2] - (E[X])^2.\n")
E_X <- sum(x_vals * p_x)
E_X2 <- sum((x_vals^2) * p_x)
Var_X <- E_X2 - (E_X^2)

cat(sprintf("-> E[X] = (1*0.1) + (2*0.2) + (3*0.3) + (4*0.4) = %.4f\n", E_X))
cat(sprintf("-> E[X^2] = (1*0.1) + (4*0.2) + (9*0.3) + (16*0.4) = %.4f\n", E_X2))
cat(sprintf("-> Var(X) = %.4f - (%.4f)^2 = %.4f\n\n", E_X2, E_X, Var_X))

cat("--- SOLUCIÓN c) ---\n")
cat("Explicación: Para P(X > 2), sumamos simplemente las probabilidades correspondientes a X=3 y X=4.\n")
p_mayor_2 <- p_x[3] + p_x[4]
cat(sprintf("-> P(X > 2) = P(X=3) + P(X=4) = %.4f + %.4f = %.4f\n", p_x[3], p_x[4], p_mayor_2))
