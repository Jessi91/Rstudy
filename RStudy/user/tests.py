from django.test import TestCase
from .models import User
from django.db import IntegrityError

class UserTestCase(TestCase):
    def test_user_creation(self):
        """ Teste la création d'un utilisateur avec des champs de base """
        user = User.objects.create(
            email="user@example.com",
            role='etudiant'
        )
        self.assertEqual(user.email, "user@example.com")
        self.assertEqual(user.role, 'etudiant')

    def test_unique_email_constraint(self):
        """ Teste la contrainte d'unicité pour l'email """
        User.objects.create(
            email="unique@example.com",
            role='enseignant'
        )
        with self.assertRaises(IntegrityError):
            User.objects.create(
                email="unique@example.com",
                role='tuteur'
            )

    def test_unique_phone_constraint(self):
        """ Teste la contrainte d'unicité pour le numéro de téléphone """
        User.objects.create(
            email="user1@example.com",
            num_tel=1234567890,
            role='etudiant'
        )
        with self.assertRaises(IntegrityError):
            User.objects.create(
                email="user2@example.com",
                num_tel=1234567890,
                role='enseignant'
            )
