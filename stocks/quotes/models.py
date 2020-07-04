from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField('Project name', max_length=50)
    description = models.CharField('Description', max_length=255)
    image = models.ImageField('Project image', upload_to='project/')

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name