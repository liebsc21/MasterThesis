# -*- coding: utf-8 -*-
"""
C++ code on laptop in WARB-talk
@author: sebastian
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter


m_squark = np.array([], dtype=float);
sigma_MSSM = np.array([], dtype=float);
sigma_MRSSM = np.array([], dtype=float);

# arrays for errors (all flavors are summed over already)
sigma3_MRSSM_maxPdf = np.array([], dtype=float);
sigma3_MRSSM_minPdf = np.array([], dtype=float);
sigma3_MRSSM_maxScale = np.array([], dtype=float);
sigma3_MRSSM_minScale = np.array([], dtype=float);

sigma3_MSSM_maxPdf = np.array([], dtype=float);
sigma3_MSSM_minPdf = np.array([], dtype=float);
sigma3_MSSM_maxScale = np.array([], dtype=float);
sigma3_MSSM_minScale = np.array([], dtype=float);


f_MSSM = open('MSSM_3_qq_sqsq_msg=2000GeV.txt', 'r')
#discard = f_MSSM.readline()

for lines in f_MSSM.readlines():
    m_squark = np.append(m_squark, float(lines.split()[0]))
    sigma_MSSM = np.append(sigma_MSSM, float(lines.split()[1]))

f_MSSM.close()


f_MRSSM = open('MRSSM_3_qq_sqLsqR_msg=2000GeV.txt', 'r')
#discard = f_MRSSM.readline()

for lines in f_MRSSM.readlines():
    discard = np.append(m_squark, float(lines.split()[0]))
    sigma_MRSSM = np.append(sigma_MRSSM, float(lines.split()[1]))

f_MRSSM.close()

f_MRSSM_maxPdf = open('Errors/qq_to_sqsq_MRSSM_maxPdfError_msg=2000GeV.txt', 'r')
for lines in f_MRSSM_maxPdf.readlines():
    sigma3_MRSSM_maxPdf = np.append(sigma3_MRSSM_maxPdf, float(lines))
f_MRSSM_maxPdf.close()

f_MRSSM_minPdf = open('Errors/qq_to_sqsq_MRSSM_minPdfError_msg=2000GeV.txt', 'r')
for lines in f_MRSSM_minPdf.readlines():
    sigma3_MRSSM_minPdf = np.append(sigma3_MRSSM_minPdf, float(lines))
f_MRSSM_minPdf.close()

f_MRSSM_maxScale = open('Errors/qq_to_sqsq_MRSSM_maxScaleError_msg=2000GeV.txt', 'r')
for lines in f_MRSSM_maxScale.readlines():
    sigma3_MRSSM_maxScale = np.append(sigma3_MRSSM_maxScale, float(lines))
f_MRSSM_maxScale.close()

f_MRSSM_minScale = open('Errors/qq_to_sqsq_MRSSM_minScaleError_msg=2000GeV.txt', 'r')
for lines in f_MRSSM_minScale.readlines():
    sigma3_MRSSM_minScale = np.append(sigma3_MRSSM_minScale, float(lines))
f_MRSSM_minScale.close()

sigma_MRSSM_min = np.sqrt((sigma_MRSSM - sigma3_MRSSM_minPdf)**2
 + (sigma_MRSSM - sigma3_MRSSM_minScale)**2)
sigma_MRSSM_max = np.sqrt((sigma_MRSSM - sigma3_MRSSM_maxPdf)**2
 + (sigma_MRSSM - sigma3_MRSSM_maxScale)**2)

f_MSSM_maxPdf = open('Errors/qq_to_sqsq_MSSM_maxPdfError_msg=2000GeV.txt', 'r')
for lines in f_MSSM_maxPdf.readlines():
    sigma3_MSSM_maxPdf = np.append(sigma3_MSSM_maxPdf, float(lines))
f_MSSM_maxPdf.close()

f_MSSM_minPdf = open('Errors/qq_to_sqsq_MSSM_minPdfError_msg=2000GeV.txt', 'r')
for lines in f_MSSM_minPdf.readlines():
    sigma3_MSSM_minPdf = np.append(sigma3_MSSM_minPdf, float(lines))
f_MSSM_minPdf.close()

f_MSSM_maxScale = open('Errors/qq_to_sqsq_MSSM_maxScaleError_msg=2000GeV.txt', 'r')
for lines in f_MSSM_maxScale.readlines():
    sigma3_MSSM_maxScale = np.append(sigma3_MSSM_maxScale, float(lines))
f_MSSM_maxScale.close()

f_MSSM_minScale = open('Errors/qq_to_sqsq_MSSM_minScaleError_msg=2000GeV.txt', 'r')
for lines in f_MSSM_minScale.readlines():
    sigma3_MSSM_minScale = np.append(sigma3_MSSM_minScale, float(lines))
f_MSSM_minScale.close()

sigma_MSSM_min = np.sqrt((sigma_MSSM - sigma3_MSSM_minPdf)**2
 + (sigma_MSSM - sigma3_MSSM_minScale)**2)
sigma_MSSM_max = np.sqrt((sigma_MSSM - sigma3_MSSM_maxPdf)**2
 + (sigma_MSSM - sigma3_MSSM_maxScale)**2)


sigma_min = 10**(-1)
sigma_max = 10**(5)

fig = plt.figure(1,figsize=(10, 9))
#fig.suptitle(r'cross-sections for squark production at the LHC at $\sqrt{s}=13$TeV', fontsize=20)


first_window = plt.subplot(111)
plt.xlabel(r"$m_{\tilde{q}}$ in GeV", size = 22)
plt.ylabel(r"$\sigma^{\mathrm{B}}(qq \to \tilde{q}\tilde{q})$ in fb", size = 22)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)

# set scientific notation
plt.yscale('log')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.axis([min(m_squark),max(m_squark),sigma_min,sigma_max])
plt.axes(first_window)

first_window.xaxis.set_major_formatter(FormatStrFormatter('%0.0f'))

first_window.fill_between(m_squark, sigma_MSSM - sigma_MSSM_min, sigma_MSSM + sigma_MSSM_max, facecolor=[80./100,80./100,1], color =[1,80./100,80./100], linestyle="-")
first_window.fill_between(m_squark, sigma_MRSSM - sigma_MRSSM_min, sigma_MRSSM + sigma_MRSSM_max, facecolor=[1,80./100,80./100], color =[1,80./100,80./100], linestyle="-")
plt.plot(m_squark, sigma_MSSM, lw=2, ls="-", c='blue', label = "MSSM")
plt.plot(m_squark, sigma_MRSSM, lw=2, ls="-", c='red', label = "MRSSM")


plt.legend(loc='best',prop={'size':22})

props = dict(boxstyle='round', facecolor='w', alpha=0.5)
first_window.text(300, 4, r"$m_{\tilde{g}} = 2000$ GeV", fontsize=22,
        verticalalignment='top', bbox=props)


plt.show()
plt.draw()
