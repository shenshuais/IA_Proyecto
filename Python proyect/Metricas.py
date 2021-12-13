import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from scipy.spatial import distance
def show():
    st.title("Métricas de distancia")
    file=st.file_uploader("Elege un archivo de entrada")
    if file != None:
        Hipoteca = pd.read_csv(file)
        st.subheader("El contenido del archivo")
        st.dataframe(Hipoteca)

        Opcion=st.sidebar.radio("Seleccionar la metrica",("--","Euclidiana","Chebyshev",
        "Cityblock","Minkowski"))
        if Opcion == "Euclidiana":

            st.subheader("Euclidiana")
            DstEuclidiana= cdist(Hipoteca.iloc[0:10], Hipoteca.iloc[0:10], metric='euclidean')
            MEuclideana = pd.DataFrame(DstEuclidiana)
            st.write(MEuclideana)

        elif Opcion == "Chebyshev":
            st.subheader("Chebyshev")
            Dstchebyshev= cdist(Hipoteca, Hipoteca, metric='chebyshev')
            Mchebyshev = pd.DataFrame(Dstchebyshev)
            st.write( Mchebyshev)
        elif Opcion == "Cityblock":
            st.subheader("Cityblock")
            Dstcityblock= cdist(Hipoteca, Hipoteca, metric='cityblock' )
            Mcityblock = pd.DataFrame(Dstcityblock)
            st.write(Mcityblock)
        elif Opcion == "Minkowski":
            st.subheader("Minkowski")
            pe = st.slider('Lambda', 1.0, 10.0,step=0.5)
            Dstminkowski= cdist(Hipoteca, Hipoteca, metric='minkowski', p=pe)
            Mminkowski = pd.DataFrame(Dstminkowski)
            st.write(Mminkowski)
        else:
            st.write("Ingrese una opcion de la barra lateral")