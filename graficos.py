import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def grafico(dados, idade_desejada):
    regioes = ['Norte', 'Nordeste', 'Sudeste', 'Sul', 'Centro-Oeste']
    values = dados.loc[dados['Idade']==idade_desejada, regioes].values[0] 

    fig, ax = plt.subplots()
    ax.pie(values, labels=regioes, autopct='%1.1f%%')
    ax.set_title(f'Pessoas com celular em 2005, Idade{idade_desejada}')

    st.pyplot(fig)