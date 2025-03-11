import argparse
import requests
import json

def Escolha_Utilizador():
    """
    Analisa os argumentos da linha de comando para obter a base de dados e o termo de pesquisa.
    Garante que os argumentos necessarios sejam fornecidos.
    """
    analizar = argparse.ArgumentParser(description="Obter sequencias a partir das bases de dados do NCBI.")
    analizar.add_argument("database", help="Base de dados a pesquisar (ex.: nucleotide, genome, protein, gene).")
    analizar.add_argument("term", help="Termo de pesquisa (ex.: 'Psammodromus algirus[organism], cytb[gene]').")
    argumentos = analizar.parse_args()
    return argumentos.database, argumentos.term

def procurar(database, term):
    """
    Pesquisa na base de dados do NCBI utilizando a API do Entrez e obtem WebEnv e QueryKey.
    """
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": database,
        "term": term,
        "usehistory": "y",
        "retmode": "json"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data["esearchresult"]["webenv"], data["esearchresult"]["querykey"]

def obter(database, webenv, querykey):
    """
    Obtem dados de sequencia da base de dados do NCBI e imprime-os no formato FASTA.
    """
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": database,
        "query_key": querykey,
        "WebEnv": webenv,
        "rettype": "fasta",
        "retmode": "text"
    }
    response = requests.get(url, params=params)
    print(response.text)

def main():
    """
    Funcao principal para coordenar a analise de argumentos, pesquisa e obtencao de dados.
    """
    database, term = Escolha_Utilizador()
    webenv, querykey = procurar(database, term)
    obter(database, webenv, querykey)

if __name__ == "__main__":
    main()
