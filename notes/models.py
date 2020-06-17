from django.db import models


# Create your models here.

class chemisrty(models.Model):
    sub_name = models.CharField(max_length=50)
    files = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.sub_name

    class Meta:
        verbose_name_plural = "Chemistry"


class botany(models.Model):
    sub_name = models.CharField(max_length=50)
    files = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.sub_name

    class Meta:
        verbose_name_plural = "Botany"


class zoology(models.Model):
    sub_name = models.CharField(max_length=50)
    files = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.sub_name

    class Meta:
        verbose_name_plural = "Zoology"
