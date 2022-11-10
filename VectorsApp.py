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

plt.rc('grid', color='#316931', linewidth=1, linestyle='-')
plt.rc('xtick', labelsize=15)
plt.rc('ytick', labelsize=15)

xm1 = max(abs(F1x),abs(F2x))
xm2 = max(abs(F3x),abs(FRx))
xmax = max(xm1,xm2)
ym1 = max(abs(F2y),abs(F3y))
ymax = max(abs(FRy),ym1)
width_l = max(xmax,ymax)*0.015

nn1 = max(F1_mag,F2_mag)
nn2 = max(F3_mag,FR_mag)
nn3=max(nn1,nn2)

F1_mag=F1_mag/nn3
F2_mag=F2_mag/nn3
F3_mag=F3_mag/nn3
FR_mag=FR_mag/nn3
nn3=1.0 
width1 = nn3*0.2 #F1_mag*0.1
width2 = nn3*0.2 #F2_mag*0.1
width3 = nn3*0.2 #F3_mag*0.1
width4 = nn3*0.2 #FR_mag*0.1

head_w1=width1*1.5
head_w2=width2*1.5
head_w3=width3*1.5
head_w4=width4*1.5

lx=xmax*1.2
ly=ymax*1.5
head_w = 4.0*width_l
col1, col2 = st.columns(2)

with col1:
    if F1_mag != 0.0:
        ax.arrow(0.0,0.0,0.0,F1_mag,width=width1,color='purple',length_includes_head=True,animated=True,head_width=head_w1)
       # st.write(" $ \overrightarrow{F_1} = $ ","{:.4f}".format(F1x),"$ i $")
    if F2_mag !=0.0 and F2_theta != 0.0:    
        ax.arrow(F2_theta*np.pi/180.0,0.0,0.0,F2_mag,width=width2,color='red',length_includes_head=True,animated=True,head_width=head_w2)
       # st.write(" $ \overrightarrow{F_2} = $ ","{:.4f}".format(F2x),"$ i $"," + ","{:.4f}".format(F2y),"$ j $")
    if F3_mag !=0.0 and F3_theta != 0.0:
        ax.arrow(F3_theta*np.pi/180.0,0.0,0.0,F3_mag,width=width3,color='blue',length_includes_head=True,animated=True,head_width=head_w3)
        ax.arrow(FR_theta,0.0,0.0,FR_mag,width=width4,color='darkorange',length_includes_head=True,animated=True,head_width=head_w4) 
       # st.write(" $ \overrightarrow{F_3} = $ ","{:.4f}".format(F3x),"$ i $"," + ","{:.4f}".format(F3y),"$ j $")
       # st.write(" $ \overrightarrow{F_R} = $ ","{:.4f}".format(F3y),"$ i $"," + ","{:.4f}".format(FRy),"$ j $")
       # st.write(" $ \overrightarrow{F_1} + \overrightarrow{F_R} = $","{:.4f}".format(FRx+F1x),"$ i $"," + ","{:.4f}".format(FRy),"$ j $")

    ax.grid(True)
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
