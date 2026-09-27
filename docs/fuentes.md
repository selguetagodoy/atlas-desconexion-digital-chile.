# Fuentes y trazabilidad

La versión completa del Atlas se construye a partir de fuentes oficiales y procesamiento propio. Este repositorio no redistribuye las bases originales de terceros; publica únicamente resultados seleccionados y una muestra metodológica.

El registro estructurado y canónico vive en [`data/source_registry.json`](../data/source_registry.json). Allí se documentan institución, conjunto de datos, URL oficial, período de referencia, función analítica y condición de redistribución.

| Fuente | Institución | Uso principal | Referencia oficial |
| --- | --- | --- | --- |
| Censo de Población y Vivienda 2024 | Instituto Nacional de Estadísticas | Población, hogares, viviendas y denominadores territoriales | https://censo2024.ine.gob.cl/resultados/ |
| CASEN 2024 | Ministerio de Desarrollo Social y Familia — Observatorio Social | Contexto socioeconómico y variables sociales | https://observatorio.ministeriodesarrollosocial.gob.cl/encuesta-casen-2024 |
| Estadísticas de Internet | Subsecretaría de Telecomunicaciones | Antecedentes sectoriales de conectividad y telecomunicaciones | https://www.subtel.gob.cl/estudios-y-estadisticas/internet/ |
| Mapoteca de comunas | Biblioteca del Congreso Nacional — SIIT | Referencia territorial y cartografía administrativa | https://www.bcn.cl/siit/mapoteca/comunas |

## Criterio de uso

Las fuentes oficiales constituyen la primera capa de evidencia. Los indicadores derivados deben conservar su universo, denominador, período y definición original. Los datos faltantes no se completan mediante extrapolación y una estimación no debe presentarse como observación.

La relación entre archivos canónicos, resultados publicados y fuentes externas está definida en [`SOURCE_OF_TRUTH.md`](../SOURCE_OF_TRUTH.md).

## Control automático

El workflow [`.github/workflows/source-urls.yml`](../.github/workflows/source-urls.yml) revisa semanalmente las URLs incluidas en el registro. El objetivo es detectar tempranamente fuentes movidas, caídas o que requieran revisión manual.
