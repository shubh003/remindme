from django.db import models

from datetime import datetime

# Create your models here.
class User(models.Model):

    title = models.CharField(max_length=4, blank=True, null=True)
    first_name = models.CharField(max_length=32, blank=True, null=True)
    last_name = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=64, unique=True)
    mobile_no = models.IntegerField(blank=True, null=True, unique=True)

    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return "%s: %s %s" % (self.id, self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        super(User, self).save(*args, **kwargs)