from django.db import models


# Create your models here.
class Timer(models.Model):
    start = models.PositiveIntegerField()
    end = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return '{}-{}'.format(self.start, self.end)

    class Meta:
        verbose_name = 'Timer'
        verbose_name_plural = 'Timers'
