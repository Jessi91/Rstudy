from django.test import TestCase
from .models import Forum, ParticipationForum
from django.contrib.auth import get_user_model

class ForumTestCase(TestCase):
    def setUp(self):
        # Obtention du modèle utilisateur
        User = get_user_model()

        # Création d'un utilisateur
        self.user = User.objects.create_user(email='test@example.com', password='password', role='etudiant')

        # Création d'un forum
        self.forum = Forum.objects.create(
            nom="Forum de Test",
            description="Description du Forum de Test",
            ouvert=True
        )

        # Création d'une participation au forum
        ParticipationForum.objects.create(
            user=self.user,
            forum=self.forum,
            titre_msg="Titre du message",
            contenu="Contenu du message"
        )

    def test_forum_creation(self):
        """ Teste la création d'un forum """
        self.assertEqual(self.forum.nom, "Forum de Test")
        self.assertEqual(self.forum.description, "Description du Forum de Test")
        self.assertTrue(self.forum.ouvert)

    def test_participation_forum(self):
        """ Teste la création d'une participation au forum """
        participation = ParticipationForum.objects.get(forum=self.forum, user=self.user)
        self.assertEqual(participation.titre_msg, "Titre du message")
        self.assertEqual(participation.contenu, "Contenu du message")

    def test_forum_delete(self):
        """ Teste la suppression d'un forum et ses participations associées """
        forum_id = self.forum.id_forum
        self.forum.delete()

        with self.assertRaises(Forum.DoesNotExist):
            Forum.objects.get(id_forum=forum_id)

        self.assertFalse(ParticipationForum.objects.filter(forum__id_forum=forum_id).exists())
