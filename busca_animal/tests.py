from django.test import LiveServerTestCase
from selenium import webdriver

class AnimaisTestCase(LiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome('D:\Suenilton\Pessoal\Projetos Python\Projeto TDD\chromedriver.exe')

    def tearDown(self):
        self.browser.quit()

    def test_verificacao_janela_browser(self):
        self.browser.get(self.live_server_url)