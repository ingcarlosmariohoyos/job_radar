# CLAUDE.md — job-radar (Radar de Ofertas Laborales)

## Contexto
Proyecto personal de Carlos, Data Engineer / Analista de Datos BI en Cali, Colombia. Es parte de su portafolio público en GitHub. El perfil detallado y las notas privadas están en `CLAUDE.local.md` (ignorado por git).

## Qué es el proyecto
Una herramienta propia para encontrar las ofertas donde tengo más probabilidad de ser llamado:
1. Recolectar ofertas de fuentes que lo permitan (o que yo pegue a mano).
2. Limpiarlas, normalizarlas y guardarlas en una base de datos.
3. Compararlas con mi perfil: puntaje de afinidad (0-100), requisitos que cumplo y que me faltan, alertas (idioma, seniority, ubicación) y recomendación: aplicar / aplicar ajustando el CV / no aplicar.
4. Ayudarme a aplicar: palabras clave que resaltar y mensajes para contacto directo o referidos.
5. Seguimiento de postulaciones y medición de canales (tablero en Streamlit).

## Hoja de ruta (una versión a la vez)
- **v1 – Reglas (ACTUAL):** pego ofertas a mano (texto o CSV) → el script extrae requisitos, los compara con `config/skills.csv`, aplica filtros (ciudad, remoto, años de experiencia, nivel de inglés) y da puntaje y recomendación. Todo se guarda en SQLite.
- **v2 – Embeddings:** similitud semántica local con sentence-transformers. Comparar v1 vs v2 con ofertas reales y documentar cuál acierta más.
- **v3 – Automatización:** recolección desde fuentes permitidas, ejecución diaria (Dagster o Programador de tareas de Windows), PostgreSQL en Docker, plantillas de mensajes, tablero en Streamlit.
- **v4 – Opcional:** modelo local con Ollama (ya instalado) para explicar recomendaciones y redactar mensajes.

No se avanza a la siguiente versión hasta que la anterior funcione y yo la esté usando.

## Cómo debes ayudarme (MUY IMPORTANTE)
- Este proyecto es para APRENDER. **No escribas la lógica del proyecto por mí.** Dame pistas, explicaciones y revisión. Si me quedo atascado y te lo pido, muéstrame el código explicándolo línea por línea.
- Sí puedes hacer tareas de entorno y plomería (instalar paquetes, configurar git, crear carpetas, mover archivos), explicando brevemente qué haces.
- Explica el porqué de cada decisión técnica, como lo haría un Data Engineer senior.
- Si algo se puede resolver con SQL, prefiere SQL para que practique.
- Pasos pequeños: trabajo en bloques de 1-2 horas. Cada sesión termina con algo funcionando y un "siguiente paso" claro.
- Sé honesto: si una idea mía no conviene, dímelo.
- Respóndeme en español. Nombres de variables, funciones, archivos y commits, en inglés.

## Reglas del proyecto
- **Costo cero:** solo herramientas gratuitas y modelos locales. Nada de APIs de pago. Si propones un servicio con plan gratuito, verifica que siga siendo gratis y avísame de sus límites.
- Stack: Python, SQLite (v1) → PostgreSQL local en Docker (v3), Dagster, Streamlit, GitHub público.
- Streamlit corre en local con datos reales. Si se publica para el portafolio, solo una versión demo con datos inventados: nunca exponer mis postulaciones reales.
- **Nunca** usar fuentes que prohíban la extracción automática en sus términos (por ejemplo, LinkedIn o Indeed). Antes de agregar una fuente, revisar sus términos.
- **Nunca** usar datos de mi trabajo ni del banco.
- Credenciales y configuraciones sensibles en variables de entorno (`.env`), nunca en el código.
- **Mi CV (PDF) nunca se sube al repo:** tiene datos personales. El `.gitignore` excluye `*.pdf`, `data/`, `.env`, `*.db`, `.venv/` y `CLAUDE.local.md`.
- README claro: el repo es parte de mi portafolio.

## Estructura actual
```
job-radar/
├── .gitignore
├── CLAUDE.md
├── CLAUDE.local.md   (ignorado por git)
├── README.md
├── requirements.txt
├── config/
│   └── skills.csv
├── data/             (ignorada por git)
├── src/
└── tests/
```

## `config/skills.csv`
Diccionario de mis habilidades contra el que se comparan las ofertas.

Columnas:
- `skill`: identificador en snake_case.
- `aliases`: variantes como aparecen en ofertas, en minúsculas, separadas por `;`. Incluye español e inglés cuando aplique.
- `category`: bi, database, language, processing, cloud, etl, transformation, orchestration, devops.
- `level`: 1 básico, 2 intermedio, 3 fuerte. Debe ser honesto: lo que puedo defender en una entrevista técnica.
- `evidence`: `work`, `project` o `course`.

Decisiones tomadas:
- PL/SQL es alias de `sql`, no una skill aparte.
- `pandas` y `polars` van en filas propias, no como alias de `python`.
- `azure` NO es alias de `microsoft_fabric`: si una oferta pide Azure (Data Factory, Synapse, Databricks), debe salir como requisito faltante.

## Mi progreso
- Versión actual: v1
- Completado:
  - Entorno: `.venv`, estructura de carpetas, `.gitignore` verificado con `git ls-files`.
  - Repo en GitHub.
  - `config/skills.csv` con 19 skills.
  - Instrucciones para Claude Code: `CLAUDE.md` (público) y `CLAUDE.local.md` (privado, ignorado por git).
- **Siguiente paso:** `src/skills.py` con `load_skills(path)`, que lee el CSV y construye una estructura donde cada alias apunte a su skill (nombre, categoría, nivel, evidencia). Prueba: `skills_by_alias["pbi"]` debe devolver los datos de `power_bi`. Usar el módulo `csv` de la librería estándar.

## Trampas conocidas (dar como pista, no como solución)
- El alias `sql` aparece dentro de "postgresql", "mysql" y "nosql". Buscar con `in` da falsos positivos. La solución pasa por buscar palabras completas (módulo `re`, `\b`). Ojo con alias que tienen caracteres especiales (`pl/sql`, `t-sql`, `etl/elt`).
- Normalizar el texto de la oferta (minúsculas, tildes) antes de comparar.

## Mantenimiento de este archivo
Al terminar cada sesión, actualiza la sección "Mi progreso" con lo completado y el siguiente paso.
