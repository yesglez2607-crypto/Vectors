import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
st.title("App para suma de vectores")
st.markdown("Elige la magnitud y dirección de los vectores $ \overrightarrow{A} $ y $ \overrightarrow{B} $ ")
Ax = st.slider('Magnitud del vector A', 0.0, 10.0, 1.0,step=0.1)
Ay = st.slider('Magnitud del vector B', 0.0, 10.0, 2.0,step=0.1)
Bx = st.slider('Dirección del vector A', 0.0, 360.0, 10.0)
By = st.slider('Dirección del vector B', 0.0, 360.0, 45.0)

x = np.linspace(-10,10,100,dtype=float)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x,y)
st.pyplot(fig)
