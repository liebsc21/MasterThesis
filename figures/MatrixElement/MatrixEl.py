# -*- coding: utf-8 -*-
"""
C++ code on laptop in WARB-talk
@author: sebastian
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter


t = np.array([], dtype=float);
m_tree = np.array([], dtype=float);
m_virt = np.array([], dtype=float);

f_matrix = open('MatrixEl_Virt_uu_susu.txt', 'r')
discard = f_matrix.readline()

for lines in f_matrix.readlines():
    t = np.append(t, float(lines.split()[0]))
    m_tree = np.append(m_tree, float(lines.split()[1]))
    m_virt = np.append(m_virt, float(lines.split()[2]))
f_matrix.close()

fig = plt.figure(1,figsize=(10, 9))
first_window = plt.subplot(111)
#plt.xlabel(r"$m_{\tilde{q}}$ in GeV", size = 22)
#plt.ylabel(r"$\sigma^{\mathrm{B}}(qq \to \tilde{q}\tilde{q})$ in fb", size = 22)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
#plt.yscale('log')
#plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.axis([min(t),max(t),min(m_virt/m_tree),max(m_virt/m_tree)])
plt.axes(first_window)

#first_window.xaxis.set_major_formatter(FormatStrFormatter('%0.0f'))
plt.plot(t, m_virt/m_tree, lw=2, ls="-", c='blue')#, label = "MSSM")

#plt.legend(loc='best',prop={'size':22})

#props = dict(boxstyle='round', facecolor='w', alpha=0.5)
#first_window.text(300, 4, r"$m_{\tilde{g}} = 2000$ GeV", fontsize=22,
#        verticalalignment='top', bbox=props)


plt.show()
plt.draw()
