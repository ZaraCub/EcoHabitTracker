from django.db import models
from django.contrib.auth.models import User

class EkoloskaNavika(models.Model):
    naziv = models.CharField(max_length=100)
    opis = models.TextField()
    kategorija = models.CharField(max_length=50)

    def __str__(self):
        return self.naziv

class DnevnikEkoloskihAktivnosti(models.Model):
    datum = models.DateField()
    navika = models.ForeignKey(EkoloskaNavika, on_delete=models.CASCADE)
    opis = models.TextField()

    def __str__(self):
        return f"Aktivnost za {self.navika.naziv} na datum {self.datum}"

class Feedback(models.Model):
    navika = models.ForeignKey(EkoloskaNavika, on_delete=models.CASCADE)
    ocjena = models.IntegerField()
    komentar = models.TextField()

    def __str__(self):
        return f"Feedback za {self.navika.naziv}"

# Dodatni model za proširenje User modela, ako je potrebno
class Korisnik(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ekoloske_navike = models.ManyToManyField(EkoloskaNavika)

    def __str__(self):
        return self.user.username
