# lineplot.py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mb
import pandas as pd

data = np.loadtxt("C:\\Users\\ywq\\Desktop\\example.csv", delimiter=",")



#data = pd.read_excel('C:\\Users\\ywq\\Desktop\\example.xlsx',
#                      sheetname = 'Sheet1',
#                      header = 0,
#                      index_col = 0,
#                      parse_cols = "A, B, C, D",
#                      convert_float = True)


titlefont = {
        'family' : 'serif',
        'color'  : 'Indigo',
        'weight' : 'normal',
        'size'   : 'x-large',
        }
 
labelfont = {
        'family' : 'sans-serif',
        'color'  : 'black',
        'weight' : 'normal',
        'size'   : 'medium',
        }
 
annotationfont = {
        'family' : 'monospace',         
        'color'  : (0, 0.27, 0.08),  
        'weight' : 'normal',
        'size'   : 14,
        }
 
plt.figure()
plt.plot(data[:,0], data[:,1],
         color = (0, 0.18, 0.3),
         linestyle = '-.',
         linewidth = 3,
         label = 'graph for $sin(x)$'
         )
 
plt.plot(data[:,0], data[:,3],
         color = '#A30000',
         linestyle = '--',
         linewidth = 3,
         label = 'graph for $cos(x)$'
         )
 
plt.xlim(300.0, 800.0)
plt.ylim(-1.2, 10.0)
 
plt.xlabel('Wavelength (nm)', fontdict = labelfont)
plt.ylabel('Value (a.u.)', fontdict = labelfont)
plt.title('One example', fontdict = titlefont)
 
#plt.xticks(
#    (0, pi/2, pi, 3*pi/2, 2*pi, 5*pi/2, 3*pi),
#    ('$0$', '$0.5 \pi$', '$\pi$', '$1.5 \pi$', '$2 \pi$', '$2.5 \pi$', '$3 \pi$')
#    )
 
legend = plt.legend(
                    shadow = True,
                    frameon = True,
                    fancybox = True,
                    ncol = 2,
                    fontsize = 'medium',
                    mode = 'expand',
                    loc = 'upper left',
                    )
frame = legend.get_frame()
frame.set_facecolor('White')
frame.set_edgecolor('Gray')
 
plt.text(600, 6, 
         'This is an\n annotation', 
         fontdict = annotationfont)

axes = plt.gca()
plt.minorticks_on()
#axes.grid(b = True, 
#          which = 'both', 
#          axis = 'y', 
#          color = 'Gray', 
#          linestyle = '--', 
#          alpha = 0.5,
#          linewidth = 2)
plt.grid()
 
#axes.set_axis_bgcolor('MintCream')  
 
mb.rcParams['xtick.direction'] = 'out'
mb.rcParams['ytick.direction'] = 'out'
 
plt.show()
