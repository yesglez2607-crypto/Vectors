import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("App para suma de vectores")

with st.sidebar:
    st.markdown("Elige la magnitud y dirección de los vectores $ \overrightarrow{A} $ y $ \overrightarrow{B} $ ")
    A_mag = st.slider('Magnitud del vector A', 0.0, 10.0, 1.0,step=0.1)
    B_mag = st.slider('Magnitud del vector B', 0.0, 10.0, 2.0,step=0.1)
    A_theta = st.slider('Dirección del vector A', 0.0, 360.0, 10.0)
    B_theta = st.slider('Dirección del vector B', 0.0, 360.0, 45.0)

deg2rad = 2.0*np.pi/360.0
A_theta_rad = deg2rad*A_theta
B_theta_rad = deg2rad*B_theta

Ax = A_mag*np.cos(A_theta_rad)
Ay = A_mag*np.sin(A_theta_rad)
Bx = B_mag*np.cos(B_theta_rad)
By = B_mag*np.sin(B_theta_rad)

Cx = Ax + Bx
Cy = Ay + By
C_mag = np.sqrt(Cx*Cx+Cy*Cy)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

xmax = max(abs(Ax),abs(Cx))+max(abs(Ax),abs(Cx))*0.3
xmin = -xmax
ymax = max(abs(Ay),abs(Cy))+max(abs(Ay),abs(Cy))*0.3
ymin = -ymax
width_l = max(xmax,ymax)*0.001
le = max(xmax,ymax)
head_w = 6.0*width_l

ax.arrow(0,0,Ax,Ay,width=width_l,color='red',length_includes_head=True,animated=True,head_width=head_w)
ax.arrow(Ax,Ay,Bx,By,width=width_l,color='blue',length_includes_head=True,animated=True,head_width=head_w)
ax.arrow(0,0,Cx,Cy,width=width_l,color='green',length_includes_head=True,animated=True,head_width=head_w)
ax.grid()

ax.set(xlim=(-le, le), ylim=(-le, le))
st.pyplot(fig)
