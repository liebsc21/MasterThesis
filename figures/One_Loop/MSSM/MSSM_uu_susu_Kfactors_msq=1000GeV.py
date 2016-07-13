# -*- coding: utf-8 -*-
"""
C++ code on laptop in WARB-talk
@author: sebastian
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter


m_gluino = np.array([], dtype=float);
# arrays for XSection
sigma_LO_Tree_lr = np.array([], dtype=float);
sigma_NLO_Tree_lr = np.array([], dtype=float);
sigma_NLO_1L_lr   = np.array([], dtype=float);
sigma_LO_Tree_ll = np.array([], dtype=float);
sigma_NLO_Tree_ll = np.array([], dtype=float);
sigma_NLO_1L_ll   = np.array([], dtype=float);


f_Tree = open('data/MSSM_ulur_LO_tree_msq=1000GeV.txt', 'r')
for lines in f_Tree.readlines():
    m_gluino = np.append(m_gluino, float(lines.split()[0]))
    sigma_LO_Tree_lr = np.append(sigma_LO_Tree_lr, float(lines.split()[1]))
f_Tree.close()

f_Tree = open('data/MSSM_ulul_LO_tree_msq=1000GeV.txt', 'r')
for lines in f_Tree.readlines():
    discard = np.append(m_gluino, float(lines.split()[0]))
    sigma_LO_Tree_ll = np.append(sigma_LO_Tree_ll, float(lines.split()[1]))
f_Tree.close()

f_Tree = open('data/MSSM_ulur_NLO_tree_msq=1000GeV.txt', 'r')
for lines in f_Tree.readlines():
    discard = np.append(m_gluino, float(lines.split()[0]))
    sigma_NLO_Tree_lr = np.append(sigma_NLO_Tree_lr, float(lines.split()[1]))
f_Tree.close()

f_Tree = open('data/MSSM_ulul_NLO_tree_msq=1000GeV.txt', 'r')
for lines in f_Tree.readlines():
    discard = np.append(m_gluino, float(lines.split()[0]))
    sigma_NLO_Tree_ll = np.append(sigma_NLO_Tree_ll, float(lines.split()[1]))
f_Tree.close()


f_1L = open('data/MSSM_1L_ulur_msq=1000GeV.txt', 'r')
for lines in f_1L.readlines():
    discard = np.append(m_gluino, float(lines.split()[0]))
    sigma_NLO_1L_lr = np.append(sigma_NLO_1L_lr, float(lines.split()[1]))    
f_1L.close()
f_1L = open('data/MSSM_1L_ulul_msq=1000GeV.txt', 'r')
for lines in f_1L.readlines():
    discard = np.append(m_gluino, float(lines.split()[0]))
    sigma_NLO_1L_ll = np.append(sigma_NLO_1L_ll, float(lines.split()[1]))    
f_1L.close()

K_min = 0
K_max = 2

fig = plt.figure(1,figsize=(12,8))
font_size = 18
#fig.suptitle(r'cross-sections for squark production at the LHC at $\sqrt{s}=13$TeV', fontsize=20)

############# first subplot #####################
first_window = plt.subplot2grid((2,2), (0,0))
plt.xlabel(r"$m_{\tilde{g}}$ in GeV", size = font_size)
plt.ylabel(r"$K_{\mathrm{MSSM}}(pp \to \tilde{u}_L\tilde{u}_R)$ ", size = font_size)
plt.xticks(fontsize = font_size)
plt.yticks(fontsize = font_size)

# set scientific notation
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.axis([150,max(m_gluino),K_min,K_max])
plt.axes(first_window)

first_window.xaxis.set_major_formatter(FormatStrFormatter('%0.0f'))

first_window.fill_between(m_gluino, m_gluino*0, sigma_NLO_Tree_lr/sigma_LO_Tree_lr, 
facecolor=[70./100,70./100,1], color =[80./100,80./100,1], linestyle="-", label = "Born contribution")

first_window.fill_between(m_gluino, sigma_NLO_Tree_lr/sigma_LO_Tree_lr, sigma_NLO_1L_lr/sigma_LO_Tree_lr, 
facecolor=[90./100,90./100,1], color =[80./100,80./100,1], linestyle="-", label = "Real and virtual corrections")

plt.plot(m_gluino, sigma_NLO_1L_lr/sigma_LO_Tree_lr, lw=2, ls="-", c='blue')#, label = "1L")

############# second subplot #####################
second_window = plt.subplot2grid((2,2), (0,1))
plt.xlabel(r"$m_{\tilde{g}}$ in GeV", size = font_size)
plt.ylabel(r"$K_{\mathrm{MSSM}}(pp \to \tilde{u}_L\tilde{u}_L)$ ", size = font_size)
plt.xticks(fontsize = font_size)
plt.yticks(fontsize = font_size)

# set scientific notation
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.axis([150,max(m_gluino),K_min,K_max])
plt.axes(second_window)

second_window.xaxis.set_major_formatter(FormatStrFormatter('%0.0f'))

second_window.fill_between(m_gluino, m_gluino*0, sigma_NLO_Tree_ll/sigma_LO_Tree_ll, 
facecolor=[70./100,70./100,1], color =[80./100,80./100,1], linestyle="-", label = "Born contribution")

second_window.fill_between(m_gluino, sigma_NLO_Tree_ll/sigma_LO_Tree_ll, sigma_NLO_1L_ll/sigma_LO_Tree_ll, 
facecolor=[90./100,90./100,1], color =[80./100,80./100,1], linestyle="-", label = "Real and virtual corrections")

plt.plot(m_gluino, sigma_NLO_1L_ll/sigma_LO_Tree_ll, lw=2, ls="-", c='blue')#, label = "1L")

       
############# third subplot #####################
third_window = plt.subplot2grid((2,2), (1,0), colspan = 2)
plt.xlabel(r"$m_{\tilde{g}}$ in GeV", size = font_size)
plt.ylabel(r"$K_{\mathrm{MSSM}}(pp \to \tilde{u}\tilde{u})$ ", size = font_size)
plt.xticks(fontsize = font_size)
plt.yticks(fontsize = font_size)

# set scientific notation
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.axis([150,max(m_gluino),K_min,K_max])
plt.axes(third_window)

third_window.xaxis.set_major_formatter(FormatStrFormatter('%0.0f'))

third_window.fill_between(m_gluino, m_gluino*0, (sigma_NLO_Tree_lr + 2*sigma_NLO_Tree_ll)/(sigma_LO_Tree_lr + 2*sigma_LO_Tree_ll), 
facecolor=[70./100,70./100,1], color =[80./100,80./100,1], linestyle="-", label = "Born contribution")

third_window.fill_between(m_gluino, (sigma_NLO_Tree_lr + 2*sigma_NLO_Tree_ll)/(sigma_LO_Tree_lr + 2*sigma_LO_Tree_ll), (sigma_NLO_1L_lr + 2*sigma_NLO_1L_ll)/(sigma_LO_Tree_lr + 2*sigma_LO_Tree_ll), 
facecolor=[90./100,90./100,1], color =[80./100,80./100,1], linestyle="-", label = "Real and virtual corrections")

plt.plot(m_gluino, (sigma_NLO_1L_lr + 2*sigma_NLO_1L_ll)/(sigma_LO_Tree_lr + 2*sigma_LO_Tree_ll), lw=2, ls="-", c='blue')#, label = "1L")

plt.legend(loc='best',prop={'size':font_size})

props = dict(boxstyle='round', facecolor='w', alpha=0.5)
third_window.text(1400, 0.5, r"$m_{\tilde{q}} = 1000$ GeV", fontsize=font_size,
        verticalalignment='top', bbox=props)        



plt.show()
plt.draw()
