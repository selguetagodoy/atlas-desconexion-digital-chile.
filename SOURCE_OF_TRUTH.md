# Source of Truth

Este documento define qué archivos y referencias deben considerarse canónicos dentro del repositorio público del **Atlas de la Desconexión Digital de Chile 2026**.

## 1. Identidad del proyecto

- **Proyecto:** Atlas de la Desconexión Digital de Chile 2026.
- **Autor:** Sebastián Elgueta Godoy.
- **Concept DOI:** https://doi.org/10.5281/zenodo.22921208
- **Version DOI v0.1.0:** https://doi.org/10.5281/zenodo.22921209
- **Landing canónica:** https://selguetagodoy.github.io/atlas-desconexion-digital-chile.html
- **Repositorio:** https://github.com/selguetagodoy/atlas-desconexion-digital-chile.

## 2. Jerarquía de evidencia

Para resolver discrepancias, se utiliza el siguiente orden:

1. fuente oficial primaria documentada en `data/source_registry.json`;
2. documentación metodológica del proyecto;
3. archivos de muestra publicados en `data/`;
4. README y piezas de difusión;
5. referencias externas de terceros.

Las notas institucionales de COTEL documentan presentación, difusión y autoría pública del Atlas, pero no reemplazan las fuentes estadísticas originales.

## 3. Registro de fuentes

`data/source_registry.json` es el registro canónico de las principales fuentes externas del proyecto. Cada entrada identifica institución, conjunto de datos, URL oficial, período de referencia, uso analítico y condición de redistribución.

El workflow `.github/workflows/source-urls.yml` comprueba semanalmente que esas URLs sigan respondiendo. Un bloqueo anti-bot o un error 4xx se registra como advertencia; errores de red persistentes o respuestas 5xx hacen fallar el chequeo para forzar revisión.

## 4. Datos publicados

Este repositorio contiene únicamente una muestra pública:

- `data/muestra_severidad.csv`
- `data/muestra_volumen.csv`

Estos archivos no representan la base comunal completa ni permiten reconstruir íntegramente el Índice de Vulnerabilidad Digital.

## 5. Reglas de integridad

- No completar observaciones faltantes sin evidencia.
- No presentar estimaciones como datos observados.
- Conservar el universo y denominador de cada indicador.
- Mantener separadas severidad relativa y volumen absoluto.
- Atribuir siempre la fuente primaria cuando se publique un resultado derivado.
- No redistribuir bases de terceros desde este repositorio salvo que sus términos lo permitan explícitamente.

## 6. Citación

La referencia citable del proyecto está definida en `CITATION.cff` y `CITATION.bib`. Para una versión archivada y persistente debe preferirse el DOI de Zenodo correspondiente a la versión utilizada.
