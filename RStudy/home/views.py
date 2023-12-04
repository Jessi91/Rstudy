from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import redirect, render
from .models import GroupeEtude, MembresGroupe
from django.contrib.auth import get_user_model as User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from user.models import User
from .models import Invitation





# Create your views here.
def index(request):
    return render(request, 'home/index.html')

@login_required
def creer_groupe(request):
    if request.method == 'POST':
        nom_groupe = request.POST.get('nom_groupe')
        description = request.POST.get('description', '')
        
        # Créer le groupe
        nouveau_groupe = GroupeEtude.objects.create(nom_groupe=nom_groupe, description=description)

        # Ajouter l'utilisateur comme administrateur du groupe
        MembresGroupe.objects.create(user=request.user, groupe=nouveau_groupe, role_groupe='admin')

        return redirect('liste_groupes')  # Rediriger vers la liste des groupes
    return render(request,  'FeatureAhmed/creer_groupe.html')



@login_required
def liste_groupes(request):
    groupes = GroupeEtude.objects.all()
    return render(request, 'FeatureAhmed/liste_groupes.html', {'groupes': groupes})




@login_required
def inviter_amis(request, id):
    try:
        groupe = GroupeEtude.objects.get(pk=id)
    except GroupeEtude.DoesNotExist:
        raise Http404("Le groupe n'existe pas.")

    # Récupérer la liste des amis (utilisateurs) disponibles à inviter
    amis = User.objects.exclude(pk=request.user.id).exclude(membresgroupe__groupe=groupe)

    if request.method == 'POST':
        amis_ids = request.POST.getlist('amis')
        
        # Ajouter les amis au groupe avec le rôle 'user'
        for ami_id in amis_ids:
            ami = User.objects.get(pk=ami_id)

            # Créer une invitation
            Invitation.objects.create(groupe=groupe, invitant=request.user, invite=ami, statut='en_attente', droit_acces='contributor')

        return redirect('liste_groupes')

    return render(request, 'FeatureAhmed/inviter_amis.html', {'groupe': groupe, 'amis': amis})



    # Récupérer les membres du groupe
    membres_du_groupe = MembresGroupe.objects.filter(_groupe=groupe)
    amis = User.objects.exclude(id__in=membres_du_groupe.values('_user_id'))

    
    return render(request, 'FeatureAhmed/inviter_amis.html', {'groupe': groupe, 'amis': amis})

@login_required
def accepter_invitation(request, invitation_id):
    invitation = get_object_or_404(Invitation, id=invitation_id, invite=request.user, statut='en_attente')
    invitation.statut = 'accepte'
    invitation.save()
    # Implémentez la logique d'attribution des droits d'accès ici
    return redirect('nom_de_la_vue_appropriee')

@login_required
def refuser_invitation(request, invitation_id):
    invitation = get_object_or_404(Invitation, id=invitation_id, invite=request.user, statut='en_attente')
    invitation.statut = 'refuse'
    invitation.save()
    return redirect('nom_de_la_vue_appropriee')