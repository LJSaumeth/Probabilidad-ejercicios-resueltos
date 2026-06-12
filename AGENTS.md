# AGENTS.md

## Repo overview

Two independent language trees (`Python/`, `R/`) with solved probability exercises. Each file is a standalone script — no shared code or imports between exercises except the common plotting utilities.

## How to run

```bash
# Python — any single exercise
python Python/ejercicio_01.py

# R — all exercises (Windows only, generates graphs)
powershell ./ejecutar_R.ps1

# R — single exercise
Rscript R/ejercicio_01.R
```

## Dependencies

- **Python**: `matplotlib>=3.8`, `scipy>=1.11` (`requirements.txt`)
- **R**: `ggplot2` (auto-installs from CRAN when missing via `utils_graficas.R:18`)

## File patterns & conventions

- Exercise files are named `ejercicio_NN.py` / `ejercicio_NN.R` (zero-padded two digits).
- Python: 19 exercises (`ejercicio_01.py`–`ejercicio_19.py`). R: 20 exercises (`ejercicio_01.R`–`ejercicio_20.R`).
- **Python conventions**:
  - Every file has a `main()` called from `if __name__ == "__main__":`.
  - Each defines a `crear_graficas()` function that saves a PNG via `graficas_util.guardar_figura()`.
  - All imports from `graficas_util` (same directory, no package prefix).
- **R conventions**:
  - Each file prints an `enunciado` variable with `cat()`, then step-by-step solutions.
  - Graph generation is conditional: `source("utils_graficas.R")` only triggers when the script detects the `--file=` CLI arg (i.e., run via `Rscript`). Interactive/sourced execution skips graphs.
- Graphs output to `graficas/Python/grafica ejercicio_NN/` and `graficas/R/grafica ejercicio_NN/` respectively.

## Gotchas

- `graficas_util.py` reconfigures stdout to UTF-8 on import — Windows-specific workaround. Don't remove it.
- `ejecutar_R.ps1` hardcodes a Windows R path (`C:\Program Files\R\*\bin\Rscript.exe`). Won't work on other OS.
- R graph generation uses `--file=` detection; graphs are silently skipped if run in RStudio or the R REPL.
- No test framework, no linter/formatter config, no CI. Verification is manual: run the script and inspect its printed output.
- The `graficas/` directories are version-controlled and pre-populated. Running exercises regenerates them in-place.
