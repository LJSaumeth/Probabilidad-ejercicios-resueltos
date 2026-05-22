# Ejecuta todos los ejercicios R y genera gráficas con ggplot2
$Rscript = "C:\Program Files\R\R-4.6.0\bin\Rscript.exe"
if (-not (Test-Path $Rscript)) {
    $Rscript = Get-ChildItem "C:\Program Files\R\*\bin\Rscript.exe" -ErrorAction SilentlyContinue |
        Sort-Object FullName -Descending |
        Select-Object -First 1 -ExpandProperty FullName
}
if (-not $Rscript) {
    Write-Error "No se encontró Rscript. Instala R: winget install RProject.R"
    exit 1
}
$raiz = $PSScriptRoot
Get-ChildItem (Join-Path $raiz "R\ejercicio_*.R") | Sort-Object Name | ForEach-Object {
    Write-Host ">> $($_.Name)"
    & $Rscript $_.FullName
}
Write-Host "`nListo. Gráficas en: $raiz\graficas\R\"
