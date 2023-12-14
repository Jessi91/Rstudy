from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Formation, Matiere

class SimpleModelTestCase(TestCase):
    def setUp(self):
        User = get_user_model() 
        self.responsable = User.objects.create_user(email='responsable@example.com', password='password', role='enseignant')
        self.formation = Formation.objects.create(
            nom="Formation Test",
            type="Licence",
            duree_mois=12,
            responsable=self.responsable
        )
        self.matiere = Matiere.objects.create(
            nom="Matiere Test",
            duree="02:00"
        )

    def test_formation_creation(self):
        """ Teste la création d'une formation """
        self.assertEqual(self.formation.nom, "Formation Test")
        self.assertEqual(self.formation.type, "Licence")

    def test_matiere_creation(self):
        """ Teste la création d'une matière """
        self.assertEqual(self.matiere.nom, "Matiere Test")
