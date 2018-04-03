# -*- coding: utf-8 -*-
import csv
from requests_html import HTMLSession
import wget
import os
from tqdm import tqdm
import requests


def download_file(url, file_name):
    response = requests.get(url, stream=True)
    with open(file_name, "wb") as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)
    handle.close()


def download_pdfs():
    with open('urls.csv', 'r') as f:
        reader = csv.reader(f)
        urls_list = list(reader)

    list_cleaned = []
    for url in urls_list:
        if url[0] not in list_cleaned:
            list_cleaned.append(url[0])
    
    for url in list_cleaned:
        name_file = url.split('=')[-1]
        print(name_file)
        path_file = os.path.join('downloads', name_file)

        if not os.path.exists(path_file):
            download_file(url, path_file)


def get_link_planilhas(pagina):
    url = 'http://www.ceasa.rj.gov.br/ceasa_portal/view/ListarCotacoes.asp'
    params = {
        'pagina': pagina
    }
    session = HTMLSession()
    response= session.get(url, params=params)
    links = response.html.absolute_links    

    for link in links:
        if 'Boletim diario de precos' in link and link.endswith('.pdf'):
            # faz o append no csv da base
            with open('urls.csv', 'a', newline='') as baseFile:
                fieldnames = ['url']
                writer = csv.DictWriter(baseFile, fieldnames=fieldnames, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
                row_inserted = { 'url': link }
                writer.writerow(row_inserted)
                print(row_inserted)
    return True


def main():
    paginas = list(range(1, 70, 1))
    print(paginas)
    # ultuma pagina = 69
    for pagina in paginas:
        get_link_planilhas(pagina)
    # faz o download de todos os PFDs de cotação disponíveis
    download_pdfs()

if __name__ == '__main__':
    main()
    