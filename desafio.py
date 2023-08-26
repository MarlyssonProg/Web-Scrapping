# Importa a biblioteca HTMLSession da biblioteca requests_html
from requests_html import HTMLSession

# Cria uma sessão HTTP usando a classe HTMLSession
sessao = HTMLSession()

# Define a URL da página que será utilizada
url = 'https://www.olx.com.br/eletronicos-e-celulares/estado-sp?q=iphone'

# Faz uma requisição GET à página da web usando a sessão criada
resposta = sessao.get(url)
print('resposta:', resposta)

# Cria uma lista vazia que irá armazenar as informações dos anúncios
anuncios = []

# Usa o método find do objeto html retornado na resposta para encontrar todos os links dos anúncios
links = resposta.html.find("a[data-ds-component='DS-NewAdCard-Link']")
print('links:', links)

# Itera sobre todos os links encontrados na página
for link in links:

    # Extrai o URL de cada anúncio do atributo 'href' do elemento
    url_iphone = link.attrs['href']

    # Faz uma requisição GET ao URL de cada anúncio usando a sessão criada
    resposta_iphone = sessao.get(url_iphone)

    # Extrai o título e o preço de cada anúncio
    titulo = resposta_iphone.html.find('h1', first=True).text
    preco = resposta_iphone.html.find(
        'span[class="ad__sc-1wimjbb-1 hoHpcC sc-bZQynM hYqmow"]', first=True).text

    # Adiciona as informações do anúncio em um dicionário de anúncios
    anuncios.append({
        'url': url_iphone, 'titulo': titulo, 'preco': preco
    })
