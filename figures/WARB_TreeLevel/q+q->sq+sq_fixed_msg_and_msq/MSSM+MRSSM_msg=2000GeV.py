# -*- coding: utf-8 -*-
"""
C++ code on laptop in WARB-talk
@author: sebastian
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter


m_squark = np.array([], dtype=float);
# arrays for MSSM
sigma3_MSSM_dd = np.array([], dtype=float);
sigma3_MSSM_du = np.array([], dtype=float);
sigma3_MSSM_ds = np.array([], dtype=float);
sigma3_MSSM_dc = np.array([], dtype=float);
sigma3_MSSM_db = np.array([], dtype=float);

sigma3_MSSM_uu = np.array([], dtype=float);
sigma3_MSSM_us = np.array([], dtype=float);
sigma3_MSSM_uc = np.array([], dtype=float);
sigma3_MSSM_ub = np.array([], dtype=float);

sigma3_MSSM_ss = np.array([], dtype=float);
sigma3_MSSM_sc = np.array([], dtype=float);
sigma3_MSSM_sb = np.array([], dtype=float);

sigma3_MSSM_cc = np.array([], dtype=float);
sigma3_MSSM_cb = np.array([], dtype=float);

sigma3_MSSM_bb = np.array([], dtype=float);

# arrays for MRSSM
sigma3_MRSSM_dd = np.array([], dtype=float);
sigma3_MRSSM_du = np.array([], dtype=float);
sigma3_MRSSM_ds = np.array([], dtype=float);
sigma3_MRSSM_dc = np.array([], dtype=float);
sigma3_MRSSM_db = np.array([], dtype=float);

sigma3_MRSSM_uu = np.array([], dtype=float);
sigma3_MRSSM_us = np.array([], dtype=float);
sigma3_MRSSM_uc = np.array([], dtype=float);
sigma3_MRSSM_ub = np.array([], dtype=float);

sigma3_MRSSM_ss = np.array([], dtype=float);
sigma3_MRSSM_sc = np.array([], dtype=float);
sigma3_MRSSM_sb = np.array([], dtype=float);

sigma3_MRSSM_cc = np.array([], dtype=float);
sigma3_MRSSM_cb = np.array([], dtype=float);

sigma3_MRSSM_bb = np.array([], dtype=float);

# arrays for errors (all flavors are already summed over)
sigma3_MRSSM_maxPdf = np.array([], dtype=float);
sigma3_MRSSM_minPdf = np.array([], dtype=float);
sigma3_MRSSM_maxScale = np.array([], dtype=float);
sigma3_MRSSM_minScale = np.array([], dtype=float);


f_MSSM = open('had_cros_MSSM_q+q->sq+sq_msg=2000GeV.txt', 'r')
discard = f_MSSM.readline()

for lines in f_MSSM.readlines():
    m_squark = np.append(m_squark, float(lines.split()[0]))
    sigma3_MSSM_dd = np.append(sigma3_MSSM_dd, float(lines.split()[1]))
    sigma3_MSSM_du = np.append(sigma3_MSSM_du, float(lines.split()[2]))
    sigma3_MSSM_ds = np.append(sigma3_MSSM_ds, float(lines.split()[3]))
    sigma3_MSSM_dc = np.append(sigma3_MSSM_dc, float(lines.split()[4]))
    sigma3_MSSM_db = np.append(sigma3_MSSM_db, float(lines.split()[5]))
        
    sigma3_MSSM_uu = np.append(sigma3_MSSM_uu, float(lines.split()[6]))
    sigma3_MSSM_us = np.append(sigma3_MSSM_us, float(lines.split()[7]))
    sigma3_MSSM_uc = np.append(sigma3_MSSM_uc, float(lines.split()[8]))
    sigma3_MSSM_ub = np.append(sigma3_MSSM_ub, float(lines.split()[9]))
    
    sigma3_MSSM_ss = np.append(sigma3_MSSM_ss, float(lines.split()[10]))
    sigma3_MSSM_sc = np.append(sigma3_MSSM_sc, float(lines.split()[11]))
    sigma3_MSSM_sb = np.append(sigma3_MSSM_sb, float(lines.split()[12]))
    
    sigma3_MSSM_cc = np.append(sigma3_MSSM_cc, float(lines.split()[13]))
    sigma3_MSSM_cb = np.append(sigma3_MSSM_cb, float(lines.split()[14]))
    
    sigma3_MSSM_bb = np.append(sigma3_MSSM_bb, float(lines.split()[15]))

sigma_MSSM = sigma3_MSSM_dd+sigma3_MSSM_du+sigma3_MSSM_ds+sigma3_MSSM_dc+sigma3_MSSM_db+sigma3_MSSM_uu+sigma3_MSSM_us+sigma3_MSSM_uc+sigma3_MSSM_ub+sigma3_MSSM_ss+sigma3_MSSM_sc+sigma3_MSSM_sb+sigma3_MSSM_cc+sigma3_MSSM_cb+sigma3_MSSM_bb 

f_MSSM.close()


f_MRSSM = open('had_cros_MRSSM_q+q->sq+sq_msg=2000GeV.txt', 'r')
discard = f_MRSSM.readline()

for lines in f_MRSSM.readlines():
    discard = np.append(m_squark, float(lines.split()[0]))
    sigma3_MRSSM_dd = np.append(sigma3_MRSSM_dd, float(lines.split()[1]))
    sigma3_MRSSM_du = np.append(sigma3_MRSSM_du, float(lines.split()[2]))
    sigma3_MRSSM_ds = np.append(sigma3_MRSSM_ds, float(lines.split()[3]))
    sigma3_MRSSM_dc = np.append(sigma3_MRSSM_dc, float(lines.split()[4]))
    sigma3_MRSSM_db = np.append(sigma3_MRSSM_db, float(lines.split()[5]))
        
    sigma3_MRSSM_uu = np.append(sigma3_MRSSM_uu, float(lines.split()[6]))
    sigma3_MRSSM_us = np.append(sigma3_MRSSM_us, float(lines.split()[7]))
    sigma3_MRSSM_uc = np.append(sigma3_MRSSM_uc, float(lines.split()[8]))
    sigma3_MRSSM_ub = np.append(sigma3_MRSSM_ub, float(lines.split()[9]))
    
    sigma3_MRSSM_ss = np.append(sigma3_MRSSM_ss, float(lines.split()[10]))
    sigma3_MRSSM_sc = np.append(sigma3_MRSSM_sc, float(lines.split()[11]))
    sigma3_MRSSM_sb = np.append(sigma3_MRSSM_sb, float(lines.split()[12]))
    
    sigma3_MRSSM_cc = np.append(sigma3_MRSSM_cc, float(lines.split()[13]))
    sigma3_MRSSM_cb = np.append(sigma3_MRSSM_cb, float(lines.split()[14]))
    
    sigma3_MRSSM_bb = np.append(sigma3_MRSSM_bb, float(lines.split()[15]))

sigma_MRSSM = sigma3_MRSSM_dd+sigma3_MRSSM_du+sigma3_MRSSM_ds+sigma3_MRSSM_dc+sigma3_MRSSM_db+sigma3_MRSSM_uu+sigma3_MRSSM_us+sigma3_MRSSM_uc+sigma3_MRSSM_ub+sigma3_MRSSM_ss+sigma3_MRSSM_sc+sigma3_MRSSM_sb+sigma3_MRSSM_cc+sigma3_MRSSM_cb+sigma3_MRSSM_bb 

f_MRSSM.close()

f_MRSSM_maxPdf = open('Errors/qq_to_sqsq_MRSSM_with_antiquarks_maxPdfError_msg=2000GeV.txt', 'r')
for lines in f_MRSSM_maxPdf.readlines():
    sigma3_MRSSM_maxPdf = np.append(sigma3_MRSSM_maxPdf, float(lines))
f_MRSSM_maxPdf.close()

f_MRSSM_minPdf = open('Errors/qq_to_sqsq_MRSSM_with_antiquarks_minPdfError_msg=2000GeV.txt', 'r')
for lines in f_MRSSM_minPdf.readlines():
    sigma3_MRSSM_minPdf = np.append(sigma3_MRSSM_minPdf, float(lines))
f_MRSSM_minPdf.close()

f_MRSSM_maxScale = open('Errors/qq_to_sqsq_MRSSM_with_antiquarks_maxScaleError_msg=2000GeV.txt', 'r')
for lines in f_MRSSM_maxScale.readlines():
    sigma3_MRSSM_maxScale = np.append(sigma3_MRSSM_maxScale, float(lines))
f_MRSSM_maxScale.close()

f_MRSSM_minScale = open('Errors/qq_to_sqsq_MRSSM_with_antiquarks_minScaleError_msg=2000GeV.txt', 'r')
for lines in f_MRSSM_minScale.readlines():
    sigma3_MRSSM_minScale = np.append(sigma3_MRSSM_minScale, float(lines))
f_MRSSM_minScale.close()

sigma_MRSSM_min = np.sqrt((sigma_MRSSM*10**3 - sigma3_MRSSM_minPdf)**2
 + (sigma_MRSSM*10**3 - sigma3_MRSSM_minScale)**2)
sigma_MRSSM_max = np.sqrt((sigma_MRSSM*10**3 - sigma3_MRSSM_maxPdf)**2
 + (sigma_MRSSM*10**3 - sigma3_MRSSM_maxScale)**2)


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

first_window.fill_between(m_squark, sigma_MRSSM*10**3 - sigma_MRSSM_min, sigma_MRSSM*10**3 + sigma_MRSSM_max, facecolor=[1,80./100,80./100], color =[1,80./100,80./100], linestyle="-")
plt.plot(m_squark, sigma_MSSM*10**3, lw=2, ls="-", c='blue', label = "MSSM")
plt.plot(m_squark, sigma_MRSSM*10**3, lw=2, ls="-", c='red', label = "MRSSM")

plt.legend(loc='best',prop={'size':22})

props = dict(boxstyle='round', facecolor='w', alpha=0.5)
first_window.text(300, 4, r"$m_{\tilde{g}} = 2000$ GeV", fontsize=22,
        verticalalignment='top', bbox=props)


plt.show()
plt.draw()
