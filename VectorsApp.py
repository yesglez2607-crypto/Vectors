import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("App para suma de vectores")

with st.sidebar:
    st.markdown("Elige la magnitud del vector $ \overrightarrow{F_1}$ ")
    F1_mag = st.number_input("magnitud:",0.000)
    st.markdown("Elige la magnitud y dirección del vector $ \overrightarrow{F_2} $")
    #A_mag = st.slider('Magnitud del vector A', 0.0, 10.0, 1.0,step=0.1)
    F2_mag = st.number_input("magnitud de F2:",0.000)
    F2_theta = st.number_input("ángulo de F2:",0.000) 
    st.markdown("Elige la magnitud y dirección del vector $ \overrightarrow{F_3} $")
    #A_mag = st.slider('Magnitud del vector A', 0.0, 10.0, 1.0,step=0.1)
    F3_mag = st.number_input("magnitud de F3:",0.000)
    F3_theta = st.number_input("ángulo de  F3:",0.000)
    #B_mag = st.number_input("",0.0)    
    #B_theta= st.number_input("pon un ángulo B",0.000)
    #B_mag = st.slider('Magnitud del vector B', 0.0, 10.0, 2.0,step=0.1)
    # A_theta = st.slider('Dirección del vector A', 0.0, 360.0, 10.0)
    #  B_theta = st.slider('Dirección del vector B', 0.0, 360.0, 45.0)

deg2rad = 2.0*np.pi/360.0
F3_theta_rad = deg2rad*F2_theta
F3_theta_rad = deg2rad*F3_theta

F1x = F1_mag
F2x = F2_mag*np.cos(F2_theta_rad)
F2y = F2_mag*np.sin(F2_theta_rad)
F3x = F3_mag*np.cos(F3_theta_rad)
F3y = F3_mag*np.sin(F3_theta_rad)

FRx = F2x + F3x
FRy = F2y + F3y
FR_mag = np.sqrt(FRx*FRx+FRy*FRy)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

xmax = max(abs(F2x),abs(FRx))+max(abs(F2x),abs(FRx))*0.3
xmin = -xmax
ymax = max(abs(F2y),abs(FRy))+max(abs(F2y),abs(FRy))*0.3
ymin = -ymax
width_l = max(xmax,ymax)*0.001
le = max(xmax,ymax)
head_w = 20.0*width_l
ax.axhline(0,color='black') # x = 0
ax.axvline(0,color='black') # y = 0


ax.arrow(0,0,F1x,F2y,width=width_l,color='purple',length_includes_head=True,animated=True,head_width=head_w)
ax.arrow(0,0,F2x,F2y,width=width_l,color='red',length_includes_head=True,animated=True,head_width=head_w)
ax.arrow(F2x,F2y,F3x,F3y,width=width_l,color='blue',length_includes_head=True,animated=True,head_width=head_w)
ax.arrow(0,0,FRx,FRy,width=width_l*10,color='darkorange',length_includes_head=True,animated=True,head_width=head_w)
ax.grid(color='green', linestyle='-.', linewidth=0.2)
st.write("componentes: ",Cx,Cy)
ax.set(xlim=(-le, le), ylim=(-le, le))
st.pyplot(fig)
