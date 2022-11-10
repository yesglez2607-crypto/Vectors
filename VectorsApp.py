import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("App para suma de vectores")

with st.sidebar:
    st.markdown("Elige la magnitud del vector $ \overrightarrow{F_1}$ ")
    F1_mag = st.number_input("magnitud:",0.0000)
    st.markdown("Elige la magnitud y dirección del vector $ \overrightarrow{F_2} $")
    #A_mag = st.slider('Magnitud del vector A', 0.0, 10.0, 1.0,step=0.1)
    F2_mag = st.number_input("magnitud de F2:",0.0000)
    F2_theta = st.number_input("ángulo de F2:",0.0000) 
    st.markdown("Elige la magnitud y dirección del vector $ \overrightarrow{F_3} $")
    #A_mag = st.slider('Magnitud del vector A', 0.0, 10.0, 1.0,step=0.1)
    F3_mag = st.number_input("magnitud de F3:",0.0000)
    F3_theta = st.number_input("ángulo de  F3:",0.0000)
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
#ax = fig.add_subplot(111,polar=True)
ax = fig.add_axes([0.0,0.0,1.0,1.0],polar=True)
#ax.spines['left'].set_position('center')
#ax.spines['bottom'].set_position('center')
#fig2 = plt.figure()
# radar green, solid grid lines
plt.rc('grid', color='#316931', linewidth=1, linestyle='-')
plt.rc('xtick', labelsize=15)
plt.rc('ytick', labelsize=15)
# force square figure and square axes looks better for polar, IMO
#width = 400
#height = 400
# matplotlib.rcParams['figure.figsize']
#size = min(width, height)
# make a square figure
#fig = plt.figure(figsize=(size, size))
#ax = fig.add_subplot(111)



#ax = fig.add_axes([0.0, 0.0, 0.8, 0.8], polar=True)
xm1 = max(abs(F1x),abs(F2x))
xm2 = max(abs(F3x),abs(FRx))
xmax = max(xm1,xm2)
ym1 = max(abs(F2y),abs(F3y))
ymax = max(abs(FRy),ym1)
#xmin = -xmax
#ymin = -ymax
width_l = max(xmax,ymax)*0.015
#le1 = max(xmax,ymax)
#le = le1*1.3
lx=xmax*1.2
ly=ymax*1.5
head_w = 4.0*width_l
ax.axhline(0,color='black') # x = 0
ax.axvline(0,color='black') # y = 0

#ax.annotate("", xy=(0.0,F1x), xytext=(0, 0),arrowprops=dict(arrowstyle="->",color='red',lw=2.5))
if F1_mag != 0.0:
    ax.arrow(0.0,0.0,0.0,F1x,width=width_l,color='purple',length_includes_head=True,animated=True,head_width=head_w)
    st.write(" $ \overrightarrow{F_1} = $ ","{:.4f}".format(F1x),"$ i $")
if F2_mag !=0.0 and F2_theta != 0.0:    
    ax.arrow(F2_theta*np.pi/180.0,0.0,0.0,F2_mag,width=width_l,color='red',length_includes_head=True,animated=True,head_width=head_w)
    st.write(" $ \overrightarrow{F_2} = $ ","{:.4f}".format(F2x),"$ i $"," + ","{:.4f}".format(F2y),"$ j $")
if F3_mag !=0.0 and F3_theta != 0.0:
    ax.arrow(F3_theta*np.pi/18,0.0,0.0,F3_mag,width=width_l,color='blue',length_includes_head=True,animated=True,head_width=head_w)
    ax.arrow(0.,0.,FRy,FRx,width=width_l,color='darkorange',length_includes_head=True,animated=True,head_width=head_w) 
    st.write(" $ \overrightarrow{F_3} = $ ","{:.4f}".format(F3x),"$ i $"," + ","{:.4f}".format(F3y),"$ j $")
    st.write(" $ \overrightarrow{F_R} = $ ","{:.4f}".format(F3y),"$ i $"," + ","{:.4f}".format(FRy),"$ j $")
    st.write(" $ \overrightarrow{F_1} + \overrightarrow{F_R} = $","{:.4f}".format(FRx+F1x),"$ i $"," + ","{:.4f}".format(FRy),"$ j $")


########### ax.grid(color='green', linestyle='-.', linewidth=0.2)

# ax = plt.subplot(111, projection='polar')
#ax.plot(azi*np.pi/180, time, color='black', marker='D', markerfacecolor='limegreen')
#ax.set_theta_zero_location('N')
#ax.set_theta_direction(-1) # clockwise
ax.grid(True)
st.pyplot(fig)
#ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True,

# ax.set_ylabel('Time', color='crimson')
#ax.tick_params(axis='y', colors='crimson')

#ax.set(xlim=(-lx, lx), ylim=(-ly, ly))
##plt.axis('equal')
#st.pyplot(fig)




#r = np.arange(0, 3.0, 0.01)
#theta = 2*np.pi*r
#ax2.plot(theta, r, color='#ee8d18', lw=3)
#ax2.set_rmax(2.0)
#grid(True)

#ax2.set_title("And there was much rejoicing!", fontsize=20)
#This is the line I added:
#arr = plt.arrow(0, 0.5, 0,1 , alpha = 0.5, width = 0.1,edgecolor = 'black', facecolor = 'green',lw = 2)

#plt.show()





#picture = st.camera_input("Take a picture")

#if picture:
#    st.image(picture)
