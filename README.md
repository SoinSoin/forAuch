# forAuch
Le but de l'exercice n'est pas forcément de le terminer mais d'aller le plus loin possible. 
A l'aide de la présentation de Nicolas ainsi que de la documentation que vous trouverez sur internet vous devriez pouvoir y arriver.
- MVC -> https://openclassrooms.com/fr/courses/4670706-adoptez-une-architecture-mvc-en-php/4678736-comment-fonctionne-une-architecture-mvc
- python3 -> https://docs.python.org/3/
- django -> https://docs.djangoproject.com/en/2.1/

L'dée est que votre application Web retourne la page suivante: 
![Alt text](forReadme/site.png?raw=true "Super Form")

Pour arriver à ce résultat nous vous mettons à disposition les fichiers nécessaire dans ce repository.

### Les commandes shell nécessaire
```
-  pour Linux/Mac:
$ python3 -m virtualenv nomEnv
$ source nomEnv/bin/activate 

-  pour Windows:
$ virtualenv nomEnv
$ source nomEnv/Scripts/activate

$ ./manage.py runserver -> pour lancer le serveur python
```

/!\ on vous dira quand utiliser les comandes en dessous :wink:
```
$ ./manage.py makemigrations 
$ ./manage.py migrate 
$ ./manage.py createsuperuser 
```

## Exercice 1 (Modèles)

Rendez vous dans le fichier app_master/models.py.
L'exercice consiste à recréer un model pour créer une table, vous trouverez plus d'information dans le fichier.
- NB: pour savoir ce qu'est un modèle voir la resource MVC plus haut ainsi que celle de Django(rubrique: 'The model layer').

## Exercice 2 (Routes)

Rendez vous dans le fichier Master/urls.py.
Cette fois vous dervrez construire une route qui retourne la vue de la page d'accueil,vous trouverez plus d'information dans le fichier.
- NB: pour savoir ce qu'est une route  voir la resource MVC plus haut ainsi que celle de Django(rubrique: 'The view layer/The basics/URLconf').

## Exercice 3 (Vue)

Rendez vous dans le fichier Master/views.py.
Le but est de gérer l'erreur qui surviendra si les données renvoyer pas le formulaire ne sont pas valide, vous trouverez plus d'information dans le fichier.
- NB: pour savoir ce qu'est une route  voir la resource MVC plus haut ainsi que celle de Django(rubrique: 'The view layer' ).

## Exercice 4 (Template)

Rendez vous dans le fichier app_master/templates/accueil.html.
Il faut compléter le template en rajoutant le champs manquant du formulaire, vous trouverez plus d'information dans le fichier.
- NB: pour savoir ce qu'est une route  voir la resource MVC plus haut ainsi que celle de Django(rubrique: 'The template layer' ).


:star: have fun !!! :star:
