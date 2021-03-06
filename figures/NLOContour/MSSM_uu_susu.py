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
    
    #sigmaTree = nans((len(mass_sq),len(mass_glu)))  
    #myfile = open('MSSM_Tree_uu_susu.txt', 'r')     
    #i = 0
    #for line in myfile:
    #    data = line.split()
    #    for j in range(0,N):
    #        sigmaTree[j][i] = data[j]
    #    i += 1   
    #myfile.close()
    
	
    sigma = (sigmaLR + 2*sigmaLL)#/sigmaTree
    v = 10**np.linspace(-1, 7, 9, endpoint=True)
    fig = plt.figure(1,figsize=(9, 8)) 
    ax1 = plt.axes()
    font_size = 18
    plt.xlabel(r"$m_{\tilde{q}}$ in GeV", size = font_size)
    plt.ylabel(r"$m_{\tilde{g}}$ in GeV", size = font_size)
    plt.xticks(fontsize = font_size)
    plt.yticks(fontsize = font_size)
    cf=ax1.contourf(mass_sq, mass_glu, sigma, v, norm = LogNorm(), vmin=1, vmax =10**6)
    levels1 = [1, 10**3, 10**4, 10**5, 10**6]
    cl1 = plt.contour(cf, levels=levels1,
                  colors='k',
                  linewidths=(1,),
                  hold='on')    
    levels2 = [10,100]
    cl2 = plt.contour(cf, levels=levels2,
                  colors='k',
                  linewidths=(2,),
                  hold='on')
    levels3 = [20,50]
    cl3 = plt.contour(cf, levels=levels3,
                  colors='k',
                  linestyles='dashed',
                  linewidths=(1,),
                  hold='on')
    manual_locations2 = [(1000.0, 2500.0), (1000.0, 1000.0)]              
    manual_locations3 = [(1000.0, 2000.0), (1000.0, 1400.0)]
    plt.clabel(cl2, fmt='%2.1f', inline=1, colors='k', fontsize = font_size, manual=manual_locations2)
    plt.clabel(cl3, fmt='%2.1f', inline=1, colors='k', fontsize = font_size, manual=manual_locations3)
    
    cbar = fig.colorbar(cf, ticks=v, orientation='horizontal')
    cbar.ax.set_xlabel(r'$\sigma^{\mathrm{B}}_{\mathrm{MRSSM}}(uu \to \tilde{u}_L\tilde{u}_R)$ in fb', size = font_size)
    cbar.ax.tick_params(labelsize=font_size)
    cbar.add_lines(cl1)
    cbar.add_lines(cl2, erase=False)
    plt.show()
    
contourdata()
 
