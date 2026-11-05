# Proyecto de web empresarial en Django
Proyecto intermedio para practicar Django, basado en la creación de una web de presentación de una cafetería con varias secciones dinámicas manejadas desde el panel del administrador.
Basado en el curso [Curso Práctico de Django: Desarrollo Web Backend con Python](udemy.com/course/curso-django-2-practico-desarrollo-web-python-3/).

Conceptos utilizados:
- Creación de aplicaciones para modularizar el proyecto
- Separando rutas en URLconf para cada aplicación
- Fusionando el frontend y el backend
- Resaltando la sección actual en la navegación
- Sirviendo archivos multimedia

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