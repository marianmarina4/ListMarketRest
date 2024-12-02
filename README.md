# ListMarketRest 🛒

ListMarketRest es una API REST para gestionar listas de compras. Proporciona funcionalidades como la creación, edición, y compartición de listas entre usuarios registrados. Está diseñada para facilitar la organización de compras y la colaboración en tiempo real.

---

## Características ✨

- Crear, actualizar y eliminar listas de compras.
- Agregar productos a las listas.
- Compartir listas de compras con otros usuarios.
- Control de acceso basado en usuarios.
- Documentación de la API generada automáticamente con Swagger.

---

## Tecnologías Utilizadas 🛠️

- **Backend**: Django, Django REST Framework
- **Base de datos**: SQLite (en desarrollo), compatible con PostgreSQL.
- **Autenticación**: Token Authentication.
- **Documentación de la API**: Swagger/OpenAPI.

---

## Instalación ⚙️

Sigue estos pasos para configurar el proyecto localmente:

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu_usuario/ListMarketRest.git
   cd ListMarketRest
# List Market
Una API de lista de compras colaborativa que permite a los usuarios crear, editar y compartir sus listas de compras en tiempo real. Este proyecto está desarrollado en Django.

### Características
* Crear y Editar Listas: Los usuarios pueden agregar o quitar elementos de sus listas de compras.
* Gestión de Usuarios: Registro e inicio de sesión para usuarios.

### Requisitos
* Python 3.x
* Django
* Otros paquetes según requirements.txt (por ejemplo, djangorestframework para la API, channels para la funcionalidad en tiempo real).
### Instalación

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
   
### Uso
1. Accede a http://127.0.0.1:8000 en tu navegador para ver la aplicación.
2. Regístrate e inicia sesión.
3. Crea una lista de compras y comienza a agregar productos.
4. Comparte la lista con otros usuarios para que puedan colaborar.

### Estructura del Proyecto
* /list_market: Contiene la configuración principal de Django.
* /shopping: Aplicación para la gestión de listas de compras.
* /products: Aplicación que maneja los productos y su información.
