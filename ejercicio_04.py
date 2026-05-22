def main():
    # Probabilidades de cada carrera
    p_datos = 0.60
    p_sistemas = 0.30
    p_otras = 0.10  # El 10% restante

    # Probabilidades de usar transporte público (TP) dado la carrera
    p_tp_dado_datos = 0.40
    p_tp_dado_sistemas = 0.50
    p_tp_dado_otras = 0.20

    # a) Si se selecciona un estudiante al azar, probabilidad de que use TP
    # Se usa el Teorema de la Probabilidad Total
    p_tp = (p_datos * p_tp_dado_datos) + (p_sistemas * p_tp_dado_sistemas) + (p_otras * p_tp_dado_otras)
    print(f"a) Probabilidad de que use transporte público P(TP): {p_tp:.4f}")

    # b) Probabilidad de que sea de Ingeniería de Datos dado que usa TP
    # Se usa el Teorema de Bayes
    p_datos_dado_tp = (p_datos * p_tp_dado_datos) / p_tp
    print(f"b) Probabilidad de que sea de Ing. Datos dado que usa TP P(Datos|TP): {p_datos_dado_tp:.4f}")

if __name__ == "__main__":
    main()
