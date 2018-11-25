from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    username = models.CharField(max_length=40, unique=True, verbose_name="Login")
    email = models.EmailField()
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Family(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=60, help_text='Nazwa drzewa', blank=True, null=True)
    size = models.PositiveSmallIntegerField(default=0)
    photo = models.ImageField(upload_to='pictures', null=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Address(models.Model):
    address = models.CharField(max_length=50, help_text='Adres', blank=True, null=True)
    zip_code = models.CharField(max_length=10,  help_text='Kod pocztowy', blank=True, null=True)
    city = models.CharField(max_length=40, help_text='Miasto', blank=True, null=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {} {}".format(self.address, self.zip_code, self.city)


class Member(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, verbose_name='Imiona')
    last_name = models.CharField(max_length=40, verbose_name='Nazwisko')
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    birth_date = models.DateField(verbose_name='Data narodzin', blank=True, null=True)
    death_date = models.DateField(verbose_name='Data śmierci', blank=True, null=True)
    alive = models.BooleanField(verbose_name='Nieżyje?')
    phone_number = models.CharField(max_length=15, verbose_name='Numer telefonu', blank=True, null=True)
    photo = models.ImageField(upload_to='pictures', null=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' ' + self.last_name


class Parent(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)


class Spouse(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)
