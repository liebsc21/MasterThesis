# -*- coding: utf-8 -*-
"""
C++ code on laptop in WARB-talk
@author: sebastian
"""

import numpy as np
from matplotlib import pyplot as plt
#from matplotlib.ticker import ScalarFormatter, FormatStrFormatter


t = np.array([], dtype=float);
matrix_LO_Tree = np.array([], dtype=float);
matrix_NLO_Tree = np.array([], dtype=float);
matrix_NLO_Virt = np.array([], dtype=float);
matrix_NLO_Single = np.array([], dtype=float);
matrix_NLO_Double   = np.array([], dtype=float);


f_matrix = open('MatrixEl_Virt_uu_susu.txt', 'r')
discard = f_matrix.readline()
for lines in f_matrix.readlines():
    t = np.append(t, float(lines.split()[0]))
    matrix_LO_Tree = np.append(matrix_LO_Tree, float(lines.split()[1]))
    matrix_NLO_Tree = np.append(matrix_NLO_Tree, float(lines.split()[2]))
    matrix_NLO_Virt = np.append(matrix_NLO_Virt, float(lines.split()[3]))
    matrix_NLO_Single = np.append(matrix_NLO_Single, float(lines.split()[4]))
    matrix_NLO_Double = np.append(matrix_NLO_Double, float(lines.split()[5]))    
f_matrix.close()


fig = plt.figure(1,figsize=(12, 9))

first_window = plt.subplot(111)
plt.rcParams.update({'font.size': 22})
plt.xlabel(r"$t$ in $10^6$ GeV$^2$")#, size = 22)

# plot without poles
plt.ylabel(r"$|\mathcal{M}_{\mathrm{MRSSM}}(uu \to \tilde{u}_L\tilde{u}_R)|^2$")
plt.axis([min(t/10**6) - 1.1,max(t/10**6) + 1.1,0,0.8])
plt.plot(t/10**6, matrix_LO_Tree, lw=2, ls="-", c='black', label = r"$|\mathcal{M}^{\mathrm{B}}_{\mathrm{MRSSM}}|^2$ mit LO $\alpha_s$")
plt.plot(t/10**6, matrix_NLO_Tree, lw=2, ls="--", c='red', label = r"$|\mathcal{M}^{\mathrm{B}}_{\mathrm{MRSSM}}|^2$ mit NLO $\alpha_s$")
plt.plot(t/10**6, matrix_NLO_Tree+matrix_NLO_Virt, lw=2, ls="-", c='red', label = r"$|\mathcal{M}^{\mathrm{B}}_{\mathrm{MRSSM}}|^2 + |\mathcal{M}^{\mathrm{V}}_{\mathrm{MRSSM}}|^2$ mit NLO $\alpha_s$")
first_window.fill_between(t/10**6, matrix_NLO_Tree, matrix_NLO_Tree+matrix_NLO_Virt, 
facecolor=[1,90./100,90./100], color =[1,80./100,80./100], linestyle="-", label = r"$|\mathcal{M}^{\mathrm{V}}_{\mathrm{MRSSM}}|^2$ mit NLO $\alpha_s$")
plt.legend(loc=(0.2,0.1),prop={'size':20})

# plot with poles
#plt.ylabel(r"$|\mathcal{M}^{\mathrm{V}}_{\mathrm{MRSSM}}(uu \to \tilde{u}_L\tilde{u}_R)|^2$")
#plt.axis([min(t/10**6) - 1.1,max(t/10**6) + 1.1,-0.05,0.15])
#plt.plot(t/10**6, matrix_NLO_Virt, lw=2, ls="-", c='black', label = r"finite part of $|\mathcal{M}^{\mathrm{V}}_{\mathrm{MRSSM}}|^2$")
#plt.plot(t/10**6, matrix_NLO_Single, lw=2, ls="-", c='red', label = r"single pole of $|\mathcal{M}^{\mathrm{V}}_{\mathrm{MRSSM}}|^2$")
#plt.plot(t/10**6, matrix_NLO_Double, lw=2, ls="-", c='blue', label = r"double pole of $|\mathcal{M}^{\mathrm{V}}_{\mathrm{MRSSM}}|^2$")
#plt.legend(loc=(0.25,0.2),prop={'size':20})

plt.show()
plt.draw()
