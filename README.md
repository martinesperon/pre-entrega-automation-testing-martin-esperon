# 🧪 Pre Entrega - Automation Testing (Martín Esperon)

## 📌 Propósito del proyecto
Este proyecto forma parte del trabajo práctico final del curso de **Automatización de Pruebas de Software**.  
El objetivo es demostrar el uso de **Selenium WebDriver** y **Pytest** para automatizar pruebas funcionales sobre una aplicación web real: [https://www.saucedemo.com](https://www.saucedemo.com).

Las pruebas automatizadas validan:
- El título de la página principal.
- El inicio de sesión exitoso con credenciales válidas.
- La correcta visualización de productos.
- La funcionalidad del carrito de compras.

---

## ⚙️ Tecnologías utilizadas
- **Python 3.12**
- **Selenium 4.x**
- **Pytest**
- **pytest-html** (para generación de reportes)
- **Google Chrome** y **ChromeDriver**

---

## 🧠 Comando para ejecutar las pruebas

- **Para ejecutar todas las pruebas y generar un reporte en HTML:**
pytest -v --html=reports/reporte.html --self-contained-html
