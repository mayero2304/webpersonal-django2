from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=140, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to= "projects")
    url = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    update = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

    class Meta:
        verbose_name = "proyecto"
        # verbose_name_plural = "proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title
