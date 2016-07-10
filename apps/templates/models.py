from django.db import models

from datetime import datetime

# Create your models here.
class TemplateVariable(models.Model):

    name = models.CharField(max_length=32, unique=True)

    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        super(TemplateVariable, self).save(*args, **kwargs)

class Template(models.Model):

    text = models.TextField()
    variables = models.ManyToManyField(TemplateVariable)

    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        super(Template, self).save(*args, **kwargs)
