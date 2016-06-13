# -*- coding: utf-8 -*-
"""
C++ code on laptop in WARB-talk
@author: sebastian
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter


m_squark = np.array([], dtype=float);
# arrays for XSection
sigma_LO_Tree = np.array([], dtype=float);
sigma_NLO_Tree = np.array([], dtype=float);
sigma_NLO_Virt_withoutPrefactors = np.array([], dtype=float);
sigma_NLO_Virt = np.array([], dtype=float);
sigma_NLO_Real_withoutPrefactors = np.array([], dtype=float);
sigma_NLO_Real = np.array([], dtype=float);
sigma_NLO_1L   = np.array([], dtype=float);


f_Tree = open('MRSSM_Tree_uu_susu_msg=2000GeV.txt', 'r')

for lines in f_Tree.readlines():
    m_squark = np.append(m_squark, float(lines.split()[0]))
    sigma_LO_Tree = np.append(sigma_LO_Tree, float(lines.split()[1]))

f_Tree.close()


f_1L = open('MRSSM_1L_uu_susu_msg=2000GeV.txt', 'r')
discard = f_1L.readline()
for lines in f_1L.readlines():
    discard = np.append(m_squark, float(lines.split()[0]))
    sigma_NLO_Tree = np.append(sigma_NLO_Tree, float(lines.split()[1]))
    sigma_NLO_Virt_withoutPrefactors = np.append(sigma_NLO_Virt_withoutPrefactors, float(lines.split()[2]))
    sigma_NLO_Real_withoutPrefactors = np.append(sigma_NLO_Real_withoutPrefactors, float(lines.split()[3]))
    sigma_NLO_1L = np.append(sigma_NLO_1L, float(lines.split()[4]))    
f_1L.close()

f_Virt = open('MRSSM_Virt_uu_susu_msg=2000GeV.txt', 'r')
discard = f_Virt.readline()
for lines in f_Virt.readlines():
    discard = np.append(m_squark, float(lines.split()[0]))
    sigma_NLO_Virt = np.append(sigma_NLO_Virt, float(lines.split()[1]))
f_Virt.close()

sigma_NLO_Real = sigma_NLO_Real_withoutPrefactors + sigma_NLO_Virt_withoutPrefactors - sigma_NLO_Virt


K_min = 0
K_max = 2

fig = plt.figure(1,figsize=(10, 9))
#fig.suptitle(r'cross-sections for squark production at the LHC at $\sqrt{s}=13$TeV', fontsize=20)


first_window = plt.subplot(111)
plt.xlabel(r"$m_{\tilde{q}}$ in GeV", size = 22)
plt.ylabel(r"$K(uu \to \tilde{u}\tilde{u})$ ", size = 22)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)

# set scientific notation
#plt.yscale('log')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
#plt.axis([min(m_squark),max(m_squark),K_min,K_max])
plt.axis([200,max(m_squark),K_min,K_max])
plt.axes(first_window)

first_window.xaxis.set_major_formatter(FormatStrFormatter('%0.0f'))

first_window.fill_between(m_squark, m_squark*0, sigma_NLO_Tree/sigma_LO_Tree, 
facecolor=[1,70./100,70./100], color =[1,80./100,80./100], linestyle="-", label = "Born contribution")

first_window.fill_between(m_squark, sigma_NLO_Tree/sigma_LO_Tree, (sigma_NLO_Tree+sigma_NLO_Virt+sigma_NLO_Real)/sigma_LO_Tree, 
facecolor=[1,90./100,90./100], color =[1,80./100,80./100], linestyle="-", label = "Real and virtual corrections")

plt.plot(m_squark, sigma_NLO_1L/sigma_LO_Tree, lw=2, ls="-", c='red')#, label = "1L")
#plt.plot(m_squark, sigma_NLO_Tree/sigma_LO_Tree, lw=2, ls="--", c='blue')#, label = "1L")
#plt.plot(m_squark, sigma_NLO_Virt/sigma_LO_Tree, lw=2, ls="--", c='red')#, label = "1L")
#plt.plot(m_squark, sigma_NLO_Real/sigma_LO_Tree, lw=2, ls="--", c='green')#, label = "1L")

plt.legend(loc='best',prop={'size':22})

props = dict(boxstyle='round', facecolor='w', alpha=0.5)
first_window.text(1400, 0.5, r"$m_{\tilde{g}} = 2000$ GeV", fontsize=22,
        verticalalignment='top', bbox=props)



plt.show()
plt.draw()
