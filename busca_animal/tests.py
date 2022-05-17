from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from animais.models import Animais

class AnimaisTestCase(LiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome('D:\Suenilton\Pessoal\Projetos Python\Projeto TDD\chromedriver.exe')
        self.animal = Animais.objects.create(
            nome_animal = 'Leão',
            predador = 'Sim',
            venenoso = 'Não',
            domestico = 'Não'
        )
    def tearDown(self):
        self.browser.quit()

    def test_buscando_um_novo_animal(self):
        """Verifica se o usuário consegue encontrar o animal pesquisado."""

        # Vini deseja encontrar um novo animal
        # para adotar

        # Ele encontra o Busca Animal e decide usar o site
        home_page = self.browser.get(self.live_server_url + '/')
        # porque ele vê no menu do site escrito Busca Animal.
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual('Busca Animal', brand_element.text)

        # Ele vê um campo para pesquisar animais pelo nome.
        buscar_animal_input = self.browser.find_element(By.CSS_SELECTOR, 'input#buscar-animal')
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'),'Exemplo: leão')
        # Ele pesquisa por leão e clica no botão pesquisar.
        buscar_animal_input.send_keys('leão')
        time.sleep(2)
        self.browser.find_element(By.CSS_SELECTOR, 'form button').click()
        # O site exibe quatro caracteristicas do animal pesquisado.
        caracteristicas = self.browser.find_elements(By.CSS_SELECTOR, 'div.result-description')
        self.assertGreater(len(caracteristicas), 3)
        # Ele desiste de adotar um leão.