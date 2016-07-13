# -*- coding: utf-8 -*-
"""
C++ code on laptop in WARB-talk
@author: sebastian
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter


m_sgluon = np.array([], dtype=float);
# arrays for XSection
sigma_LO_Tree = np.array([], dtype=float);
sigma_NLO_Tree = np.array([], dtype=float);
sigma_NLO_Virt_withoutPrefactors = np.array([], dtype=float);
sigma_NLO_Real_withoutPrefactors = np.array([], dtype=float);
sigma_NLO_1L   = np.array([], dtype=float);


f_1L = open('MRSSM_1L_uu_susu_msq=1000GeV_msg=2000GeV.txt', 'r')
discard = f_1L.readline()
for lines in f_1L.readlines():
    m_sgluon = np.append(m_sgluon, float(lines.split()[0]))
    sigma_NLO_Tree = np.append(sigma_NLO_Tree, float(lines.split()[1]))
    sigma_NLO_1L = np.append(sigma_NLO_1L, float(lines.split()[2]))    
f_1L.close()

sigma_LO_Tree = m_sgluon * 0 + 11.48

K_min = 0
K_max = max(sigma_NLO_1L/sigma_LO_Tree) + 0.1

fig = plt.figure(1,figsize=(10, 9))
#fig.suptitle(r'cross-sections for squark production at the LHC at $\sqrt{s}=13$TeV', fontsize=20)


first_window = plt.subplot(111)
plt.xlabel(r"$m_{\tilde{\sigma}}$ in GeV", size = 22)
plt.ylabel(r"$K_{\mathrm{MRSSM}}(pp \to \tilde{u}_L\tilde{u}_R)$ ", size = 22)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)

# set scientific notation
plt.xscale('log')
#plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.axis([min(m_sgluon),max(m_sgluon),K_min,K_max])
plt.axes(first_window)

first_window.fill_between(m_sgluon, m_sgluon*0, sigma_NLO_Tree/sigma_LO_Tree, 
facecolor=[1,70./100,70./100], color =[1,80./100,80./100], linestyle="-", label = "Born contribution")

first_window.fill_between(m_sgluon, sigma_NLO_Tree/sigma_LO_Tree, sigma_NLO_1L/sigma_LO_Tree, 
facecolor=[1,90./100,90./100], color =[1,80./100,80./100], linestyle="-", label = "Real and virtual corrections")

plt.plot(m_sgluon, sigma_NLO_1L/sigma_LO_Tree, lw=2, ls="-", c='red', label = "total $K$-factor")

plt.legend(loc=4,prop={'size':22})

props = dict(boxstyle='round', facecolor='w', alpha=0.5)
first_window.text(10000, 0.8, r"$m_{\tilde{g}} = 2000$ GeV, $m_{\tilde{q}} = 1000$ GeV", fontsize=22,
        verticalalignment='top', bbox=props)



plt.show()
plt.draw()
