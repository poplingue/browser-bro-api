from django.db import models

# Create your models here.

class Custom(models.Model):
    value = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.value, self.title)
