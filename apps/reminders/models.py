from django.db import models

from datetime import datetime

from apps.users.models import User
from apps.templates.models import Template

# Create your models here.

class AlertMethod(models.Model):

    TYPE_CHOICES = (
        (0, 'Email'),
        (1, 'Message')
    )

    type = models.IntegerField(choices=TYPE_CHOICES, default=0, unique=True)

    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return '%s' % (self.type, )

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        super(AlertMethod, self).save(*args, **kwargs)

class Reminder(models.Model):

    user = models.ForeignKey(User)
    alert_at = models.DateTimeField()
    template = models.ForeignKey(Template, blank=True, null=True) # Pre-saved templates
                                                                  # Custom type available to input personal message
    message = models.CharField(max_length=254, blank=True, null=True) # Only available in custom template
    method = models.ManyToManyField(AlertMethod)

    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return '%s: %s %s' % (self.user_id, self.alert_at, self.method.all())

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        super(Reminder, self).save(*args, **kwargs)