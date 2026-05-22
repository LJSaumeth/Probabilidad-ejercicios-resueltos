import math

def main():
    # a) Cuántos códigos diferentes son posibles
    # 10 opciones para cada uno de los 4 dígitos (con repetición)
    total_codigos = 10 ** 4
    print(f"a) Códigos diferentes posibles: {total_codigos}")

    # b) Probabilidad de que tenga todos sus dígitos diferentes
    # Permutaciones de 10 elementos tomados de a 4
    codigos_diferentes = math.perm(10, 4)
    prob_diferentes = codigos_diferentes / total_codigos
    print(f"\nb) Probabilidad de todos los dígitos diferentes:")
    print(f"   Códigos sin repetición: {codigos_diferentes}")
    print(f"   Probabilidad = {codigos_diferentes}/{total_codigos} = {prob_diferentes:.4f}")

    # c) Probabilidad de que el código termine en un número par
    # Opciones para el último dígito (par): 0, 2, 4, 6, 8 (5 opciones)
    # Los otros 3 dígitos tienen 10 opciones cada uno
    codigos_pares = (10 ** 3) * 5
    prob_pares = codigos_pares / total_codigos
    print(f"\nc) Probabilidad de terminar en número par:")
    print(f"   Códigos que terminan en par: {codigos_pares}")
    print(f"   Probabilidad = {codigos_pares}/{total_codigos} = {prob_pares:.4f}")

if __name__ == "__main__":
    main()
