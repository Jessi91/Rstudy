from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader

from school.form import EspacePersonnelForm
from .models import EspacePersonnel, Formation, Matiere, Enseignement
from django.contrib.auth.models import User
from user.models import User
from home.models import Formation, Enseignement, Matiere
#from school.models import Formation




def school(request):
    template = loader.get_template('school/first.html')
    return HttpResponse(template.render())

# def index(request):
#     return render(request, 'home/index.html')



def test_view(request):
    # Création d'une formation
    admin_user, created = User.objects.get_or_create(username='admin', defaults={'password': 'your_password'})
     # Utilisez la classe Formation pour appeler create_formation, pas une instance
    nouvelle_formation = Formation.create_formation(_nom='Nouvelle Formation', _description='Description de la formation', _type='Licence', _duree_mois=24, _responsable=admin_user)

    # Ajout de matières à la formation
    nouvelle_formation.add_matiere(nom_matiere='Matiere 1', description_matiere='Description matiere 1', duree_matiere='02:00:00', autres_informations='Autres infos')

    # Attribution d'un enseignant à une matière
    professeur_user = User.objects.get(username='professeur')  # Assurez-vous de remplacer 'professeur' par le nom d'utilisateur réel du professeur
    matieres = Matiere.objects.filter(_nom='Matiere 1')

    if matieres.exists():
        matiere_1 = matieres.first()
    else:
        # Créez la matière si elle n'existe pas
        matiere_1 = Matiere.objects.create(_nom='Matiere 1', _description='Description matiere 1', _duree='02:00:00', _autres_informations='Autres infos')

    nouvelle_formation.assign_enseignant(professeur=professeur_user, matiere=matiere_1, groupe_td=1)

    # Récupération des informations pour affichage
    formations = Formation.objects.all()
    matieres = Matiere.objects.all()
    enseignements = Enseignement.objects.all()

    context = {
        'formations': formations,
        'matieres': matieres,
        'enseignements': enseignements,
    }

    return render(request, 'school/test_template.html', context)


#@login_required
def espace_personnel(request):
    espace_personnel, created = EspacePersonnel.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = EspacePersonnelForm(request.POST, instance=espace_personnel)
        if form.is_valid():
            form.save()
            return redirect('espace_personnel')
    else:
        form = EspacePersonnelForm(instance=espace_personnel)

    return render(request, 'school/espace_personnel.html', {'form': form})