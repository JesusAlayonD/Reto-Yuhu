 # Reto: Sistema de Gestión de Tareas con Django y PostgreSQL
 ## Por Jesús Alayón Domínguez

El objetivo de este desafío es evaluar las habilidades del candidato en el desarrollo
de aplicaciones backend utilizando el framework Django en Python y una base de
datos PostgreSQL. Debes crear un sistema de gestión de tareas que permita a los
usuarios realizar las siguientes operaciones:
1. Crear una nueva tarea con un título, un email y una descripción.
2. Leer la lista de tareas existentes.
3. Actualizar una tarea existente (modificar el título o la descripción).
4. Eliminar una tarea existente.


### API Pública
Realicé una API pública para el uso de los endpoints de manera externa.

**Documentación de API: https://www.postman.com/cloudy-desert-43082/reto-yuhu/documentation/laj84gp/challenge-tasks?workspaceId=3dc57c25-7c12-4178-9353-e2604092cee9**

### Notificaciones Asíncronas
Realicé un proceso de correo electrónico asíncrono gracias a Celery y Redis, el proceso se ejecuta en segundo plano para realizar la operación en cuanto se necesite de manera asíncrona. Esto ocurre cuando se crea una nueva tarea.

### AWS
Subí el proyecto para su prueba en una instancia de AWS EC2.
http://54.82.215.194/

### .ENV
Existen ciertos datos que manejé con .env
- DB_NAME=challenge
- DB_USER=
- DB_PASSWORD=
- DB_HOST=localhost
- DB_PORT=5432  
- EMAIL=
- EMAIL_PASSWORD=
