# List Market
List Market
Una aplicación de lista de compras colaborativa que permite a los usuarios crear, editar y compartir sus listas de compras en tiempo real, con características adicionales de geolocalización para encontrar tiendas cercanas. Este proyecto está desarrollado en Django.

## Características
Crear y Editar Listas: Los usuarios pueden agregar o quitar elementos de sus listas de compras.
Gestión de Usuarios: Registro e inicio de sesión para usuarios.

## Requisitos
Python 3.x
Django
Otros paquetes según requirements.txt (por ejemplo, djangorestframework para la API, channels para la funcionalidad en tiempo real).
## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/list_market.git
   cd list_market

2. Crea y activa un entorno virtual:
   ```bash
   python3 -m venv env
   source env/bin/activate  # En Windows usa `env\Scripts\activate`
   
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt

4. Realiza las migraciones de la base de datos:
   ```bash
   python manage.py migrate

5. Inicia el servidor:
   ```bash
   python manage.py runserver
   
## Uso
Accede a http://127.0.0.1:8000 en tu navegador para ver la aplicación.
Regístrate e inicia sesión.
Crea una lista de compras y comienza a agregar productos.
Comparte la lista con otros usuarios para que puedan colaborar.
Estructura del Proyecto
/list_market: Contiene la configuración principal de Django.
/shopping: Aplicación para la gestión de listas de compras.
/products: Aplicación que maneja los productos y su información.
db.sqlite3: Base de datos de desarrollo (SQLite) incluida para pruebas locales.

## Contribución
Si deseas contribuir:

Realiza un fork de este repositorio.
Crea una rama para tu funcionalidad (git checkout -b feature/nueva-funcionalidad).
Haz commit de tus cambios (git commit -m 'Agrega nueva funcionalidad').
Realiza push a la rama (git push origin feature/nueva-funcionalidad).
Abre un Pull Request.
