# -*- coding: utf-8 -*-
"""
C++ code on laptop in WARB-talk
@author: sebastian
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter


m_squark = np.array([], dtype=float);
sigma_dd = np.array([], dtype=float);
sigma_dd_C = np.array([], dtype=float); # charged conjugated cross section
sigma_du = np.array([], dtype=float);
sigma_du_C = np.array([], dtype=float);
sigma_ds = np.array([], dtype=float);
sigma_ds_C = np.array([], dtype=float);
sigma_dc = np.array([], dtype=float);
sigma_dc_C = np.array([], dtype=float);
sigma_db = np.array([], dtype=float);
sigma_db_C = np.array([], dtype=float);

sigma_uu = np.array([], dtype=float);
sigma_uu_C = np.array([], dtype=float);
sigma_us = np.array([], dtype=float);
sigma_us_C = np.array([], dtype=float);
sigma_uc = np.array([], dtype=float);
sigma_uc_C = np.array([], dtype=float);
sigma_ub = np.array([], dtype=float);
sigma_ub_C = np.array([], dtype=float);

sigma_ss = np.array([], dtype=float);
sigma_ss_C = np.array([], dtype=float);
sigma_sc = np.array([], dtype=float);
sigma_sc_C = np.array([], dtype=float);
sigma_sb = np.array([], dtype=float);
sigma_sb_C = np.array([], dtype=float);

sigma_cc = np.array([], dtype=float);
sigma_cc_C = np.array([], dtype=float);
sigma_cb = np.array([], dtype=float);
sigma_cb_C = np.array([], dtype=float);

sigma_bb = np.array([], dtype=float);
sigma_bb_C = np.array([], dtype=float);

f = open('had_cros_MRSSM_q+q->sq+sq_mr=2.txt', 'r')
discard = f.readline()

for lines in f.readlines():
    m_squark = np.append(m_squark, float(lines.split()[0]))
    sigma_dd = np.append(sigma_dd, float(lines.split()[1]))
    sigma_dd_C = np.append(sigma_dd_C, float(lines.split()[2]))
    sigma_du = np.append(sigma_du, float(lines.split()[3]))
    sigma_du_C = np.append(sigma_du_C, float(lines.split()[4]))
    sigma_ds = np.append(sigma_ds, float(lines.split()[5]))
    sigma_ds_C = np.append(sigma_ds_C, float(lines.split()[6]))
    sigma_dc = np.append(sigma_dc, float(lines.split()[7]))
    sigma_dc_C = np.append(sigma_dc_C, float(lines.split()[8]))
    sigma_db = np.append(sigma_db, float(lines.split()[9]))
    sigma_db_C = np.append(sigma_db_C, float(lines.split()[10]))
        
    sigma_uu = np.append(sigma_uu, float(lines.split()[11]))
    sigma_uu_C = np.append(sigma_uu_C, float(lines.split()[12]))
    sigma_us = np.append(sigma_us, float(lines.split()[13]))
    sigma_us_C = np.append(sigma_us_C, float(lines.split()[14]))
    sigma_uc = np.append(sigma_uc, float(lines.split()[15]))
    sigma_uc_C = np.append(sigma_uc_C, float(lines.split()[16]))
    sigma_ub = np.append(sigma_ub, float(lines.split()[17]))
    sigma_ub_C = np.append(sigma_ub_C, float(lines.split()[18]))
    
    sigma_ss = np.append(sigma_ss, float(lines.split()[19]))
    sigma_ss_C = np.append(sigma_ss_C, float(lines.split()[20]))
    sigma_sc = np.append(sigma_sc, float(lines.split()[21]))
    sigma_sc_C = np.append(sigma_sc_C, float(lines.split()[22]))
    sigma_sb = np.append(sigma_sb, float(lines.split()[23]))
    sigma_sb_C = np.append(sigma_sb_C, float(lines.split()[24]))

    sigma_cc = np.append(sigma_cc, float(lines.split()[25]))
    sigma_cc_C = np.append(sigma_cc_C, float(lines.split()[26]))
    sigma_cb = np.append(sigma_cb, float(lines.split()[27]))
    sigma_cb_C = np.append(sigma_cb_C, float(lines.split()[28]))
    
    sigma_bb = np.append(sigma_bb, float(lines.split()[29]))
    sigma_bb_C = np.append(sigma_bb_C, float(lines.split()[30]))

f.close()


sigma_min = 10**(-5.5)
sigma_max = 10**(5.5)

plt.figure(1,figsize=(15, 10))
first_window = plt.subplot(111)
#plt.title("LO-cross-section for squark production in the MRSSM at LHC with $\sqrt{s} = 13$TeV", fontsize=25)
plt.xlabel(r"$m_{\tilde{q}}$ in GeV", size = 22)
plt.ylabel(r"$\sigma_{MRSSM}(q_iq_j \to \tilde{q}_i\tilde{q}_j)$ in fb", size = 22)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)

# set scientific notation
plt.yscale('log')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.axis([min(m_squark),max(m_squark),sigma_min,sigma_max])
plt.axis([min(m_squark),max(m_squark),sigma_min,sigma_max])
plt.axes(first_window)

first_window.xaxis.set_major_formatter(FormatStrFormatter('%0.0f'))

plt.plot(m_squark, sigma_uu, lw=2, c='m', label = r"$\tilde{u}\tilde{u}$")
plt.plot(m_squark, sigma_du, lw=2, c='b', label = r"$\tilde{d}\tilde{u}$")
plt.plot(m_squark, sigma_dd, lw=2, c='r', label = r"$\tilde{d}\tilde{d}$")
plt.plot(m_squark, 0*m_squark, lw=2, c='w', ls = '--', label = " ")

plt.plot(m_squark, sigma_us, lw=2, c='y', ls = '--', label = r"$\tilde{u}\tilde{s}$")
plt.plot(m_squark, sigma_uc, lw=2, c='b', ls = '--', label = r"$\tilde{u}\tilde{c}$")
plt.plot(m_squark, sigma_ds, lw=2, c='g', ls = '--', label = r"$\tilde{d}\tilde{s}$")
plt.plot(m_squark, sigma_dc, lw=2, c='c', ls = '--', label = r"$\tilde{d}\tilde{c}$")

plt.plot(m_squark, sigma_ss, lw=2, c='r', ls = ':', label = r"$\tilde{s}\tilde{s}$")
plt.plot(m_squark, sigma_sc, lw=2, c='g', ls = ':', label = r"$\tilde{s}\tilde{c}$")
plt.plot(m_squark, sigma_cc, lw=2, c='c', ls = ':', label = r"$\tilde{c}\tilde{c}$")
plt.plot(m_squark, sigma_uu_C, lw=2, c='k', ls = '-.', label = r"$\bar{\tilde{u}}\bar{\tilde{u}}$")

#plt.legend(handles=[plotdu], loc=1)

plt.legend(loc='best',prop={'size':22},ncol=3)

props = dict(boxstyle='round', facecolor='w', alpha=0.5)
first_window.text(500, 50000, r"$\frac{m_{\tilde{g}}}{m_{\tilde{q}}} = 2$", 
                  fontsize=24, verticalalignment='top', bbox=props)


plt.show()
plt.draw()