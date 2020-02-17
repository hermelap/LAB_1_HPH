# -- ------------------------------------------------------------------------------------ -- #
# -- Proyecto: Repaso de python 3 y analisis de precios OHLC                              -- #
# -- Codigo: principal.py - script principal de proyecto                                  -- #
# -- Rep: https://github.com/hermelap/LAB_0_HPH
# -- #
# -- Autor: Hermela Peña                                                              -- #
# -- ------------------------------------------------------------------------------------ -- #

# -- ------------------------------------------------------------- Importar con funciones -- #

import funciones as fn  # Para procesamiento de datos
import pandas as pd  # Procesamiento de datos
from datos import token as OA_Ak  # Importar token para API de OANDA

# -- --------------------------------------------------------- Descargar precios de OANDA -- #

# token de OANDA
OA_In = "USD_MXN"  # Instrumento
OA_Gn = "D"  # Granularidad de velas
fini = pd.to_datetime("2019-07-06 00:00:00").tz_localize('GMT')  # Fecha inicial
ffin = pd.to_datetime("2019-12-06 00:00:00").tz_localize('GMT')  # Fecha final

# Descargar precios masivos
df_pe = fn.f_precios_masivos(p0_fini=fini, p1_ffin=ffin, p2_gran=OA_Gn,
                             p3_inst=OA_In, p4_oatk=OA_Ak, p5_ginc=4900)

# Movimiento

MA_Fast = 50 # Promedio movil de menor rezago
MA_Slow = 100 # Promedio movil de mayor rezago

fn.decision(df_pe, MA_Fast, MA_Slow)
