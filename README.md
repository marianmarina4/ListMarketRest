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


## Uso de la API

### Autenticación

La API utiliza JWT para la autenticación. Primero, obtén un token enviando una solicitud POST a:


### Endpoints principales

#### Listas de compras:

- **GET** `/shopping/` - Listar listas visibles.
- **POST** `/shopping/` - Crear una lista.
- **PUT** `/shopping/<id>/` - Actualizar una lista.
- **DELETE** `/shopping/<id>/` - Eliminar una lista.

#### Productos:

- **GET** `/products/` - Listar productos.
- **POST** `/products/` - Crear un producto.
- **PUT** `/products/<id>/` - Actualizar un producto.
- **DELETE** `/products/<id>/` - Eliminar un producto.

Consulta la documentación completa en [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) o [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/) (si está habilitada).

## Pruebas

Para ejecutar las pruebas automatizadas:

```bash
python manage.py test

## Contribución

¡Las contribuciones son bienvenidas! Por favor, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y confirma los commits (`git commit -m "Descripción del cambio"`).
4. Envía tu rama al repositorio remoto (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request explicando tus cambios.

## Licencia

Este proyecto está bajo la licencia MIT.

## Contacto

Desarrollador: Mariano Marina  
Email: marianomarina@example.com  
LinkedIn: [linkedin.com/in/marianomarina](https://linkedin.com/in/marianomarina)  

Si tienes alguna duda o sugerencia, no dudes en contactarme.

