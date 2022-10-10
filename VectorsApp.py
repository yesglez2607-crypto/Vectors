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
F2_theta_rad = deg2rad*F2_theta
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
ax = fig.add_subplot(111, projection='polar')
ax.set_theta_zero_location('E')
ax.set_theta_direction(1) # clockwise

xm1 = max(abs(F1x),abs(F2x))
xm2 = max(abs(F3x),abs(FRx))
xmax = max(xm1,xm2)
ym1 = max(abs(F2y),abs(F3y))
ymax = max(abs(FRy),ym1)
#xmin = -xmax
#ymin = -ymax
width_l = max(xmax,ymax)*0.005
le1 = max(xmax,ymax)
le = le1*1.3
head_w = 20.0*width_l
ax.axhline(0,color='black') # x = 0
ax.axvline(0,color='black') # y = 0


ax.arrow(0,0,F1x,0.0,width=width_l,color='purple',length_includes_head=True,animated=True,head_width=head_w)
ax.arrow(0,0,F2x,F2y,width=width_l,color='red',length_includes_head=True,animated=True,head_width=head_w)
ax.arrow(0,0,F3x,F3y,width=width_l,color='blue',length_includes_head=True,animated=True,head_width=head_w)
ax.arrow(0,0,FRx,FRy,width=width_l,color='darkorange',length_includes_head=True,animated=True,head_width=head_w)
ax.grid(color='green', linestyle='-.', linewidth=0.2)

#ax.grid(True)

# ax.set_ylabel('Time', color='crimson')
#ax.tick_params(axis='y', colors='crimson')

#ax.set(xlim=(-le, le), ylim=(-le, le))
#time = np.array([4 ,5 ,6, 7, 10])
#azi = np.array([70 ,100 ,120, 150, 170])
#ax = fig.add_subplot(111, projection='polar')
#ax.plot(azi*np.pi/180, color='black', marker='D', markerfacecolor='limegreen')

st.pyplot(fig)
st.write(" $ \overrightarrow{F_1} = $ ","{:.4f}".format(F1x),"$ i $")
st.write(" $ \overrightarrow{F_2} = $ ","{:.4f}".format(F2x),"$ i $"," + ","{:.4f}".format(F2y),"$ j $")
st.write(" $ \overrightarrow{F_3} = $ ","{:.4f}".format(F3x),"$ i $"," + ","{:.4f}".format(F3y),"$ j $")
st.write(" $ \overrightarrow{F_R} = $ ","{:.4f}".format(F3y),"$ i $"," + ","{:.4f}".format(FRy),"$ j $")
st.write(" $ \overrightarrow{F_1} + \overrightarrow{F_R} = $","{:.4f}".format(FRx+F1x),"$ i $"," + ","{:.4f}".format(FRy),"$ j $")

