**Entrez_API**

Este repositório contém um script python que descarrega sequências de uma base de dados
Este é um trabalho proposto na Unidade Curricular de Análise de Sequências Biológicas do curso de Bioinformática.

**Utilização**

Linguagem:
  -Python3
Pacotes:
  -argparse
  -requests
  -json

**Instalação**

sudo apt install python3-pip

**Toturial**

python3 script.py database term

**Database**

Nome da base de dados nucleotideo->"nucleotide", proteina->"protein", genoma->"genome e gene->"gene"

**Term**

O que queremos pesquisar na base de dados. Caso seja coposto por mais de um elemento tem de se escrever entre aspas.

**Exemplo**

python3 homework1_asb.py nucleotide "Psammodromus algirus[organism], cytb[gene]"

**Bibliografia**

https://requests.readthedocs.io/en/latest/user/quickstart/

https://docs.python.org/3/library/json.html
