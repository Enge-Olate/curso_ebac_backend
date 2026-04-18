
# Análise de Dados Climáticos com Python

Projeto para um exercício do curso Full Stack Python da EBAC.


## API Reference

#### Pegue os dados nessa URL

```http
  GET https://api.open-meteo.com/v1/forecast
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. NULL |



Pegue dados climáticos, nessa API.



## Características

- CLI
- Informe [--lat=float] && [--lon=float]


## Caso de uso

Por padrão o código vai com latitude e longitude de Santa Rita do Sapucaí MG.

```CLI
    python3 analise_clima.py --lat=𝙌 --lon=𝙌
```
    **𝙌**: Números racionais sepados por ponto.


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![python](https://img.shields.io/badge/Python-3.13.5-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![pip](https://img.shields.io/badge/Pip-3.13.5-3776AB.svg?style=flat&logo=pip&logoColor=white)](https://pip.pypa.io/en/stable/)
[![pandas](https://img.shields.io/badge/Pandas-3776AB.svg?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![seaborn](https://img.shields.io/badge/Seaborn-3776AB.svg?style=flat&logo=seaborn&logoColor=white)](https://pypi.org/project/seaborn/)

