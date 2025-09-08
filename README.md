# 🌿 Processamento Geoespacial: NDVI com Dados Landsat-8

Este projeto foi desenvolvido para processar dados de satélite Landsat-8 de maneira automatizada, com foco no cálculo do Índice de Diferença de Vegetação Normalizada (NDVI). Ele utiliza as bandas vermelha (B4) e infravermelho próximo (B5) para analisar e mapear a saúde da vegetação em uma área de interesse.

## 📋 Funcionalidades

- **União de Bandas**: Junta as bandas B4 e B5 do Landsat-8 em um único arquivo `sentinel.tif`
- **Cálculo de NDVI**: Aplica a fórmula do NDVI para gerar um mapa de índice de vegetação
- **Geração de Saídas**: Salva o resultado do NDVI em um novo arquivo GeoTIFF
- **Análise Vetorial**: Cria um shapefile (.shp) que destaca as áreas com alta densidade de vegetação (NDVI > 0.5)
- **Visualização**: Apresenta os resultados graficamente para uma análise visual

## 🛠️ Requisitos

Para rodar este projeto, você precisará das seguintes bibliotecas Python:

- `rasterio` - Para manipulação de dados raster
- `numpy` - Para operações matemáticas
- `matplotlib` - Para visualização
- `geopandas` - Para manipulação de dados vetoriais
- `fiona` - Para leitura/escrita de formatos vetoriais
- `shapely` - Para geometrias

### Instalação

Você pode instalá-las usando pip:

```bash
pip install rasterio numpy matplotlib geopandas fiona shapely
```

Ou usando o ambiente virtual do projeto:

```bash
# Ativar o ambiente virtual
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```

## 🚀 Como Usar

### 1. Preparação dos Dados
Certifique-se de que os arquivos .TIF das bandas 4 e 5 do Landsat-8 estejam no diretório `data/`:
- `LC08_L1TP_094076_20250907_20250907_02_RT_B4.TIF` (Banda Vermelha)
- `LC08_L1TP_094076_20250907_20250907_02_RT_B5.TIF` (Banda Infravermelho Próximo)

### 2. Unir as Bandas
Execute o script `criar_sentinel.py` para criar o arquivo `sentinel.tif`:

```bash
cd data
python criar_sentinel.py
```

### 3. Processar os Dados
Execute o notebook Jupyter `processamento_ndvi.ipynb` para:
- Calcular o NDVI
- Gerar o arquivo GeoTIFF
- Criar o shapefile com áreas de alta vegetação
- Visualizar os resultados

```bash
jupyter notebook notebook/processamento_ndvi.ipynb
```

## 📁 Estrutura do Projeto

```
Projetos_p/
├── README.md
├── data/
│   ├── criar_sentinel.py          # Script para unir bandas
│   ├── LC08_L1TP_094076_20250907_20250907_02_RT_B4.TIF  # Banda Vermelha
│   ├── LC08_L1TP_094076_20250907_20250907_02_RT_B5.TIF  # Banda NIR
│   ├── sentinel.tif               # Arquivo com bandas unidas
│   ├── ndvi.tif                   # Mapa de NDVI calculado
│   ├── areas_ndvi_alto.shp        # Shapefile com áreas de alta vegetação
│   ├── areas_ndvi_alto.dbf        # Arquivo de atributos
│   ├── areas_ndvi_alto.prj        # Arquivo de projeção
│   └── areas_ndvi_alto.shx        # Arquivo de índice
├── notebook/
│   └── processamento_ndvi.ipynb   # Notebook principal
├── images/                        # Diretório para imagens geradas
└── venv/                          # Ambiente virtual Python
```

## 📊 Arquivos Gerados

Após a execução completa, os seguintes arquivos serão gerados:

- **`sentinel.tif`** - Arquivo raster com as bandas B4 e B5 unidas
- **`ndvi.tif`** - Mapa de NDVI calculado (valores de -1 a 1)
- **`areas_ndvi_alto.shp`** - Shapefile com áreas de alta densidade de vegetação (NDVI > 0.5)
- **Arquivos auxiliares** (.dbf, .prj, .shx) - Necessários para o funcionamento do shapefile

## 🗺️ Análise GIS

Os arquivos gerados podem ser importados para softwares de GIS como:
- **QGIS** (gratuito)
- **ArcGIS** (comercial)
- **Google Earth Engine** (online)

### Importando no QGIS:
1. Abra o QGIS
2. Adicione camada raster: `data/ndvi.tif`
3. Adicione camada vetorial: `data/areas_ndvi_alto.shp`
4. Configure a simbologia conforme necessário

## 📊 Interpretação do NDVI

Os valores de NDVI variam de -1 a 1:

| Valor NDVI | Interpretação | Cor Sugerida |
|------------|---------------|--------------|
| **-1 a 0** | Água, solo nu, áreas urbanas | Azul/Cinza |
| **0 a 0.3** | Vegetação esparsa, pastagens | Amarelo |
| **0.3 a 0.7** | Vegetação moderada, cultivos | Verde claro |
| **0.7 a 1** | Vegetação densa, florestas | Verde escuro |

## 🔧 Detalhes Técnicos

### Especificações dos Dados:
- **Satélite**: Landsat-8
- **Sensor**: OLI (Operational Land Imager)
- **Resolução Espacial**: 30 metros
- **Data**: 07/09/2025
- **Cena**: LC08_L1TP_094076_20250907_20250907_02_RT
- **Dimensões**: 7661 x 7761 pixels

### Fórmula do NDVI:
```
NDVI = (NIR - RED) / (NIR + RED)
```

Onde:
- **NIR**: Banda 5 (Infravermelho Próximo)
- **RED**: Banda 4 (Vermelho)

## 📝 Notas Importantes

- ⚠️ **Dados de Teste**: Este projeto usa dados Landsat-8 de 2025 (futuro) para fins demonstrativos
- 🔄 **Processamento**: O processamento pode demorar dependendo do tamanho dos dados
- 💾 **Espaço em Disco**: Certifique-se de ter espaço suficiente para os arquivos gerados
- 🌐 **Sistema de Coordenadas**: Os dados mantêm o sistema de coordenadas original do Landsat-8

## 🚨 Solução de Problemas

### Erro ao abrir arquivos:
- Verifique se os arquivos .TIF estão no diretório correto
- Confirme se as bibliotecas estão instaladas corretamente

### Erro de memória:
- Para dados muito grandes, considere usar chunks ou reduzir a resolução

### Problemas de visualização:
- Certifique-se de que o matplotlib está configurado corretamente
- Para ambientes sem display, use backend 'Agg'

## 🤝 Contribuição

Este é um projeto educacional demonstrando técnicas de processamento de dados geoespaciais. Sinta-se à vontade para:
- Reportar problemas
- Sugerir melhorias
- Adicionar novas funcionalidades
- Compartilhar casos de uso

## 📚 Referências

- [Landsat-8 Data Users Handbook](https://www.usgs.gov/landsat-missions/landsat-8-data-users-handbook)
- [NDVI - Wikipedia](https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index)
- [Rasterio Documentation](https://rasterio.readthedocs.io/)
- [GeoPandas Documentation](https://geopandas.org/)

## 📄 Licença

Este projeto é destinado a fins educacionais e de demonstração. Os dados do Landsat-8 são de domínio público.
