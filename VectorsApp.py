import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import math as mt
st.set_page_config(layout="wide")
st.title("Práctica de laboratorio No 5")
st.markdown(" ##     Vectores: Fuerzas en equilibrio ")

with st.sidebar:
    st.markdown("Elige la magnitud del vector $ \overrightarrow{F_1}$ ")
    F1_mag = st.number_input("magnitud:",0.0000)
    st.markdown("Elige la magnitud y dirección del vector $ \overrightarrow{F_2} $")
    
    F2_mag = st.number_input("magnitud de F2:",0.0000)
    F2_theta = st.number_input("ángulo de F2:",0.0000) 
    st.markdown("Elige la magnitud y dirección del vector $ \overrightarrow{F_3} $")
    
    F3_mag = st.number_input("magnitud de F3:",0.0000)
    F3_theta = st.number_input("ángulo de  F3:",0.0000)


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
FR_theta = mt.atan2(FRy,FRx)

fig = plt.figure()
ax = fig.add_axes([0.0,0.0,1.0,1.0],polar=True)

plt.rc('grid', color='#316931', linewidth=3, linestyle='-')
plt.rc('xtick', labelsize=16)  
plt.rc('ytick', labelsize=1)

nn1 = max(F1_mag,F2_mag)
nn2 = max(F3_mag,FR_mag)
nn3=max(nn1,nn2)

F1_mag=F1_mag/nn3
F2_mag=F2_mag/nn3
F3_mag=F3_mag/nn3
FR_mag=FR_mag/nn3

width1 = 0.2 
head_w=width1*1.8
head_l=head_w*0.9

col1, col2 = st.columns(2)

with col1:
    if F1_mag != 0.0:
        ax.arrow(0.0,0.0,0.0,F1_mag,width=width1,edgecolor = 'black', facecolor = 'purple',length_includes_head=True,animated=True,head_width=head_w,head_length=head_l,lw=2.0)
    if F2_mag !=0.0 and F2_theta != 0.0:    
        ax.arrow(F2_theta*np.pi/180.0,0.0,0.0,F2_mag,width=width1,edgecolor = 'black', facecolor = 'red',length_includes_head=True,animated=True,head_width=head_w,head_length=head_l,lw=2.0)
    if F3_mag !=0.0 and F3_theta != 0.0:
        ax.arrow(F3_theta*np.pi/180.0,0.0,0.0,F3_mag,width=width1,edgecolor = 'black', facecolor = 'blue',length_includes_head=True,animated=True,head_width=head_w,head_length=head_l,lw=2.0)
        ax.arrow(FR_theta,0.0,0.0,FR_mag,width=width1,edgecolor = 'black', facecolor = 'darkorange',length_includes_head=True,animated=True,head_width=head_w,head_length=head_l,lw=2.0) 

    ax.grid(True,lw=0.8,linestyle='--')
    st.pyplot(fig)

with col2:
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.markdown(""" ### Vectores de las fuerzas 
    
    
    
    
    """)

    if F1_mag != 0.0:
        st.write(" $ \overrightarrow{F_1} = $ ","{:.4f}".format(F1x),"$ i $")
        st.markdown(' ## $\phi$ ',F1x)
    if F2_mag !=0.0 and F2_theta != 0.0:    
        st.write(" $ \overrightarrow{F_2} = $ ","{:.4f}".format(F2x),"$ i $"," + ","{:.4f}".format(F2y),"$ j $")
    if F3_mag !=0.0 and F3_theta != 0.0:
        st.write(" $ \overrightarrow{F_3} = $ ","{:.4f}".format(F3x),"$ i $"," + ","{:.4f}".format(F3y),"$ j $")
        st.write(" $ \overrightarrow{F_R} = $ ","{:.4f}".format(F3y),"$ i $"," + ","{:.4f}".format(FRy),"$ j $")
        st.write(" $ \overrightarrow{F_1} + \overrightarrow{F_R} = $","{:.4f}".format(FRx+F1x),"$ i $"," + ","{:.4f}".format(FRy),"$ j $")
