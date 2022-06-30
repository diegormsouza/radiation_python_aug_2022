#-----------------------------------------------------------------------------------------------------------
# INPE / CGCT / DISSM - Training: Wien's Displacement Law
# Author: Diego Souza & Simone Sievert
#-----------------------------------------------------------------------------------------------------------
# Required modules
import pandas                       # Python Data Analysis Library
import matplotlib.pyplot as plt     # Plotting library
import numpy as np                  # Scientific computing with Python
#-----------------------------------------------------------------------------------------------------------

# Choose the plot size (width x height, in inches)
fig, ax = plt.subplots(figsize=(16, 8))

# Plot title
plt.title(f'Wien\'s Displacement Law',  fontsize=12, fontweight='bold')

# X axis
plt.xlabel("Wavelenght", fontsize=12, fontweight='bold')

# X axis limits and ticks
plt.xlim(0, 3)
plt.xticks([0,0.5,1,1.5,2,2.5,3])

# Y axis
plt.ylabel("W/m2/µm", fontsize=12, fontweight='bold')

# Y axis limits and ticks
plt.ylim(0, 1500)
plt.yticks([0, 300, 600, 900, 1200, 1500])

# Constantes físicas
h = 6.626e-34
c = 3.0e+8
k = 1.38e-23

#input data
Ts = 6000. # Kelvin [K]]
Dn = 1.5E11 # Distancia Terra e Sol [m]
Rs = 6.8E8 # Raio do Sol [m]

scale = ( Rs**2 )/( Dn**2 )

def planck(wav, T):
    h = 6.626e-34
    c = 3.0e+8
    k = 1.38e-23

    a = 2.0*np.pi*h*c**2
    b = h*c/(wav*k*T)

    intensity = a / ((wav**5) * (np.exp(b) - 1.0))
    return intensity

# generate x-axis in increments from 1nm to 3 micrometer in 1 nm increments
# starting at 1 nm to avoid wav = 0, which would result in division by zero.
wavelengths = np.arange(1e-9, 3e-6, 1e-9) 

temperatures = [(3500, 'darkred'), (4000, 'red'), (4500, 'orange'), (5000, 'gold'), (5500, 'lightgreen')]
peaks = []

for Ts, color in temperatures:

  intensity = planck(wavelengths, Ts)
  wavelenghts = wavelengths * 1E6
  intensity = intensity * 1E-6 * scale

  # Create the line plot  
  plt.plot(wavelenghts, intensity, color=color, marker='', markersize = 1, linewidth = 2.0, label =  str(Ts) + 'k') 

  # Find the maximuns
  y = np.argmax(intensity)
  max_wavelenght = wavelenghts[y]

  # Plot the reference line
  ax.plot([max_wavelenght, max_wavelenght], [0, intensity[y]], color = 'black', linestyle = '--', linewidth = 0.7, zorder=1)  

  # Plot the text and circle
  ax.text(max_wavelenght, intensity[y] + 30, 'T = ' + str(Ts) + ' K\n \u03BB = ' + str(max_wavelenght.round(2)) + ' μm')
  ax.scatter(max_wavelenght, intensity[y], s = 100, color=color, zorder=2)
  peaks.append((max_wavelenght, intensity[y]))

# Connect the peaks
plt.plot((peaks[0][0],peaks[1][0]),(peaks[0][1],peaks[1][1]),'--', color = 'red', zorder=0) 
plt.plot((peaks[1][0],peaks[2][0]),(peaks[1][1],peaks[2][1]),'--', color = 'red', zorder=0) 
plt.plot((peaks[2][0],peaks[3][0]),(peaks[2][1],peaks[3][1]),'--', color = 'red', zorder=0) 
plt.plot((peaks[3][0],peaks[4][0]),(peaks[3][1],peaks[4][1]),'--', color = 'red', zorder=0) 

# Plot the UV line and text
ax.plot([0.4, 0.4], [0, 10000], color = 'blue', linestyle = '--', linewidth = 0.5, zorder=1)  
ax.text(0.15, 1450, "ULTRAVIOLET", color='black')

# Plot the IR line and text
ax.plot([0.7, 0.7], [0, 10000], color = 'blue', linestyle = '--', linewidth = 0.5, zorder=1)
ax.text(0.73, 1450, "INFRARED", color='black')

# Plot the VIS text
ax.text(0.5, 1450, "VISIBLE", color='black')

# Add a legend
plt.legend()

# Add grids
plt.grid(axis='x', color='0.90')
plt.grid(axis='y', color='0.90')

plt.annotate(f'Increase of intensity with\ntemperature and decrease\nof peak lenght with temperature', xy=(0.50, 0.80), xycoords = ax.transAxes, fontsize=14, 
             fontweight='bold', color='gold', bbox=dict(boxstyle="round",fc=(0.0, 0.0, 0.0, 0.5), ec=(1., 1., 1.)), alpha = 1.0)
#---------------------------------------------------------------------------------------------------------------------------
