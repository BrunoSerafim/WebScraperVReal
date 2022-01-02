# Web Scraper 
Script para extração de informação de imóveis de site da internet para criação de uma pipeline de dados do meu trabalho de conclusão de curso.

# Ferramentas utilizadas
Python 3.8.5

[Chromedriver](https://chromedriver.chromium.org/downloads) 

### Bibliotecas
>beautifulsoup4==4.9.3 
>
>fake-useragent==0.1.11
>
>selenium==3.141.0

### Documentação

[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

[CSV](https://docs.python.org/3/library/csv.html)

[Fake User Agent](https://pypi.org/project/fake-useragent/)

[Selenium](https://selenium-python.readthedocs.io/)

[Time](https://docs.python.org/3/library/time.html)

## Erros mais comuns

- A documentação recomenda utilizar uma espera implicita com o código: driver.implicitly_wait contudo no teste essa espera implícita extraia sempre os dados da primeira página. Ao explicitar um tempo de espera com a função Sleep() o código funcionou normalmente. 

- O chromedriver utiliza a versão do chrome instalada no seu computador. Caso utilize por um período contínuo convém [desabilitar a atualização automática do Chrome.](https://support.google.com/chrome/a/answer/6350036?hl=pt-BR#zippy=%2Cdesativar-as-atualiza%C3%A7%C3%B5es-do-navegador-chrome) 

- Fake User Agent list index out of range. Conforme o [Pull Request#110](https://github.com/hellysmile/fake-useragent/pull/110). Caso apareça a mensagem de erro você poderá alterar no fake_useragent/utils.py source code localizado na pasta onde o python foi instalado. Na linha 99 é feita a alteração para:

~~~ 
html = html.split('<table class="ws-table-all notranslate">')[1] 
~~~

Para encontrar o diretório é só executar o código:
~~~
import fake_useragent
print(fake_useragent.__file__)
~~~

## Utilização

É preciso alterar o url para extrair imóveis de outras regiões. No código do repositório o url está editado para extrair imóveis do site viva real na cidade de São Paulo no estado de São Paulo. 

O campo **ADDRESS** é extraido do url da busca desejada a formatação padrão contém a região, o nome do bairro e/ou rua desejada. Por exemplo:

> zona-sul/vila-nova-conceicao/avenida-presidente-juscelino-kubitschek

O campo **TIPO** é extraído do url da busca desejada

O campo **NOME** é utilizado para salvar o csv identificando a pesquisa realizada

Será salvo um arquivo csv com o nome fornecido + data em que foi realizada a extração (horário UTC) e na formatação %d%b%Y (exemplo: 01Jan2022). No arquivo serão salvas as informações do preço do imóvel, área do imóvel, endereço informado do imóvel, ID do anúncio, data da extração e região que utilizará o campo fornecido **NOME**.



