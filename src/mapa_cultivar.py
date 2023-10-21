from geobr import read_municipality
import pandas as pd
import geopandas as gpd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from unidecode import unidecode
from matplotlib_scalebar.scalebar import ScaleBar
from matplotlib.colors import ListedColormap
import contextily as cx

url = 'https://github.com/gldmelo/vcu-trigo-python/raw/main/data/vcu-trigo.json'
df_dados_vcu = pd.read_json(url)

# Remove os acentos e deixa os nomes em maiúsculas
def normalizar(nome):
    txt = unidecode(str(nome)).upper()
    return txt

# Obtém o VCU para a cidade e uf indicados
def popular_vcu_cidade(uf, cidade):
  vcu_uf = df_dados_vcu[(df_dados_vcu['Uf'] == uf) & (df_dados_vcu['cidade_normalizada'] == normalizar(cidade))]
  if vcu_uf.empty:
    return 'Não Indicada'
  return vcu_uf.iloc[0]['Vcu']

# Cria uma coluna no DataFrame com o nome da cidade normalizado
df_dados_vcu['cidade_normalizada'] = None
df_dados_vcu['cidade_normalizada'] = df_dados_vcu['Cidade'].apply(normalizar)

# Busca os dados de Cidades usando a geobr
df_cidades_brasil = read_municipality(year=2020)

# Descarta os estados fora da região sul
df_cidades_brasil = df_cidades_brasil[df_cidades_brasil['abbrev_state'].isin(['RS', 'SC', 'PR'])]

# Popula o DataFrame com o VCU de cada cidade
df_cidades_brasil['VCU Trigo'] = None
df_cidades_brasil['VCU Trigo'] = df_cidades_brasil.apply(lambda row: popular_vcu_cidade(row['abbrev_state'], row['name_muni']), axis=1)

# Indica a projeção do mapa
df_cidades_brasil.crs = 'EPSG:4326'

# Montamos um mapa de cores para cada VCU e a região não indicada para plantio
colors = {
    "Não Indicada": "tab:red",
    "VCU I": "tab:blue",
    "VCU II": "tab:green",
    "VCU III": "yellow"    
}
cmap = ListedColormap(list(colors.values()))

# E por fim, geramos a imagem do mapa com os dados
fig,ax = plt.subplots(figsize=(10,10))
df_cidades_brasil.plot(ax=ax, column='VCU Trigo', categorical=True, legend=True, cmap=cmap, edgecolor="#000", linewidth=0.2)
cx.add_basemap(ax, crs=df_cidades_brasil.crs)
ax.tick_params(axis="y", labelrotation=90)
ax.add_artist(ScaleBar(dx=1, units="km", dimension="si-length", length_fraction=0.25, location='lower right'))
ax.set_title("Regiões de Adaptação do Trigo (RS, SC, PR)", fontsize=17)
plt.savefig('vcu-trigo.png',dpi=300, bbox_inches='tight',pad_inches = 0.1)
plt.clf()
plt.close()
