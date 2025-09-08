import rasterio

# Caminhos das bandas originais (ajuste o caminho se necessário)
banda_red = "./LC08_L1TP_094076_20250907_20250907_02_RT_B4.TIF"  # Banda Vermelha
banda_nir = "./LC08_L1TP_094076_20250907_20250907_02_RT_B5.TIF"  # Banda Infravermelho

# Abrir as bandas
with rasterio.open(banda_red) as src_red, rasterio.open(banda_nir) as src_nir:
    profile = src_red.profile
    profile.update(count=2)  # agora terá 2 bandas no mesmo arquivo

    # Criar o novo arquivo "sentinel.tif"
    with rasterio.open("./sentinel.tif", "w", **profile) as dst:
        dst.write(src_red.read(1), 1)  # escreve a banda vermelha na posição 1
        dst.write(src_nir.read(1), 2)  # escreve a banda NIR na posição 2

print("✅ Arquivo 'sentinel.tif' criado com sucesso em /data/")
