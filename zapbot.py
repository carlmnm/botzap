from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = "alo alo graças a deus se o mundo existe pq ele existe?"
        self.grupos = ["hori shitoro"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    def EnviarMensagens(self):
        # <span dir="auto" title="hori shitoro" class="_3ko75 _5h6Y_ _3Whw5">hori shitoro</span>
        # <div tabindex="-1" class="_3uMse">
        # <span data-testid="send" data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com')
        time.sleep(10)

        grupo = self.driver.find_element_by_xpath("//span[@title='hori shitoro']")
        time.sleep(3)
        grupo.click()
        
        chatbox = self.driver.find_element_by_class_name('_3uMse')
        time.sleep(3)
        chatbox.click()
        
        chatbox.send_keys(self.mensagem)
        botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
        time.sleep(3)
        botao_enviar.click()

bot = WhatsappBot()
bot.EnviarMensagens()
