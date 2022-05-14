from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from animais.models import Animais

class AnimaisVIEWSTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.animal = Animais.objects.create(
            nome_animal = 'Tigre',
            predador = 'Sim',
            venenoso = 'Não',
            domestico = 'Não'
        )

    def test_index_views_retorna_caracteristicas_animais(self):
        """Verifica se a views retorna as caracteristicas do animal"""
        
        response = self.client.get('/', 
            {'buscar': 'Tigre'}
        )
        caracteristica_animal_pesquisado = response.context['caracteristicas']
        self.assertIs(type(response.context['caracteristicas']), QuerySet)
        self.assertEqual(caracteristica_animal_pesquisado[0].nome_animal, 'Tigre')