from django.test import TestCase, RequestFactory
from animais.models import Animais

class AnimaisMODELSTestCase(TestCase):

    def setUp(self):
        self.animal = Animais.objects.create(
            nome_animal = 'Leão',
            predador = 'Sim',
            venenoso = 'Não',
            domestico = 'Não'
        )

    def test_animal_cadastrado_com_caracteristicas(self):
        """Verifica se o animal está cadastrado com suas respectivas caracterisiticas"""
        self.assertEqual(self.animal.nome_animal, 'Leão')