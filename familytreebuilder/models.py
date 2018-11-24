from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.


class CustomUser(AbstractUser):
    username = models.CharField(max_length=40, unique=True, verbose_name="Login")
    email = models.EmailField()
    last_update = models.DateTimeField(auto_now=True)

    def update(self):
        self.last_update = timezone.now
        self.save()

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

    def update(self):
        self.last_update = timezone.now
        self.save()

    def inc_size(self):
        self.size += 1
        self.update()

    def set_name(self, new_name):
        self.name = new_name
        self.update()

    def set_photo_path(self, new_photo_path):
        self.photo = new_photo_path
        self.update()

    def __str__(self):
        return self.name


class Member(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, help_text='Imiona')
    last_name = models.CharField(max_length=40, help_text='Nazwisko')
    birth_date = models.DateField(help_text='Datę narodzin', blank=True, null=True)
    death_date = models.DateField(help_text='Datę śmierci', blank=True, null=True)
    alive = models.BooleanField(help_text='Nieżyje?')
    phone_number = models.CharField(max_length=15, help_text='Numer telefonu', blank=True, null=True)
    photo = models.ImageField(upload_to='pictures', null=True)
    last_update = models.DateTimeField(auto_now=True)

    def update(self):
        self.last_update = timezone.now
        self.save()

    def set_name(self, new_name):
        self.name=new_name
        self.update()

    def set_last_name(self, new_last_name):
        self.last_name = new_last_name
        self.update()

    def set_birth_date(self, new_birth_date ):
        self.birth_date = new_birth_date
        self.update()

    def set_death_date(self, new_death_date ):
        self.birth_date = new_death_date
        self.update()

    def set_alive(self, is_alive):
        self.alive = is_alive
        self.update()

    def set_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number
        self.update()

    def set_photo_path(self, new_photo_path):
        self.photo = new_photo_path
        self.update()

    def __str__(self):
        return self.name + ' ' + self.last_name


class Address(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, help_text='Adres', blank=True, null=True)
    zip_code = models.CharField(max_length=10,  help_text='Kod pocztowy', blank=True, null=True)
    city = models.CharField(max_length=40, help_text='Miasto', blank=True, null=True)
    last_update = models.DateTimeField(auto_now=True)

    def update(self):
        self.last_update = timezone.now
        self.save()

    def set_address(self, new_address):
        self.address=new_address
        self.update()

    def set_zip_code(self, new_zip_code):
        self.zip_code = new_zip_code
        self.update()

    def set_city(self, new_city):
        self.city = new_city

    def __str__(self):
        return "{} {} {}".format(self.address, self.zip_code, self.city)


class Parent(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)


class Spouse(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)
