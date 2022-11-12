import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import math as mt
import os
from matplotlib.transforms import IdentityTransform

st.set_page_config(layout="wide")
st.title("Práctica de laboratorio No 5")
st.markdown(" ## Vectores: Fuerzas en equilibrio ")


with st.sidebar:
    st.markdown("Elige la magnitud del vector $ \overrightarrow{F_1}$ ")
    F1_mag = st.number_input("magnitud:",0.0000)
    st.markdown("Elige la magnitud y dirección del vector $ \overrightarrow{F_2} $")
    
    F2_mag = st.number_input("magnitud de F2:",0.0000)
    F2_theta = st.number_input("ángulo de F2:",0.0000) 
    st.markdown("Elige la magnitud y dirección del vector $ \overrightarrow{F_3} $")
    
    F3_mag = st.number_input("magnitud de F3:",0.0000)
    F3_theta = st.number_input("ángulo de  F3:",0.0000)
    

    st.image('Dorado.jpg')
    st.markdown(""" 
             ### *Autores:*


             **Dr. Juan Pedro Palomares Báez**


             **Dr. José Manuel Nápoles Duarte**


             **MC. Carlos Armando de la Vega Cobos**
             
             """)


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

fig = plt.figure(figsize=(5, 5), dpi=300)
ax = fig.add_axes([0.25,0.052,0.8,0.87],polar=True)

plt.rc('grid', color='#316931', linewidth=2, linestyle='-')
plt.rc('xtick', labelsize=12)  
plt.rc('ytick', labelsize=1)

nn3=1.0
nn1 = max(F1_mag,F2_mag)
nn2 = max(F3_mag,FR_mag)
nn3=max(nn1,nn2)
ax.set_facecolor('azure')

if nn3 != 0.0:
    F1_mag=F1_mag/nn3
    F2_mag=F2_mag/nn3
    F3_mag=F3_mag/nn3
    FR_mag=FR_mag/nn3

#F1x = F1_mag
#F2x = F2_mag*np.cos(F2_theta_rad)
#F2y = F2_mag*np.sin(F2_theta_rad)
#F3x = F3_mag*np.cos(F3_theta_rad)
#F3y = F3_mag*np.sin(F3_theta_rad)

width1 =  0.2 #min(min(min(F1_mag,F2_mag),F3_mag),FR_mag)
head_w=width1*1.8
head_l1=F1_mag*0.2
head_l2=F2_mag*0.2
head_l3=F3_mag*0.2
head_l4=FR_mag*0.2
fntz = 18.0
col1, col2 = st.columns(2)
ax.grid(True,lw=0.8,linestyle='--',zorder=0)
with col1:
    if F1_mag != 0.0:
        ax.arrow(0.0,0.0,0.0,F1_mag,width=width1,edgecolor = 'black', facecolor = 'darkgreen',length_includes_head=True,animated=True,head_width=head_w,head_length=head_l1,lw=2.0,zorder=3)
        ax.text(-1.85,1.6,r'  ',fontsize = fntz, color='darkgreen')  
        ax.text(1420,1050,r'$ \overrightarrow{F_1} $',fontsize = fntz, color='darkgreen',zorder=7,transform=IdentityTransform()) 
    if F2_mag !=0.0 and F2_theta != 0.0:    
        ax.arrow(F2_theta*np.pi/180.0,0.0,0.0,F2_mag,width=width1,edgecolor = 'black', facecolor = 'red',length_includes_head=True,animated=True,head_width=head_w,head_length=head_l2,lw=2.0,zorder=4)
        #ax.text(-1.7,1.454,r'$ \overrightarrow{F_2} $',fontsize = fntz, color='red') 
        ax.text(1420,850,r'$ \overrightarrow{F_2} $',fontsize = fntz, color='red',zorder=7,transform=IdentityTransform()) 
    if F3_mag !=0.0 and F3_theta != 0.0:
        ax.arrow(F3_theta*np.pi/180.0,0.0,0.0,F3_mag,width=width1,edgecolor = 'black', facecolor = 'blue',length_includes_head=True,animated=True,head_width=head_w,head_length=head_l3,lw=2.0,zorder=5)
        ax.arrow(FR_theta,0.0,0.0,FR_mag,width=width1,edgecolor = 'black', facecolor = 'darkorange',length_includes_head=True,animated=True,head_width=head_w,head_length=head_l4,lw=2.0,zorder=6) 
        #ax.text(-1.54,1.442,r'$ \overrightarrow{F_3} $',fontsize = fntz, color='blue') 
        #ax.text(-1.38,1.465,r'$ \overrightarrow{F_R} $',fontsize = fntz, color='darkorange') 
        ax.text(1420,500,r'$ \overrightarrow{F_3} $',fontsize = fntz, color='blue',zorder=7,transform=IdentityTransform())
        ax.text(1420,300,r'$ \overrightarrow{F_R} $',fontsize = fntz, color='darkorange',zorder=7,transform=IdentityTransform()) 
    st.pyplot(fig)
    plt.savefig('plot.png')
    plt.show()
    
   # st.pyplot(fig)


#    if btn == True:
      #  plt.savefig('plot.png')

str1="#### $ \overrightarrow{F_1} = $ " + " {:.4f}".format(F1x) + " $ i $"
strr = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">' + str1 + '</p>'
str2="#### $ \overrightarrow{F_2} = $ " + " {:.4f}".format(F2x) + " $ i $" + " + " + " {:.4f}".format(F2y) + " $ j $"
str3="#### $ \overrightarrow{F_3} = $ " + " {:.4f}".format(F3x) + " $ i $" + " + " + " {:.4f}".format(F3y) + " $ j $"
str4="#### $ \overrightarrow{F_R} = \overrightarrow{F_2} + \overrightarrow{F_3} = $ " + " {:.4f}".format(FRx) + " $ i $" + " + " + " {:.4f}".format(FRy) + " $ j $"
str5="#### $ \overrightarrow{F_1} + \overrightarrow{F_R} = $" + " {:.4f}".format(FRx+F1x) + " $ i $" + " + " + " {:.4f}".format(FRy) + " $ j $ "

with col2:
    st.write('    ')
    st.write('    ')
    st.write('    ')
    st.write('    ')
    st.write('    ')    
    st.markdown(""" 
    ### Vectores de las fuerzas 
    

    
    
    """)

    if F1_mag != 0.0:
        st.markdown(str1)   
    if F2_mag !=0.0 and F2_theta != 0.0:
        st.markdown(str2)   
    if F3_mag !=0.0 and F3_theta != 0.0:
        st.markdown(str3)
        st.markdown(str4)
        st.markdown(str5)

with open("plot.png", "rb") as file:
    btn = st.download_button(
        label="Descargar imagen",
        data=file,
        file_name=None,
        mime="image/png"
        )
    if btn:  
        os.system("rm *.png") 
