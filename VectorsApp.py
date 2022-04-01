import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
st.title("App para suma de vectores")
st.markdown("Elige la magnitud y dirección de los vectores $ \overrightarrow{A} $ y $ \overrightarrow{B} $ ")
A_mag = st.slider('Magnitud del vector A', 0.0, 10.0, 1.0,step=0.1)
B_mag = st.slider('Magnitud del vector B', 0.0, 10.0, 2.0,step=0.1)
A_theta = st.slider('Dirección del vector A', 0.0, 360.0, 10.0)
B_theta = st.slider('Dirección del vector B', 0.0, 360.0, 45.0)
Ax = A_mag*np.cos(2.0*np.pi*A_theta/360.0)
Ay = A_mag*np.sin(2.0*np.pi*A_theta/360.0)
Bx = B_mag*np.cos(2.0*np.pi*B_theta/360.0)
By = B_mag*np.sin(2.0*np.pi*B_theta/360.0)
Cx = Ax + Bx
Cy = Ay + By
#st.write(Ax,Ay)
#x = np.linspace(-10,10,100,dtype=float)
#y = np.sin(x)
fig, ax = plt.subplots()
#
ax.arrow(0,0,Ax,Ay,width=0.1,color='red',length_includes_head=True)
ax.arrow(Ax,Ay,Cx,Cy,width=0.1,color='blue',length_includes_head=True)
ax.arrow(0,0,Cx,Cy,width=0.1,color='green',length_includes_head=True)
ax.grid()
xmax = max(abs(Ax),abs(Ax+Bx))+max(abs(Ax),abs(Ax+Bx))*0.1
xmin = -xmax
ymax = max(abs(Ay),abs(Ay+By))+max(abs(Ay),abs(Ay+By))*0.1
ymin = -ymax
st.write("xmin = ",xmin, " xmax = ",xmax)
st.write("ymin = ",ymin, " ymax = ",ymax)
st.write(Ax,Ax+Bx,abs(Ax),abs(Ax+Bx))
st.write(Ay,Ay+By,abs(Ay),abs(Ay+By))
st.write(Cx,Cy)
ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax),on=True)
#ax.axis(on=True)
#ax.plot(x,y)
st.pyplot(fig)
