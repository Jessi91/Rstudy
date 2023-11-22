from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import redirect, render
from .models import GroupeEtude, MembresGroupe
from django.contrib.auth import get_user_model as User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from user.models import User





# Create your views here.
def index(request):
    return render(request, 'home/index.html')

@login_required
def creer_groupe(request):
    if request.method == 'POST':
        nom_groupe = request.POST.get('nom_groupe')
        description = request.POST.get('description', '')
        
        # Créer le groupe
        nouveau_groupe = GroupeEtude.objects.create(_nom_groupe=nom_groupe, _description=description)

        # Ajouter l'utilisateur comme administrateur du groupe
        MembresGroupe.objects.create(_user=request.user, _groupe=nouveau_groupe, _role_groupe='admin')

        return redirect('liste_groupes')  # Rediriger vers la liste des groupes
    return render(request,  'FeatureAhmed/creer_groupe.html')

@login_required
def liste_groupes(request):
    groupes = GroupeEtude.objects.all()
    return render(request, 'FeatureAhmed/liste_groupes.html', {'groupes': groupes})


@login_required
def inviter_amis(request, groupe_id):
    try:
        groupe = GroupeEtude.objects.get(pk=groupe_id)
    except GroupeEtude.DoesNotExist:
        raise Http404("Le groupe n'existe pas.")

    if request.method == 'POST':
        amis_ids = request.POST.getlist('amis')
        
        # Ajouter les amis au groupe avec le rôle 'user'
        for ami_id in amis_ids:
            ami = User.objects.get(pk=ami_id)
            groupe.add_user(ami)

        return redirect('liste_groupes')

    # Récupérer les membres du groupe
    membres_du_groupe = MembresGroupe.objects.filter(_groupe=groupe)
    amis = User.objects.exclude(id__in=membres_du_groupe.values('_user_id'))

    
    return render(request, 'FeatureAhmed/inviter_amis.html', {'groupe': groupe, 'amis': amis})


# @login_required
# def inviter_amis(request, groupe_id):
#     try:
#         groupe = GroupeEtude.objects.get(pk=groupe_id)
#     except GroupeEtude.DoesNotExist:
#         raise Http404("Le groupe n'existe pas.")

#     if request.method == 'POST':
#         amis_ids = request.POST.getlist('amis')
        
#         # Ajouter les amis au groupe avec le rôle 'user'
#         for ami_id in amis_ids:
#             ami = User.objects.get(pk=ami_id)
#             MembresGroupe.objects.create(_user=ami, _groupe=groupe, _role_groupe='user')

#         return redirect('liste_groupes')

#     # Exclure les amis déjà dans le groupe
#     amis = User.objects.exclude(membresgroupe__groupe=groupe)
    
#     return render(request, 'FeatureAhmed/inviter_amis.html', {'groupe': groupe, 'amis': amis})
