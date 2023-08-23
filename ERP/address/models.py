from django.db import models

# Create your models here.
class District(models.Model):
    apskr_id = models.BigAutoField(primary_key=True)
    apskr_no = models.IntegerField(default=0, blank=False, help_text=' Apskrities numeris')
    apskr_name = models.CharField(
        max_length=256,
        blank=False,
        help_text=' Apskrities pavadinimas',
        verbose_name='Apskritis'
    )

    def __str__(self):
        return f"{self.apskr_name} {self.apskr_id}"

    class Meta:
        verbose_name = 'Apskritis'
        verbose_name_plural = 'Apskritys'
        ordering = ['apskr_name']


class Municipality(models.Model):
    sav_id = models.BigAutoField(primary_key=True)
    sav_name = models.CharField(
        max_length=256,
        blank=False,
        help_text=' Savivaldybės pavadinimas',
        verbose_name='Savivaldybė'
    )
    apskr_name = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name='Apskritis')

    def __str__(self):
        return f"{self.sav_name} {self.sav_id}"

    class Meta:
        verbose_name = 'Savivaldybė'
        verbose_name_plural = 'Savivaldybės'
        ordering = ['sav_name']


class Elderate(models.Model):
    sen_id = models.BigAutoField(primary_key=True)
    sen_name = models.CharField(
        max_length=256,
        blank=True,
        help_text=' Seniūnija',
        verbose_name='Seniūnija'
    )
    sav_name = models.ForeignKey(Municipality, on_delete=models.CASCADE, verbose_name='Savivaldybė')

    def __str__(self):
        return f"{self.sen_name} {self.sen_id}"

    class Meta:
        verbose_name = 'Seniūnija'
        verbose_name_plural = 'Seniūnijos'
        ordering = ['sen_name']


class City(models.Model):
    gyv_id = models.BigAutoField(primary_key=True)
    gyv_name = models.CharField(
        max_length=256,
        blank=False,
        help_text=' Savivaldybės pavadinimas',
        verbose_name='Savivaldybė'
    )
    sen_name = models.ForeignKey(Elderate, on_delete=models.CASCADE, verbose_name='Seniūnija')

    def __str__(self):
        return f"{self.gyv_name} {self.gyv_id}"

    class Meta:
        verbose_name = 'Gyvenvietė'
        verbose_name_plural = 'Gyvenvietės'
        ordering = ['gyv_name']


class Street(models.Model):
    active = models.BooleanField(default=True, verbose_name='Aktyvus')

    str_id = models.BigAutoField(primary_key=True)
    str_name = models.CharField(
        max_length=256,
        blank=False,
        help_text=' Gatvės pavadinimas',
        verbose_name='Gatvės pavadinimas'
    )
    gyv_name = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Gyvenvietė')

    def __str__(self):
        return f"{self.str_name} {self.str_id} {self.gyv_name}"

    class Meta:
        verbose_name = 'Gatvė'
        verbose_name_plural = 'Gatvės'
        ordering = ['str_name']


class Building(models.Model):
    active = models.BooleanField(default=True, verbose_name='Aktyvus')
    AOB_KODAS = models.BigAutoField(primary_key=True)
    NR = models.CharField(
        max_length=256,
        blank=False,
        help_text=' Namo numeris',
        verbose_name='Namo numeris'
    )
    KORPUSO_NR = models.CharField(
        max_length=256,
        blank=True,
        help_text=' Korpuso numeris',
        verbose_name='Korpuso numeris')
    PASTO_KODAS = models.CharField(
        max_length=256,
        blank=True,
        help_text=' Pašto kodas',
        verbose_name='Pašto kodas')

    str_name = models.ForeignKey(Street, on_delete=models.CASCADE, verbose_name='Gatvė')

    def __str__(self):
        return f"{self.NR}, {self.KORPUSO_NR}, {self.PASTO_KODAS}, {self.str_name}"

    class Meta:
        verbose_name = 'Namo informacija'
        verbose_name_plural = 'Namo informacija'
        ordering = ['NR', 'PASTO_KODAS']
