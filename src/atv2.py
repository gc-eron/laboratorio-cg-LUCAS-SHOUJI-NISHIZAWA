import numpy as np
import streamlit as st
def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)
st.title("Imagem como matriz")

bandeira = np.zeros((12, 18, 3), dtype=np.uint8)
bandeira[:] = (30, 160, 150) # fundo
bandeira[:, :6] = (110, 50, 150) # faixa à esquerda
bandeira[4:8, 6:12] = (240, 190, 40) # retângulo no meio
st.image(ampliar(bandeira))


bandeira[:, :6] = (255, 0, 0)
bandeira[:, 6:12] = (255, 255, 255)
bandeira[:, 12:] = (0, 0, 255)
st.image(ampliar(bandeira))
