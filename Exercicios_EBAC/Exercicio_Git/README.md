# Exercício Git

Este projeto é um exemplo de web scraping em Python para coletar informações de filmes de um site de cinema e salvar os dados em um arquivo CSV.

## O que o projeto faz

- Acessa uma página de filmes no site AdoroCinema.
- Extrai os seguintes dados:
  - título
  - data de lançamento
  - duração
  - gênero
- Gera um arquivo CSV com os resultados para análise posterior.

## Estrutura do projeto

- main.py: script principal responsável pela coleta e exportação dos dados.
- requirements.txt: dependências do projeto.
- data/: diretório para armazenar arquivos de dados.

## Requisitos

- Python 3.9 ou superior
- pip

## Instalação

1. Acesse a pasta do projeto.
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Como executar

Execute o script principal:

```bash
python main.py
```

Ao final, será criado um arquivo CSV com os filmes coletados. O nome padrão do arquivo é `movies_2026.csv`, mas isso pode ser alterado por meio da variável de ambiente `DATA_PATH`.

## Variáveis de ambiente

O projeto aceita as seguintes variáveis opcionais:

- `USER_AGENT`: define o cabeçalho de usuário usado nas requisições.
- `REQUESTS_DELAY`: tempo de espera entre requisições.
- `TIMEOUT`: tempo máximo de espera por resposta.
- `DATA_PATH`: caminho do arquivo CSV gerado.

## Observação

Este projeto é didático e serve como exemplo de uso de bibliotecas como `requests`, `BeautifulSoup`, `pandas` e `python-dotenv` para automação e coleta de dados na web.

