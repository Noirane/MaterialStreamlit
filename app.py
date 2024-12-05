import streamlit as st 
import folium 
import json 
import pandas as pd 
from graficos import grafico 

#Cabeçalho 
st.markdown("# Trabalho")

#Mapa
with open('paises.json') as f:
    paisesJson = json.load(f)
    m = folium.Map(location=[20,0], zoom_start=2)
    folium.GeoJson(paisesJson,
        style_function=lambda x: {'fillColor': 'green', 'fillOpacity': 1}
        if x['properties']['name'] == 'Brazil' else {}).add_to(m)
    st.components.v1.html(m._repr_html_(), height=450)

#Tabela 
st.markdown ("## Dados")
df = pd.read_csv('dataset.csv')
st.write(df)

#graficos 
grafico (df, "20_a_24")
grafico (df, "60_+")
