import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import argparse
import numpy as np
from datetime import datetime, timedelta
sns.set_style(style='darkgrid')

def get_climate_data(lat, lon):
    url = 'https://api.open-meteo.com/v1/forecast'
    params = {
        'latitude': lat,
        'longitude': lon,
        'hourly': 'temperature_2m',
        'timezone':'auto'
    }
    
    try:
        print("Buscando dados climáticos...")
        res = requests.get(url, params=params, timeout=10)
        res.raise_for_status()
        return res.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados climáticos: {e}")
        sys.exit(1)
    except requests.exceptions.Timeout:
        print("Tempo de conexão esgotado. Tente novamente mais tarde.")
        sys.exit(1)

def process_climate_data(data, export_csv=True):
    print('Processando dados com o Pandas...')
    if 'hourly' not in data or 'time' not in data['hourly']:
        print("Erro!. Estrutura de dados inesperada da API.")
        sys.exit(1)
    
    df= pd.DataFrame({
        'data_hora': pd.to_datetime(data['hourly']['time']),
        'temperatura_C': data['hourly']['temperature_2m']
    })
    if export_csv:
        df.to_csv('dados_climaticos.csv', index=False)
        print("Dados climáticos processados e salvos em 'dados_climaticos.csv'")
    return df

def plot_climate_data(df):
    print('Gerando gráfico com o Seaborn...')
    df_short = df.head(48)
    
    plt.figure(figsize=(12, 6))
    grafico = sns.lineplot(
        data=df_short,
        x='data_hora',
        y='temperatura_C',
        marker='o',
        color='coral'
    )
    grafico.set_title('Previsão de Temperatura - 48 Horas', fontsize=16)
    grafico.set_xlabel('Data e Hora', fontsize=12)
    grafico.set_ylabel('Temperatura (°C)', fontsize=12)
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    name_file = 'previsao_temperatura.png'
    plt.savefig(name_file)
    print(f"Gráfico salvo como '{name_file}'")

def max_min_temperature(df, export_csv=True):
    print("\nAnalisando máximas e minimas")
    df_analise = df.copy() 
    df_analise['data_hora'] = pd.to_datetime(df_analise['data_hora'])
    df_analise['Data'] = df_analise['data_hora'].dt.date
    df_day = df_analise.groupby('Data').agg(
        TEMP_MIN = ("temperatura_C", "min"),
        TEMP_MAX = ("temperatura_C", "max")
    ).reset_index()
    df_day["Amplitude_Térmica"] = (df_day['TEMP_MAX'] - df_day['TEMP_MIN']).round(2)
    print(df_day.to_string(index=False))     
    
    if export_csv:
        carimbo_tempo = datetime.now().strftime("%Y%m%d_%H%M")
        nome_arquivo = f"analise_extremos_{carimbo_tempo}.csv"
        
        df_day.to_csv(nome_arquivo, index=False)
        print(f"Relatório de extremos salvo de forma segura em: {nome_arquivo}\n")
    return df_day
    
def main():

    parser = argparse.ArgumentParser(
        description="Análise climática usando Open-Meteo API, Pandas e Seaborn"
    )
    parser.add_argument(
        '--lat',
        type=float,
        default=-22.25,
        help='Latitude do local (padrão: -22.25 para Santa Rita do Sapucaí, MG)'
    )
    parser.add_argument(
        '--lon',
        type=float,
        default=-45.70,
        help='Longitude do local (padrão: -45.70 para Santa Rita do Sapucaí, MG)'
    )
    
    args = parser.parse_args()
    print(f"Iniciando análise climática para latitude {args.lat} e longitude {args.lon}...")    
    data_json = get_climate_data(args.lat, args.lon)
    df_clima = process_climate_data(data_json, export_csv=True)
    df_extreme = max_min_temperature(df_clima,export_csv=True)
    print('\n Resumo dos dados climáticos:')
    print(df_clima.describe())
    print('-' * 40)
    print(df_extreme)
    print('-' * 40)
    plot_climate_data(df_clima)
    print("\nAnálise climática concluída com sucesso.")
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExecução interrompida pelo usuário.")
        sys.exit(0)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        sys.exit(1)
    