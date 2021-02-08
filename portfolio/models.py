from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Titulo')
    abstract = models.TextField(verbose_name="Resumen")
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen', upload_to='projects')
    background = models.ImageField(verbose_name='Fondo', upload_to='projects')
    link = models.CharField(max_length=250, verbose_name='Enlace')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['created']

    def __str__(self):
        return self.title