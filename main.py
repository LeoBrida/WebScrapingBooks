import requests
from bs4 import BeautifulSoup

link = "https://www.livrariascuritiba.com.br/livros?PS=24&lid=b5cba55c-e771-4ab0-9d34-31a060dc42e3"
#header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

requisicao = requests.get(link) #, headers = header

site = BeautifulSoup(requisicao.text, "html.parser")

linksLivros = []
livros = site.find_all("a", class_="productImage",limit = 2)
for livro in livros:
    link = livro['href']
    linksLivros.append(link)

links = list(set(linksLivros))
print(links)

for link in links:
    requisicaoLivro = requests.get(link)
    siteLivro = BeautifulSoup(requisicaoLivro.text, "html.parser")
    url = link
    #titulo
    #edição
    #isbn
    #Número de Páginas
    #editora
    #Ano da Edição
    #autor
    #Formato
    #tags (posso usar a categoria do livro como tag)
    #nota
        #nota final
        #qtd votos
    



'''
req1 --> link1
link1 --> conteudoLink1
conteudoLink1 --> quaisLivros
quaisLivros --> linkDeConteudoLivro

req2 --> linkDeConteudoLivro
linkDeConteudoLivro --> ConteudoLivro
ConteudoLivro --> JSON

'''
