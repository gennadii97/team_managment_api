from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    team = models.ForeignKey(Team, related_name="members", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.surname} {self.name}'
