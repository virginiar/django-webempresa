# Proyecto de web empresarial en Django
Proyecto intermedio para practicar Django, basado en la creación de una web de presentación de una cafetería con varias secciones dinámicas manejadas desde el panel del administrador.
Basado en el curso [Curso Práctico de Django: Desarrollo Web Backend con Python](udemy.com/course/curso-django-2-practico-desarrollo-web-python-3/).

Conceptos utilizados:
- Creación de aplicaciones para modularizar el proyecto
- Separando rutas en URLconf para cada aplicación
- Fusionando el frontend y el backend
- Resaltando la sección actual en la navegación
- Sirviendo archivos multimedia
- Relaciones entre modelos
- Personalizando el administrador:
  - Columnas a mostrar
  - Orden
  - Campos de búsqueda
  - Jerarquía de fechas
  - Filtros
  - Campos personalizados
  - Editor WYSIWYG: Ckeditor
- Template tags date y linebreaks
- Parámetros dinámicos
- Gestión de errores con accesor get_object_or_404
- Uso de related_name en relaciones ManyToMany para búsquedas inversas
- Uso de slice
- Procesadores de contexto
- Template tags propios
- Orden manual de campos
- Edición directa de páginas
- Formularios
  - Procesado y validación

## Instalación con Pipenv
- Instalación de paquetes
```bash
pipenv install django django-ckeditor Pillow pylint pylint-django pylint-celery
```

- Creación del proyecto
```bash
pipenv run django-admin startproject django-webempresa
```

## Ejecución del proyecto
- Ejecución directa
```bash
pipenv run python django-webempresa/manage.py runserver
```

- Añadiendo script en Pipfile
```bash
[scripts]
webempresa = "python django-webempresa/manage.py runserver"
```

La ejecución se realiza con:
```bash
pipenv run webempresa
```

## Creación de aplicaciones
- Creación de una aplicación
```bash
python manage.py startapp core
```

## Creación de modelos
- Creación de una aplicación
```bash
python manage.py startapp services
```

- Ejecución de la migración
```bash
python manage.py makemigrations
```

- Aplicación de la migración a la base de datos
```bash
python manage.py migrate
```

- Creación del superusuario
```bash
python manage.py createsuperuser
```
