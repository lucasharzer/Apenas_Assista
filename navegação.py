from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import dotenv
import os


def Navegacao():

    try:
        dotenv.load_dotenv(dotenv.find_dotenv())
        url = str(os.getenv("URL"))
        path_image = str(os.getenv("PATH_IMAGE"))

        driver = webdriver.Chrome(executable_path="./chromedriver.exe")

        driver.get(url)

        driver.maximize_window()

        try:
            concordo = driver.find_element_by_xpath(
                "/html/body/div/div[5]/div[3]/div[2]/button[1]/div/span")
            concordo.click()
        except:
            print("O botão concordo não apareceu.")

        while True:
            try:
                busca = driver.find_element_by_xpath(
                    "/html/body/div/div[3]/div/div[2]/div[1]/div/ion-searchbar/div/input")

                if busca:
                    busca.send_keys("Anônimo 2021")
                    sleep(1)
                    busca.send_keys(Keys.ENTER)
                    sleep(1)
                    break
            except:
                pass
        
        while True:
            try:
                nome = driver.find_elements_by_class_name("title-list-row__row-header-title")[0].text

                if nome:
                    sleep(1)
                    break
            except:
                pass
        
        classe = driver.find_element_by_xpath(
            "/html/body/div/div[4]/div[3]/div/div[2]/ion-grid/div/ion-row[1]/ion-col[2]/a")
        filme = classe.get_attribute("href")

        driver.get(filme)
        
        while True:
            try:
                titulo_br = driver.find_element_by_xpath(
                    "/html/body/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/h1").text
                if titulo_br:
                    sleep(1)
                    break
            except:
                pass

        titulo_original = driver.find_element_by_xpath(
            "/html/body/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/div[1]/h3").text

        ano = driver.find_element_by_xpath(
            "/html/body/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/span").text[1:-1]
        
        sinopse = driver.find_element_by_xpath(
            "/html/body/div/div[4]/div[2]/div/div[2]/div[2]/div[5]/div[1]/div[4]/p/span").text

        arquivo = open(path_image, 'w')

        arquivo.write(f"Ano: {ano}\n")
        arquivo.write(f"{titulo_original}\n")
        arquivo.write(f"Sinopse: {sinopse}\n")
        arquivo.close()

        print("\033[1;32mConteúdo:\033[m\n")

        arquivo = open(path_image, 'r')
        for linha in arquivo:
            linha = linha.rstrip()
            print(f"\033[1;35m{linha}\033[m")
        arquivo.close()

        driver.close()
    except:
        print("\033[1;31mAlgum erro ocorreu\033[m")
    finally:
        print("\033[1;32m\nProcesso finalizado\033[m")
