import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
st.title("App para suma de vectores")
st.markdown("Elige la magnitud y dirección de los vectores $ \overrightarrow{A} $ y $ \overrightarrow{B} $ ")
A_mag = st.slider('Magnitud del vector A', 0.0, 10.0, 1.0,step=0.1)
B_mag = st.slider('Magnitud del vector B', 0.0, 10.0, 2.0,step=0.1)
A_theta = st.slider('Dirección del vector A', 0.0, 360.0, 10.0)
B_theta = st.slider('Dirección del vector B', 0.0, 360.0, 45.0)
Ax = A_mag*np.cos(np.pi*A_theta/180.0)
Ay = A_mag*np.sin(np.pi*A_theta/180.0)
Bx = B_mag*np.cos(np.pi*B_theta/180.0)
By = B_mag*np.sin(np.pi*B_theta/180.0)
#st.write(Ax,Ay)
#x = np.linspace(-10,10,100,dtype=float)
#y = np.sin(x)
fig, ax = plt.subplots()
#
ax.arrow(0,0,Ax,Ay,width=0.1,color='red')
ax.arrow(Ax,Ay,Ax+Bx,Ay+By,width=0.1,color='blue')
ax.grid()
xmax = max(abs(Ax),abs(Ax+Bx))
xmin = -xmax
ymin = xmin
ymax = xmax
ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax))
#ax.plot(x,y)
st.pyplot(fig)
