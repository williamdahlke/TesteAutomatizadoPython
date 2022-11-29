from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def testeAutomatizadoSelenium():
    try:
        #cria o objeto da classe webdriver
        driver = webdriver.Chrome()
        driver.get("http://grupovirtuous.com.br/matkids/game.php")

        #aplica o nome para o jogador
        driver.find_element_by_name("nome").send_keys("William")
        #clica para avançar
        driver.find_element_by_name("envia").click()

        #procura na tela elementos com a tag b
        lista_parcelas = driver.find_elements_by_tag_name("b")

        #pega os valores aleatórios indicados na tela e realiza a operação matemática
        parcela1 = int(lista_parcelas[3].text)
        parcela2 = int(lista_parcelas[4].text)
        soma = parcela1 + parcela2
        #Coloca o valor da soma no campo resposta e clica no botão enviar
        driver.find_element_by_name("resposta").send_keys(soma)
        driver.find_element_by_name("envia").click()

        #Destrói o objeto
        driver.close        
    except:
        print("Não é possível executar o Chrome Driver e/ou acessar a página desejada. Favor verificar!")
 
testeAutomatizadoSelenium()
