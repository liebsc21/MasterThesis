# -*- coding: utf-8 -*-
"""
plot of cross section as contour with squark and gluino mass as axis
only u-squarks, no antisquarks
"""

from matplotlib import pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

                          
def nans(shape, dtype=float):
    """grid of shape full nan"""
    a = np.empty(shape, dtype)
    a.fill(np.nan)
    return a

# grid size
N = 10 

def contourdata():
    """
    
    """
    mass_sq = np.linspace(100, 2000, num=N)
    mass_glu = np.linspace(100, 3000, num=N)
    # note reverse ordering for yi and xi because of the way   
    # shape works in numpy    
                                                  
    sigmaLR = nans((len(mass_sq),len(mass_glu)))  
    myfile = open('MSSM_1L_uu_suLsuR.txt', 'r')     
    i = 0
    for line in myfile:
        data = line.split()
        for j in range(0,N):
            sigmaLR[j][i] = data[j]
        i += 1   
    myfile.close()
    
    sigmaLL = nans((len(mass_sq),len(mass_glu)))  
    myfile = open('MSSM_1L_uu_suLsuL.txt', 'r')     
    i = 0
    for line in myfile:
        data = line.split()
        for j in range(0,N):
            sigmaLL[j][i] = data[j]
        i += 1   
    myfile.close()
    
    sigmaTree = nans((len(mass_sq),len(mass_glu)))  
    myfile = open('MSSM_Tree_uu_susu.txt', 'r')     
    i = 0
    for line in myfile:
        data = line.split()
        for j in range(0,N):
            sigmaTree[j][i] = data[j]
        i += 1   
    myfile.close()
    
    K = (sigmaLR + 2*sigmaLL)/sigmaTree
    v = np.linspace(0.5, 1.7, 13, endpoint=True)
    fig = plt.figure(1,figsize=(9, 8)) 
    ax1 = plt.axes()
    font_size = 18
    plt.xlabel(r"$m_{\tilde{q}}$ in GeV", size = font_size)
    plt.ylabel(r"$m_{\tilde{g}}$ in GeV", size = font_size)
    plt.xticks(fontsize = font_size)
    plt.yticks(fontsize = font_size)
    cf=ax1.contourf(mass_sq, mass_glu, K, v, vmin=0.5, vmax = 2)
    
    levels1 = [0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7]
    cl1 = plt.contour(cf, levels=levels1,
                  colors='k',
                  linewidths=(1,),
                  hold='on')

    cbar = fig.colorbar(cf, ticks=v, orientation='horizontal')
    cbar.ax.set_xlabel(r'$K_{\mathrm{MSSM}}(pp \to \tilde{u}_L\tilde{u}_R)$ in fb', size = font_size)
    cbar.ax.tick_params(labelsize=font_size)
    cbar.add_lines(cl1)
    plt.show()
    
contourdata()
 
