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


class sem1(models.Model):
    sub_name = models.CharField(max_length=50)
    files = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.sub_name

    class Meta:
        verbose_name_plural = "Sem-1"


class sem2(models.Model):
    sub_name = models.CharField(max_length=50)
    files = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.sub_name

    class Meta:
        verbose_name_plural = "Sem-2"


class sem3(models.Model):
    sub_name = models.CharField(max_length=50)
    files = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.sub_name

    class Meta:
        verbose_name_plural = "Sem-3"


class sem4(models.Model):
    sub_name = models.CharField(max_length=50)
    files = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.sub_name

    class Meta:
        verbose_name_plural = "Sem-4"


class sem5(models.Model):
    sub_name = models.CharField(max_length=50)
    files = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.sub_name

    class Meta:
        verbose_name_plural = "Sem-5"


class sem6(models.Model):
    sub_name = models.CharField(max_length=50)
    files = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.sub_name

    class Meta:
        verbose_name_plural = "Sem-6"
