# -*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import csv
from time import gmtime, strftime, sleep


def Scraper(address, tipo, nome):
    
    i = 1
    running = True
    salas = []

    while running:
        url = f"https://www.vivareal.com.br/aluguel/sp/sao-paulo/{address}/{tipo}/?pagina={i}#ordenar-por=preco:ASC"
  
        i+=1
  
        ua = UserAgent()
        userAgent = ua.random

        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument(f'user-agent={userAgent}')
  
  
  
        driver = webdriver.Chrome(executable_path='<PATH>/chromedriver.exe', options=options)  
        driver.get(url)
        sleep(4)
      
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        article = soup.find_all('article')
  
        data_extracao = strftime("%d%b%Y", gmtime()) 
  
  
        for index, res in zip(range(36), article):
          sala = []
          try:
            sala.append(res.find('div', class_="property-card__price js-property-card-prices js-property-card__price-small").text.split()[1].replace('.',''))
            sala.append(res.find('span', class_="property-card__detail-value js-property-card-value property-card__detail-area js-property-card-detail-area").text.split()[0])
            sala.append(res.find('span', class_="property-card__address").text)
            sala.append(res.find('a', class_="property-card__labels-container js-main-info js-listing-labels-link")['href'].split('-')[-1].replace("/", ""))
            sala.append(data_extracao)
            sala.append(nome)
          except:
            pass 
          if salas == []:
              salas.append(sala)
          elif sala == salas[0]:
              running = False
              driver.quit()
              break
          else:
              salas.append(sala)
        driver.quit()      
    
   
    
    with open(f'<PATH>/{nome}{data_extracao}.csv', 'w', newline='') as f:
        writer = csv.writer(f,)
        writer.writerow(["preco", "metros_quadrados", "endereco", "id", "data", "regiao"])
        writer.writerows(salas)


        

if __name__ == '__main__':
    main() 