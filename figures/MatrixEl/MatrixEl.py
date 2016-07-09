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
matrix_NLO_SE = np.array([], dtype=float);
matrix_NLO_Vertex = np.array([], dtype=float);
matrix_NLO_Boxes = np.array([], dtype=float);


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

f_SE = open('MatrixEl_SE_uu_susu.txt', 'r')
discard = f_SE.readline()
for lines in f_SE.readlines():
    discard = np.append(discard, float(lines.split()[0]))
    discard = np.append(discard, float(lines.split()[1]))
    discard = np.append(discard, float(lines.split()[2]))
    matrix_NLO_SE = np.append(matrix_NLO_SE, float(lines.split()[3]))
    discard = np.append(discard, float(lines.split()[4]))
    discard = np.append(discard, float(lines.split()[5]))    
f_SE.close()

f_Vertex = open('MatrixEl_Vertex_uu_susu.txt', 'r')
discard = f_Vertex.readline()
for lines in f_Vertex.readlines():
    discard = np.append(discard, float(lines.split()[0]))
    discard = np.append(discard, float(lines.split()[1]))
    discard = np.append(discard, float(lines.split()[2]))
    matrix_NLO_Vertex = np.append(matrix_NLO_Vertex, float(lines.split()[3]))
    discard = np.append(discard, float(lines.split()[4]))
    discard = np.append(discard, float(lines.split()[5]))    
f_Vertex.close()

f_Boxes = open('MatrixEl_Boxes_uu_susu.txt', 'r')
discard = f_Boxes.readline()
for lines in f_Boxes.readlines():
    discard = np.append(discard, float(lines.split()[0]))
    discard = np.append(discard, float(lines.split()[1]))
    discard = np.append(discard, float(lines.split()[2]))
    matrix_NLO_Boxes = np.append(matrix_NLO_Boxes, float(lines.split()[3]))
    discard = np.append(discard, float(lines.split()[4]))
    discard = np.append(discard, float(lines.split()[5]))    
f_Boxes.close()


fig = plt.figure(1,figsize=(14, 9))

first_window = plt.subplot(111)
plt.rcParams.update({'font.size': 22})
plt.xlabel(r"$t$ in $10^6$ GeV$^2$")#, size = 22)

# plot without poles
plt.ylabel("(Absolute) Squared Matrix Element")
plt.axis([min(t/10**6) - 1.1,max(t/10**6) + 1.1,0,1.4])
plt.plot(t/10**6, matrix_LO_Tree, lw=2, ls="-", c='black', label = r"$\frac{1}{4\cdot 9}\sum|\mathcal{M}^{\mathrm{B}}_{\mathrm{MRSSM}}|^2$ mit LO $\alpha_s$")
plt.plot(t/10**6, matrix_NLO_Tree, lw=2, ls="--", c='red', label = r"$\frac{1}{4\cdot 9}\sum|\mathcal{M}^{\mathrm{B}}_{\mathrm{MRSSM}}|^2$ mit NLO $\alpha_s$")
plt.plot(t/10**6, matrix_NLO_Tree+matrix_NLO_Virt, lw=2, ls="-", c='red', label = r"$\frac{1}{4\cdot 9}\sum|\mathcal{M}^{\mathrm{B}}_{\mathrm{MRSSM}}|^2 + \frac{1}{4\cdot 9}\sum 2 \Re \left( \mathcal{M}^{\mathrm{B}} \mathcal{M}^{\mathrm{1L}\ast} \right)$ mit NLO $\alpha_s$")
first_window.fill_between(t/10**6, matrix_NLO_Tree, matrix_NLO_Tree+matrix_NLO_Virt, 
facecolor=[1,90./100,90./100], color =[1,80./100,80./100], linestyle="-", label = r"$\frac{1}{4\cdot 9}\sum 2 \Re \left( \mathcal{M}^{\mathrm{B}} \mathcal{M}^{\mathrm{1L}\ast} \right)$ mit NLO $\alpha_s$")

# plot with poles
#plt.ylabel(r"$\frac{1}{4\cdot 9}\sum 2 \Re \left( \mathcal{M}^{\mathrm{B}} \mathcal{M}^{\mathrm{1L}\ast} \right)_{\mathrm{Virt}}(uu \to \tilde{u}_L\tilde{u}_R)$")
#plt.axis([min(t/10**6) - 1.1,max(t/10**6) + 1.1,-0.05,0.25])
#plt.plot(t/10**6, matrix_NLO_Virt, lw=2, ls="-", c='black', label = r"finite part of $\frac{1}{4\cdot 9}\sum 2 \Re \left( \mathcal{M}^{\mathrm{B}} \mathcal{M}^{\mathrm{1L}\ast} \right)_{\mathrm{Virt}}$")
#plt.plot(t/10**6, matrix_NLO_Single, lw=2, ls="-", c='red', label = r"single pole of $\frac{1}{4\cdot 9}\sum 2 \Re \left( \mathcal{M}^{\mathrm{B}} \mathcal{M}^{\mathrm{1L}\ast} \right)_{\mathrm{Virt}}$")
#plt.plot(t/10**6, matrix_NLO_Double, lw=2, ls="-", c='blue', label = r"double pole of $\frac{1}{4\cdot 9}\sum 2 \Re \left( \mathcal{M}^{\mathrm{B}} \mathcal{M}^{\mathrm{1L}\ast} \right)_{\mathrm{Virt}}$")

# different contributions to |M|^2
#plt.ylabel(r"$\frac{1}{4\cdot 9}\sum 2\Re \left( \mathcal{M}^{\mathrm{B}} \mathcal{M}^{\mathrm{1L}\ast} \right)(uu \to \tilde{u}_L\tilde{u}_R)$")
#plt.axis([min(t/10**6) - 1.1,max(t/10**6) + 1.1,-0.3,0.6])
#plt.plot(t/10**6, matrix_NLO_SE, lw=2, ls="--", c='green', label = r"$\frac{1}{4\cdot 9}\sum 2 \Re \left( \mathcal{M}^{\mathrm{B}} \mathcal{M}^{\mathrm{1L}\ast} \right)_{\mathrm{Self-Energy}}$")
#plt.plot(t/10**6, matrix_NLO_Vertex, lw=2, ls="--", c='red', label = r"$\frac{1}{4\cdot 9}\sum 2 \Re \left( \mathcal{M}^{\mathrm{B}} \mathcal{M}^{\mathrm{1L}\ast} \right)_{\mathrm{Vertices}}$")
#plt.plot(t/10**6, matrix_NLO_Boxes, lw=2, ls="--", c='blue', label = r"$\frac{1}{4\cdot 9}\sum 2 \Re \left( \mathcal{M}^{\mathrm{B}} \mathcal{M}^{\mathrm{1L}\ast} \right)_{\mathrm{Boxes}}$")
#plt.plot(t/10**6, matrix_NLO_Virt, lw=2, ls="-", c='black', label = r"$\frac{1}{4\cdot 9}\sum 2 \Re \left( \mathcal{M}^{\mathrm{B}} \mathcal{M}^{\mathrm{1L}\ast} \right)_{\mathrm{Virt}}$")
#plt.plot(t/10**6, matrix_NLO_SE + matrix_NLO_Vertex + matrix_NLO_Boxes, lw=2, ls="--", c='green', label = "summed")

plt.legend(loc=1,prop={'size':20})
first_window.axhline(y=0, color='k')
first_window.axvline(x=0, color='k')
plt.show()
plt.draw()
