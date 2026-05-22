"""Utilidades para guardar gráficas en graficas/Python/grafica ejercicio_XX/."""

import io
import sys
from pathlib import Path

import matplotlib.pyplot as plt


def _configurar_salida_utf8() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except (AttributeError, LookupError, OSError):
            pass
    elif hasattr(sys.stdout, "buffer"):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")


_configurar_salida_utf8()


def carpeta_graficas(num_ejercicio: int) -> Path:
    base = Path(__file__).resolve().parent.parent / "graficas" / "Python"
    carpeta = base / f"grafica ejercicio_{num_ejercicio:02d}"
    carpeta.mkdir(parents=True, exist_ok=True)
    return carpeta


def guardar_figura(carpeta: Path, nombre: str, dpi: int = 150) -> Path:
    if not nombre.endswith(".png"):
        nombre = f"{nombre}.png"
    ruta = carpeta / nombre
    plt.tight_layout()
    plt.savefig(ruta, dpi=dpi, bbox_inches="tight")
    plt.close()
    print(f"-> Gráfica guardada: {ruta}")
    return ruta
