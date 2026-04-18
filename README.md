# 🐼 Práctica de Transformación y Unión de Datos con Pandas

Pipeline de análisis de datos desarrollado como práctica académica del curso **Nuevas Tecnologías Python** — Ingeniería de Sistemas, CESDE (Semana 12 · Unidad II).

---

## ¿Qué hace este proyecto?

Implementa un pipeline completo de procesamiento de datos sobre un dataset de ventas ficticio, aplicando las técnicas fundamentales de análisis y transformación con Pandas:

- **Auditoría de llaves (PK/FK)** antes de cualquier unión — detección de duplicados y registros huérfanos
- **`merge()` con inner join y left join** — unión de tabla de vendedores con historial de transacciones
- **`groupby()` + `agg()`** — paradigma Split-Apply-Combine para métricas por región y vendedor
- **Columnas derivadas con `np.where()`** — clasificación automática de rendimiento
- **Exportación con `to_csv()`** — generación del dataset analítico final

---

## Conceptos clave aplicados

| Concepto | Descripción |
|---|---|
| `merge(how='inner')` | Intersección estricta — solo vendedores con transacciones |
| `merge(how='left')` | Preserva todo el catálogo — vendedores sin ventas aparecen con NaN |
| `groupby()` | Divide el DataFrame en grupos virtuales por categoría |
| `.agg({'monto': ['sum', 'mean', 'count']})` | Aplica múltiples funciones de agregación por grupo |
| `np.where()` | Columna derivada condicional (ej: clasificar rendimiento Alto/Bajo) |
| `reset_index()` | Convierte el índice jerárquico de groupby en columnas normales |
| `duplicated().sum()` | Detecta llaves primarias sucias antes del merge |
| `isin()` | Verifica integridad referencial entre tablas |

---

## Estructura del proyecto

```
practica-de-limpieza-pandas/
├── data/
│   ├── raw/                  # CSV de entrada (vendedores, transacciones)
│   └── processed/            # dataset_analitico.csv — resultado final
├── src/
│   └── practica_semana12.py  # Script principal
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Cómo ejecutar

```bash
# 1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/practica-de-limpieza-pandas.git
cd practica-de-limpieza-pandas

# 2. Crear y activar el entorno virtual
python -m venv .venv

# Git Bash
source .venv/Scripts/activate

# PowerShell
# .venv\Scripts\Activate.ps1

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar el pipeline
python src/practica_semana12.py
```

---

## Resultado esperado

Al ejecutar el script se generan en consola:

1. Las dos tablas de entrada (vendedores y transacciones)
2. Reporte de auditoría de llaves (PK válida, sin huérfanos)
3. Comparación inner join vs left join — evidenciando la diferencia con vendedores sin ventas
4. Métricas agregadas por región y por vendedor
5. Dataset final con columna de clasificación de rendimiento

El archivo `data/processed/dataset_analitico.csv` contiene el resultado consolidado.

---

## Dependencias

```
pandas
numpy
openpyxl
```

---

## Autor

**Pedro Zamora Martínez**  
Estudiante de Tecnico En Desarrollo De Software  — CESDE, Semestre 3 · 2026