import streamlit as st
import pandas as pd               
import numpy as np                
import matplotlib.pyplot as plt   
import seaborn as sns 
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn import model_selection

def show():
    st.title("Árbol de decisión")
    file=st.file_uploader("Elege un archivo de entrada")
    if file != None:
        archivo = pd.read_csv(file)
        st.dataframe(archivo)
        st.subheader("Descripción de los datos")
        st.dataframe(archivo.describe())

        st.subheader("Mapa de colores")
        fig = plt.figure(figsize=(14,7))
        MatrizCorr = np.triu(archivo.corr())
        sns.heatmap(archivo.corr(), cmap='RdBu_r', annot=True, mask=MatrizCorr)
        st.pyplot(fig)