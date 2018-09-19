from django.db import models

class Hobbies(models.Model):
    # La mension "pass" est à supprimer
    # Le but de cet exercice est de créer un modèle pour la table 
    # "Hobbies"
    # Deux champs sont à créer, un champ nommé "type_hobby" et 
    # un autre nommé "description". Le premier doit être une chaîne de
    # caractères d'une longueur maximale de 100 caractères et le second
    # est une chaîne de caractère longue
    pass

    def __str__(self):
        return self.type_hobby

class Formateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    hobbies = models.ForeignKey(Hobbies, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nom} {self.prenom}'

class Apprenant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    hobbies = models.ForeignKey(Hobbies, on_delete=models.CASCADE)
    formateur = models.ForeignKey(Formateur, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nom} {self.prenom}'
