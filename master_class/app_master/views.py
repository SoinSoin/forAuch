from django.shortcuts import render
from django.contrib import messages
from django.db import connection


from .models import (Apprenant, Formateur, Hobbies)
from .forms import (HobbiesForm,)


def accueil(request):
    if request.method == 'POST':
        form = HobbiesForm(request.POST)
        
        if form.is_valid():
            try:
                form.save()
                messages.add_message(
                    request, 
                    messages.SUCCESS, 
                    'Vous avez créé un nouveau hobby avec succès'
                )
            except:
                # Le but de cet exercice sera de gérer le cas
                # où les données du formulaire ne sont pas valides.
                # La mension "pass" est à supprimer.
                # Vous devez renvoyer un message d'erreur.
                pass
                
    
    else:
        form = HobbiesForm()


    hobbies = Hobbies.objects.all()
    
    return render(request, 'accueil.html', {
        'form':form, 
        'hobbies':hobbies,        
    })

