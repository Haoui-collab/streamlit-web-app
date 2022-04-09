import streamlit as st
import plotly_express as px 
from PIL import Image
import pandas as pd 
import plotly.graph_objs as go
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib.backends.backend_agg import RendererAgg
from sklearn.preprocessing import LabelEncoder, OneHotEncoder # used for encoding categorical data


st.title(":bar_chart: VISUALISATION DU DATA")
excel_file ='COMFO_sn.xlsx'
df =pd.read_excel(excel_file)

if st.checkbox('Afficher les donnés'):
    #st.subheader('Voici les données de notre fichier')
    st.dataframe(df)
    st.title(":bar_chart: Statistique des commentaires")
    st.markdown("##")
    total_sales = int(df["polarity_total"].sum())
    col1, col2,col3,col4 = st.columns(4)
    col1.metric("Commentaire",f" {total_sales:,}")
    col2.metric("Positive", "51,278")
    col3.metric("Negative", "31,552")
    col4.metric("Neutre", "23,538")
    st.title(":bar_chart: L'analyse des commentaires par rapport au polarité")
    fig = px.histogram(df, x="Experts")
    st.write(fig)
    #st.bar_chart(df['Experts'])
    st.title(":bar_chart: Statistique des Polarités")
    pie_chart = px.pie(df,
    values='polarity_total',
    names='Polarity')
    st.plotly_chart(pie_chart)
    st.subheader("L'emotion du commentaire")

with st.form(key='emotion_clf_form'):
	raw_text = st.text_area("Ecrivez votre phrase ici pour l'analyser")
	submit_text = st.form_submit_button(label='Submit')
if submit_text:
			col1,col2  = st.columns(2)

with col1:
				st.success("Texte Original")
				st.write(raw_text)

				st.success("Prediction")

with col2:
				st.success("Probabilité")

  
    
   
