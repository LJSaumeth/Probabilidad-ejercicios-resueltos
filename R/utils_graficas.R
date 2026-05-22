# Utilidades para guardar gráficas en graficas/R/grafica ejercicio_XX/ (ggplot2)

carpeta_graficas <- function(num_ejercicio) {
  args <- commandArgs(trailingOnly = FALSE)
  file_arg <- grep("^--file=", args, value = TRUE)
  script_dir <- if (length(file_arg)) {
    dirname(normalizePath(sub("^--file=", "", file_arg[1]), winslash = "/"))
  } else {
    normalizePath(".", winslash = "/")
  }
  raiz <- normalizePath(file.path(script_dir, ".."), winslash = "/", mustWork = FALSE)
  carpeta <- file.path(raiz, "graficas", "R", sprintf("grafica ejercicio_%02d", num_ejercicio))
  dir.create(carpeta, recursive = TRUE, showWarnings = FALSE)
  carpeta
}

cargar_ggplot <- function() {
  if (!requireNamespace("ggplot2", quietly = TRUE)) {
    install.packages("ggplot2", repos = "https://cloud.r-project.org", quiet = TRUE)
  }
  suppressPackageStartupMessages(library(ggplot2))
  invisible(TRUE)
}

guardar_ggplot <- function(plot, carpeta, nombre, width = 8, height = 5, dpi = 120) {
  if (!grepl("\\.png$", nombre, ignore.case = TRUE)) {
    nombre <- paste0(nombre, ".png")
  }
  ruta <- file.path(carpeta, nombre)
  ggplot2::ggsave(
    filename = ruta,
    plot = plot,
    width = width,
    height = height,
    dpi = dpi,
    bg = "white"
  )
  cat(sprintf("-> Gráfica guardada: %s\n", ruta))
  invisible(ruta)
}

tema_probabilidad <- function() {
  theme_minimal(base_size = 12) +
    theme(
      plot.title = element_text(face = "bold", hjust = 0.5),
      axis.title = element_text(face = "bold")
    )
}
