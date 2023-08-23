from django.db import models

# Create your models here.
class ListTest(models.Model):
    name = models.CharField(
        max_length=256,
        blank=False,
        help_text=' ListTest name',
        verbose_name='ListTest name'
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.id}"

    class Meta:
        verbose_name = 'ListTest'
        verbose_name_plural = 'ListTests'
        ordering = ['name']
