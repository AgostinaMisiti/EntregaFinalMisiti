# Proyecto de Tienda de Ropa

Este proyecto es una aplicación web desarrollada con Django, que permite gestionar una tienda de ropa. Los usuarios pueden iniciar sesión, cerrar sesión, agregar prendas, buscarlas y ver una página sobre el creador del proyecto.

## Características

- **Inicio de sesión**: Los usuarios pueden iniciar sesión con sus credenciales.
- **Cierre de sesión**: Los usuarios pueden cerrar sesión.
- **Agregar prendas**: Los usuarios pueden agregar prendas con nombre, talle y precio.
- **Buscar prendas**: Los usuarios pueden buscar prendas por nombre.
- **Página de "Acerca de mí"**: Información sobre el creador del proyecto.
- **Herencia de plantillas**: Uso de plantillas base para crear un diseño consistente en todas las páginas.

## Tecnologías Utilizadas
**Django**: Framework web para desarrollo rápido y eficiente.
**Python**: Lenguaje de programación principal.

## Estructura del Proyecto
**ropa/**: Carpeta que contiene la aplicación principal del proyecto (maneja las prendas).
**templates/**: Carpeta que contiene las plantillas HTML de la aplicación.
**db.sqlite3**: Base de datos SQLite donde se almacenan los datos.

## Instalación

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/tuusuario/tu-repositorio.git

2. **Crear un entorno virtual**:
python -m venv venv

3. **Activar el entorno virtual**:
En windows: .\venv\Scripts\activate

4. **Instalar las dependencias**:
pip install -r requirements.txt

5. **Realizar las migraciones de la base de datos**:
python manage.py migrate

6. **Ejecutar el servidor de desarrollo**:
python manage.py runserver


