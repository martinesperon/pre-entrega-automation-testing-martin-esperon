# 🧪 Framework de Automatización de Pruebas – Trabajo Final Integrador

## 📌 Descripción del Proyecto

Este proyecto implementa un framework de automatización de pruebas desarrollado en **Python** que integra:

- **Pruebas de UI** con Selenium WebDriver  
- **Pruebas de API** utilizando Requests  
- **Ejecución de tests** con Pytest  
- **Generación de reportes HTML** automáticos con captura de pantallas  

El objetivo principal es demostrar un flujo completo de testing automatizado, aplicando buenas prácticas, separación de responsabilidades y el patrón **Page Object Model (POM)** para garantizar mantenibilidad y escalabilidad del código.

---

## 🛠 Tecnologías Utilizadas

- **Python 3.x**
- **Pytest**
- **Selenium WebDriver**
- **Requests**
- **pytest-html / pytest-selenium**
- **Git + GitHub**

---

## 📁 Estructura del Proyecto

.
├── pages/ # Page Object Model (clases por página)
│ ├── login_page.py
│ ├── home_page.py
│ └── products_page.py
│
├── tests/
│ ├── ui/
│ │ ├── test_login.py # Casos UI con Selenium
│ │ ├── test_add_to_cart.py
│ │ └── test_checkout.py
│ │
│ ├── api/
│ │ ├── test_get_users.py # Requests API GET
│ │ ├── test_create_user.py # Requests API POST
│ │ └── test_delete_user.py # Requests API DELETE
│
├── utils/
│ ├── driver_factory.py # Inicialización WebDriver
│ └── helpers.py
│
├── reports/
│ └── html/ # Reportes generados automáticamente
│
├── requirements.txt
├── pytest.ini
└── README.md
---

## 🚀 Funcionalidades Implementadas

### ✔ 1. Pruebas de UI (Selenium WebDriver)

- Al menos **5 casos de prueba** sobre un sitio demo (por ejemplo: saucedemo.com)  
- Flujo de prueba completo: login → navegación → agregar producto → checkout  
- **Escenario negativo obligatorio** (ej: login inválido)  
- Código estructurado siguiendo **Page Object Model (POM)**  

### ✔ 2. Pruebas de API (Requests)

- Al menos **3 casos automáticos** usando una API pública (ReqRes / JSONPlaceholder)  
- Métodos HTTP cubiertos: **GET, POST, DELETE**  
- Validación de:
  - Código de estado  
  - Estructura JSON  
  - Campos específicos  
  - Escenarios positivos y negativos  

### ✔ 3. Reportes HTML

- Generación automática de reportes detallados:
  - Tests ejecutados
  - Estado (pasado / fallado)
  - Duración
- **Capturas de pantalla automáticas** en pruebas fallidas de UI

Ejemplo de comando:

bash
```pytest --html=reports/html/report.html --self-contained-html```

## 📦 Instalación del Proyecto
1. Clonar el repositorio
```git clone https://github.com/usuario/nombre-del-repo.git```
```cd nombre-del-repo```

2. Crear entorno virtual (opcional pero recomendado)
```python -m venv venv```

```source venv/bin/activate       # Linux / Mac```
```venv\Scripts\activate          # Windows```

3. Instalar dependencias
```pip install -r requirements.txt```

▶️ Cómo Ejecutar las Pruebas
Ejecutar todas las pruebas
pytest

Ejecutar solo UI
```pytest tests/ui```

Ejecutar solo API
```pytest tests/api```

Generar un reporte HTML
```pytest --html=reports/html/report.html --self-contained-html```

📊 ¿Cómo Interpretar los Reportes?

Los reportes HTML generados incluyen:

Resumen general
Total de tests, pasados, fallados y tiempo total de ejecución

Detalle individual por test
Nombre del test y estado

Captura de pantalla automática (solo para UI)
Se adjunta cuando una prueba falla
→ permite verificar visualmente el estado final del navegador

Ubicación de los reportes
reports/html/report.html

Abrilo en cualquier navegador.

✍️ Autor Martín Esperon

Trabajo Final Integrador – Framework de Automatización de Pruebas
Curso: QA con Automatización – Python + Selenium + Pytest
