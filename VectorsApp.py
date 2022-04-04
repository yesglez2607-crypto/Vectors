import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
st.title("App para suma de vectores")
st.markdown("Elige la magnitud y dirección de los vectores $ \overrightarrow{A} $ y $ \overrightarrow{B} $ ")

with st.sidebar:
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

#st.write(Ax,Ay)
#x = np.linspace(-10,10,100,dtype=float)
#y = np.sin(x)
#fig, ax = plt.subplots()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
#
xmax = max(abs(Ax),abs(Cx))+max(abs(Ax),abs(Cx))*0.3
xmin = -xmax
ymax = max(abs(Ay),abs(Cy))+max(abs(Ay),abs(Cy))*0.3
ymin = -ymax


ax.arrow(0,0,Ax,Ay,width=abs(xmax)*0.01,color='red',length_includes_head=True,animated=True)
ax.arrow(Ax,Ay,Bx,By,width=abs(xmax)*0.01,color='blue',length_includes_head=True,animated=True)
ax.arrow(0,0,Cx,Cy,width=abs(xmax)*0.01,color='green',length_includes_head=True,animated=True)
ax.grid()
#plt.text(Ax/2.0, Ay/2, "A", size=np.int(abs(xmax)*1.5), rotation=A_theta,ha="center", va="center",)

#st.write("xmin = ",xmin, " xmax = ",xmax)
#st.write("ymin = ",ymin, " ymax = ",ymax)
#st.write(Ax,Ax+Bx,abs(Ax),abs(Ax+Bx))
#st.write(Ay,Ay+By,abs(Ay),abs(Ay+By))
#st.write(Cx,Cy)
#xmin, xmax, ymin, ymax = ax.axis([xmin, xmax, ymin, ymax])
ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax))
ax.axis('on')
#ax.plot(x,y)
st.pyplot(fig)
