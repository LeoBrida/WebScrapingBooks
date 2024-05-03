#coding: utf-8
import requests
import time
import json
from bs4 import BeautifulSoup


link = "https://www.livrariascuritiba.com.br/livros?PS=24&lid=b5cba55c-e771-4ab0-9d34-31a060dc42e3"

requisicao = requests.get(link)

site = BeautifulSoup(requisicao.text, "html.parser")

linksLivros = []
livros = site.find_all("a", class_="productImage",limit = 2)
for livro in livros:
    link = livro['href']
    linksLivros.append(link)

links = list(set(linksLivros))

dictsList = []

for link in links:
    requisicaoLivro = requests.get(link)
    siteLivro = BeautifulSoup(requisicaoLivro.text, "html.parser")

    # URL
    url = link

    # Título
    tituloBruto = siteLivro.find("div", class_="title-product")
    tagTitulo = tituloBruto.div.extract()
    titulo = tagTitulo.string.extract()

    # Edição
    edicaoBruta = siteLivro.find("td", class_="value-field Edicao")
    if edicaoBruta == None:
        edicao = None
    else:
        edicao = edicaoBruta.string.extract()
    
    # ISBN
    isbnBruto = siteLivro.find("td", class_="value-field ISBN")
    if isbnBruto == None:
        isbn = None
    else:
        isbn = isbnBruto.string.extract()
  
    # Número de Páginas
    numPaginasBruto = siteLivro.find("td", class_="value-field Numero-de-Paginas")
    if numPaginasBruto == None:
        numPaginas = None
    else:
        numPaginas = numPaginasBruto.string.extract()

    # Editora
    editoraBruto = siteLivro.find("td", class_="value-field Editora")
    if editoraBruto == None:
        editora = None
    else:
        editora = editoraBruto.string.extract()

    # Ano da Edição
    anoEdicaoBruto = siteLivro.find("td", class_="value-field Ano-da-Edicao")
    if anoEdicaoBruto == None:
        anoEdicao = "Não informado"
    else:
        anoEdicao = anoEdicaoBruto.string.extract()

    # Autor
    autorBruto = siteLivro.find("td", class_="value-field Autor")
    if autorBruto == None:
        autor = None
    else:
        autor = autorBruto.string.extract()

    # Formato
    formatoBruto = siteLivro.find("td", class_="value-field Formato")
    if formatoBruto == None:
        formato = None
    else:
        formato = formatoBruto.string.extract()

    # Tags (posso usar a categoria do livro como tag)
    tagBruto = siteLivro.find("li", class_ = "last")
    tag = ((tagBruto.a.extract()).span.extract()).string.extract()

    # Preço
    precoBruto = siteLivro.find("strong", class_="skuBestPrice")
    preco = precoBruto.string.extract()
   
    # Nota
    # Nota final
    notaBruto = siteLivro.find("meta", itemprop = "ratingValue")
    if notaBruto == None:
        nota =  None
    else:
        nota = notaBruto['content']
   

    # Qtd votos
    qtdVotosBruto = siteLivro.find("strong", itemprop="ratingCount")
    if qtdVotosBruto == None:
        qtdVotos = None
    else:
        qtdVotos = qtdVotosBruto.string.extract()
    
    dados = dict(url = url, titulo = titulo, edicao = edicao, serie = None, isbn = isbn, numPaginas = numPaginas, editora = editora, ano = anoEdicao, autores = autor, tags = tag, precos = preco, nota = {'notaFinal': nota, 'qtdVotos': qtdVotos})

    dictsList.append(dados)

    time.sleep(3)

with open("data.json", "w") as f:
    json.dump(dictsList, f, indent=2)

    
