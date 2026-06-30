import os
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import re

#Carregando variáveis de ambiente
load_dotenv()

def get_headers():
    return {
        "User-Agent": os.getenv("USER_AGENT", "Mozilla/5.0"),
        "Accept-Language": "pt-BR, pt;q=0.9, en-US; q=0, en; q=0.7"
    }

def scrap_movies(url):
    headers = get_headers()
    delay = int(os.getenv("REQUESTS_DELAY", 2))
    
    try:
        print(f"Acessando : {url}")
        res = requests.get(url, headers, timeout=int(os.getenv("TIMEOUT", 10)))
        res.raise_for_status()
        time.sleep(delay)
        soup = BeautifulSoup(res.text, "html.parser")
        movies = soup.find_all("div", class_="card entity-card entity-card-list cf")
        data = []
        for movie in movies:
            title_tag = movie.find("h2", class_="meta-title")
            title = title_tag.text.strip() if title_tag else "Título não encontrado!"
            meta_body = movie.find("div", class_="meta-body-item meta-body-info")
            data_lancamento = "N/A"
            duracao = "N/A"
            generos = "N/A"
            if meta_body:
                # pega lançamentos
                data_tag = meta_body.find("span", class_="date")
                if data_tag:
                    data_lancamento = data_tag.text.strip()

                # pega todos os textos diretos dentro do bloco
                textos = list(meta_body.stripped_strings)

                # remove data
                textos = [t for t in textos if t != data_lancamento and t != "|"]

                # agora normalmente fica:
                # ["2h 12min", "Aventura", "Ação", "Fantasia"]

                if textos:
                    duracao = textos[0]

                    if len(textos) > 1:
                        generos = ",".join(textos[1:])
                        data.append({
                            "titulo": title,
                            "lancamento": data_lancamento,
                            "duracao": duracao,
                            "genero": generos,
                        })
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"Erro http: {http_err}")
    except Exception as e:
        print(f"Erro: {e}")
    return []

def main():
    target = "https://www.adorocinema.com/filmes/numero-cinemas/"
    filmes = scrap_movies(target)
    
    if filmes:
        df = pd.DataFrame(filmes)
        file = os.getenv("DATA_PATH", "movies_2026.csv")
        df.to_csv(file, index=False, encoding="utf-8-sig")
        print(f"Arquivo {file} criado com sucesso!")
    else:
        print("Falha ao coletar dados")

if __name__ == "__main__":
    main()