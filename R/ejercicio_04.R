enunciado <- "
=========================================================
EJERCICIO 4 (R)
Se lanzan dos dados justos (de 6 caras). Sean los eventos:
A = “la suma de los dados es 8”,
B = “el producto de los dados es 12”.
Calcule P(A), P(B), P(A∪B) y P(A∩B). ¿Son A y B mutuamente excluyentes?
=========================================================
"
cat(enunciado)

espacio <- expand.grid(d1=1:6, d2=1:6)
espacio$suma <- espacio$d1 + espacio$d2
espacio$prod <- espacio$d1 * espacio$d2
n_S <- nrow(espacio)

A <- subset(espacio, suma == 8)
B <- subset(espacio, prod == 12)
A_int_B <- subset(espacio, suma == 8 & prod == 12)

p_A <- nrow(A) / n_S
p_B <- nrow(B) / n_S
p_A_int_B <- nrow(A_int_B) / n_S
p_A_union_B <- p_A + p_B - p_A_int_B

cat("--- SOLUCIÓN ---\n")
cat("Explicación: Generamos el espacio muestral de 2 dados (36 casos en total). Luego filtramos los casos para A y B, y obtenemos las probabilidades dividiendo por 36.\n")
cat(sprintf("-> Casos totales: %d\n", n_S))
cat(sprintf("-> P(A) [suma=8] = %d / %d = %.4f\n", nrow(A), n_S, p_A))
cat(sprintf("-> P(B) [producto=12] = %d / %d = %.4f\n", nrow(B), n_S, p_B))
cat(sprintf("-> P(A ∩ B) = %d / %d = %.4f\n", nrow(A_int_B), n_S, p_A_int_B))
cat(sprintf("-> P(A U B) = P(A) + P(B) - P(A ∩ B) = %.4f\n\n", p_A_union_B))

cat("¿Son mutuamente excluyentes?\n")
cat("Explicación: Dos eventos son mutuamente excluyentes si no pueden ocurrir a la vez, es decir, si P(A ∩ B) = 0.\n")
if(p_A_int_B == 0){
  cat("-> SÍ son mutuamente excluyentes, porque P(A ∩ B) = 0.\n")
} else {
  cat(sprintf("-> NO son mutuamente excluyentes, porque P(A ∩ B) = %.4f (distinto de 0).\n", p_A_int_B))
}
