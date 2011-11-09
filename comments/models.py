from django.db import models

# Create your models here.

class Comment(models.Model):
    parent = models.ForeignKey('self', related_name='children', blank=True, null=True)
    text = models.TextField()

    def __unicode__(self):
        return self.text
