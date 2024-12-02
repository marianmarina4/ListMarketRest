# List Market API 🛒

**Aplicación para la gestión de listas de compras compartidas**, diseñada para facilitar la colaboración en tiempo real entre usuarios.

## Descripción 📋

**List Market API** es una aplicación basada en Django REST Framework que permite a los usuarios:

- Crear y administrar listas de compras.
- Agregar, editar y eliminar productos en listas de compras.
- Compartir listas con otros usuarios para colaborar.
- Filtrar y buscar listas de compras por usuario o estado.

El proyecto está diseñado con **JWT** para la autenticación y permisos personalizados para gestionar el acceso según roles de usuario (propietario o usuario compartido).

## Características principales ✨

- **Autenticación y permisos:** Implementación de JWT para seguridad y control de accesos mediante permisos personalizados.
- **Gestión de listas y productos:** Crear, actualizar, eliminar y compartir listas de compras con productos asociados.
- **API RESTful:** Diseño modular que sigue las mejores prácticas para APIs.
- **Estado lógico de eliminación:** Las listas no se eliminan físicamente; su estado cambia a inactivo.
- **Filtro por usuario:** Las listas visibles son aquellas creadas por el usuario o compartidas con él.

---

## Requisitos previos 🛠️

Asegúrate de tener instalados los siguientes programas:

- **Python 3.8 o superior**
- **Pipenv** (opcional, para manejar dependencias)
- **PostgreSQL** (u otro motor de base de datos compatible)

---

## Instalación 🚀

Sigue estos pasos para configurar el proyecto localmente:

### 1. Clonar el repositorio

```bash
git clone <URL_DE_TU_REPOSITORIO>
cd list_market
2. Crear un entorno virtual e instalar dependencias
bash
Copiar código
python -m venv env
source env/bin/activate    # En Windows: .\env\Scripts\activate
pip install -r requirements.txt
3. Configurar la base de datos
Crea una base de datos en PostgreSQL y configura las credenciales en settings.py:

python
Copiar código
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<NOMBRE_BD>',
        'USER': '<USUARIO>',
        'PASSWORD': '<CONTRASEÑA>',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Aplica las migraciones:

bash
Copiar código
python manage.py makemigrations
python manage.py migrate
4. Crear un superusuario
bash
Copiar código
python manage.py createsuperuser
5. Ejecutar el servidor
bash
Copiar código
python manage.py runserver
Accede a la aplicación en http://127.0.0.1:8000.

Uso de la API 📡
Autenticación
La API utiliza JWT para la autenticación. Primero, obtén un token enviando una solicitud POST a:

plaintext
Copiar código
POST /api/token/
Con el token recibido, inclúyelo en los encabezados de tus solicitudes como:

plaintext
Copiar código
Authorization: Bearer <TOKEN>
Endpoints principales
Listas de compras:
GET /shopping/ - Listar listas visibles.
POST /shopping/ - Crear una lista.
PUT /shopping/<id>/ - Actualizar una lista.
DELETE /shopping/<id>/ - Eliminar una lista.
Productos:
GET /products/ - Listar productos.
POST /products/ - Crear un producto.
PUT /products/<id>/ - Actualizar un producto.
DELETE /products/<id>/ - Eliminar un producto.
Consulta la documentación completa en:

http://127.0.0.1:8000/swagger/
http://127.0.0.1:8000/redoc/
(si está habilitada).

Pruebas ✅
Para ejecutar las pruebas automatizadas:

bash
Copiar código
python manage.py test
Contribución 🤝
¡Las contribuciones son bienvenidas! Por favor, sigue estos pasos:

Haz un fork del repositorio.
Crea una rama para tu funcionalidad:
bash
Copiar código
git checkout -b feature/nueva-funcionalidad
Realiza tus cambios y confirma los commits:
bash
Copiar código
git commit -m "Descripción del cambio"
Envía tu rama al repositorio remoto:
bash
Copiar código
git push origin feature/nueva-funcionalidad
Abre un Pull Request explicando tus cambios.
Licencia 📄
Este proyecto está bajo la licencia MIT.

Contacto 📬
Desarrollador: Mariano Marina
Email: marianomarina@example.com
LinkedIn: linkedin.com/in/marianomarina

Si tienes alguna duda o sugerencia, no dudes en contactarme.
