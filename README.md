# Calculadora de Precios (Python)

Aplicación de consola desarrollada en Python que permite calcular precios aplicando impuestos (IVA) y descuentos porcentuales de forma combinada o independiente. Este proyecto forma parte de la **Tarea 2: Trabajando con distintas herramientas** del módulo de Despliegue de Aplicaciones Web.

---

## Características de la Aplicación

- **Cálculo de IVA:** Permite calcular el precio final añadiendo un porcentaje de IVA configurable (por defecto 21%).
- **Aplicación de Descuentos:** Permite aplicar descuentos porcentuales (entre 0% y 100%) sobre un precio base.
- **Precio Final:** Aplica de forma encadenada primero el descuento y posteriormente el IVA correspondiente.
- **Control de Errores:** Validación robusta frente a entradas negativas o valores no numéricos.

---

## Requisitos del Sistema

- **Python** (versión 3.8 o superior recomendada).
- **Sphinx** (para la generación opcional de la documentación técnica).

---

## Instalación y Configuración del Entorno

1. **Clonar o descargar el repositorio** en tu equipo local:
   ```bash
   git clone <url-de-tu-repositorio>
   cd calculadora_precios
   ```

2. **Crear y activar un entorno virtual** (opcional pero recomendado):
   - En Windows:
     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```
   - En Linux / macOS:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

---

## Ejecución del Programa

Para ejecutar la calculadora interactiva por consola, ejecuta el siguiente comando:

```bash
python calculadora.py
```

---

## Documentación Técnica (Sphinx)

El código fuente se encuentra documentado siguiendo el estándar **PEP 257** mediante docstrings de estilo reStructuredText (`:param:`, `:type:`, `:return:`, `:raises:`).

Para generar la documentación técnica automatizada mediante **Sphinx**:
1. Inicializa Sphinx dentro de la carpeta del proyecto si aún no está configurado:
   ```bash
   sphinx-quickstart
   ```
2. Configura el archivo `source/conf.py` habilitando la extensión `sphinx.ext.autodoc` y apuntando a la ruta del código fuente.
3. Compila la documentación a HTML:
   - En Windows: `.\build\html\index.html` o `make.bat html`
   - En Linux / macOS: `make html`

---

## Autor
Proyecto desarrollado para el ciclo formativo de Desarrollo de Aplicaciones Web (DAW).