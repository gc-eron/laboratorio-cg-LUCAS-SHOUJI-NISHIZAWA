import numpy as np
import streamlit as st
from PIL import Image

st.title("Atv 4: RGB")

# 1. Leitura da foto
st.header("1. Leitura da foto")
col1, col2 = st.columns(2)
foto = Image.open("imagens/foto.jpg")
img = np.array(foto)
col1.image(img)
col2.text(img.shape)
# faça você: o pixel img[100, 100] na col2
col2.text(img[100, 100])

# 2. Canais
st.header("2. Canais")
col1, col2 = st.columns(2)
col1.image(img[:, :, 0], caption="R")

# faça você: G e B na col1
col1.image(img[:, :, 1], caption="G")
col1.image(img[:, :, 2], caption="B")

so_r = img.copy()
so_r[:, :, 1] = 0
so_r[:, :, 2] = 0
col2.image(so_r, caption="só R")

# 3. Cubo e BGR
st.header("3. Cubo e BGR")
col1, col2 = st.columns(2)
quadrado = np.zeros((80, 80, 3), dtype=np.uint8)
quadrado[:, :] = (255, 255, 0)
col1.image(quadrado, caption="amarelo")

# faça você: mais três vértices do cubo na col1
quadrado[:, :] = (255, 0, 0)
col1.image(quadrado, caption="vermelho")

quadrado[:, :] = (0, 255, 0)
col1.image(quadrado, caption="verde")

quadrado[:, :] = (0, 0, 255)
col1.image(quadrado, caption="azul")

# faça você: a foto com channels="BGR" na col2
col2.image(img, channels="BGR", caption="BGR")

# 4. Tons de cinza
st.header("4. Tons de cinza")
col1, col2 = st.columns(2)
r = img[:, :, 0].astype(float)
g = img[:, :, 1].astype(float)
b = img[:, :, 2].astype(float)
soma = r + g + b
media = (soma / 3).astype(np.uint8)
col1.image(media, caption="média")

# faça você: a ponderada na col2
m = (0.299 * r + 0.587 * g + 0.114 * b).astype(np.uint8)
col2.image(m, caption="ponderada")
