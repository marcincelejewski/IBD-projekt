from django.contrib.auth.models import AbstractUser
from django.db import models
from image_optimizer.fields import OptimizedImageField

# Create your models here.


class CustomUser(AbstractUser):
    username = models.CharField(max_length=40, unique=True, verbose_name="Login")
    email = models.EmailField()
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Family(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=60, verbose_name='Nazwa drzewa')
    size = models.PositiveSmallIntegerField(default=0)
    photo = OptimizedImageField(upload_to='pictures', verbose_name='Wybierz zdjęcie', null=True, blank=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def inc_size(self):
        self.size += 1
        self.save()


class Address(models.Model):
    address = models.CharField(max_length=50, verbose_name='Adres', blank=True, null=True)
    zip_code = models.CharField(max_length=10, verbose_name='Kod pocztowy', blank=True, null=True)
    city = models.CharField(max_length=40, verbose_name='Miasto', blank=True, null=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {} {}".format(self.address, self.zip_code, self.city)


class Member(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, verbose_name='Imiona')
    last_name = models.CharField(max_length=40, verbose_name='Nazwisko')
    parents = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='children')
    spouses = models.ManyToManyField('self', blank=True)
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    birth_date = models.DateField(verbose_name='Data narodzin', blank=True, null=True)
    death_date = models.DateField(verbose_name='Data śmierci', blank=True, null=True)
    alive = models.BooleanField(verbose_name='Żyje?', blank=True, null=True)
    phone_number = models.CharField(max_length=15, verbose_name='Numer telefonu', blank=True, null=True)
    photo = OptimizedImageField(upload_to='pictures', verbose_name='Wybierz zdjęcie', blank=True, null=True)
    generation = models.SmallIntegerField(null=False, default=1)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['generation']

    def __str__(self):
        return f'{self.name} {self.last_name}'
