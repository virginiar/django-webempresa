from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    content = CKEditor5Field(verbose_name="Contenido", config_name='extends')
    order = models.SmallIntegerField(default=0, verbose_name="Orden")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ["order", "-title"]

    def __str__(self):
        return self.title
