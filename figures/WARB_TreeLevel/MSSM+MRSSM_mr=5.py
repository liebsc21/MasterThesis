# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:21:19 2015

@author: sebastian
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter


m_squark = np.array([], dtype=float);
# arrays for 1st parton reaction
sigma1_MSSM_dd = np.array([], dtype=float);
sigma1_MSSM_du = np.array([], dtype=float);
sigma1_MSSM_ds = np.array([], dtype=float);
sigma1_MSSM_dc = np.array([], dtype=float);
sigma1_MSSM_db = np.array([], dtype=float);

sigma1_MSSM_uu = np.array([], dtype=float);
sigma1_MSSM_us = np.array([], dtype=float);
sigma1_MSSM_uc = np.array([], dtype=float);
sigma1_MSSM_ub = np.array([], dtype=float);

sigma1_MSSM_ss = np.array([], dtype=float);
sigma1_MSSM_sc = np.array([], dtype=float);
sigma1_MSSM_sb = np.array([], dtype=float);

sigma1_MSSM_cc = np.array([], dtype=float);
sigma1_MSSM_cb = np.array([], dtype=float);

sigma1_MSSM_bb = np.array([], dtype=float);
# arrays for 2nd parton reaction
sigma2_MSSM = np.array([], dtype=float);
# arrays for 3rd parton reaction
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
# arrays for 4th parton reaction
sigma4_MSSM_dd = np.array([], dtype=float);
sigma4_MSSM_uu = np.array([], dtype=float);
sigma4_MSSM_ss = np.array([], dtype=float);
sigma4_MSSM_cc = np.array([], dtype=float);
sigma4_MSSM_bb = np.array([], dtype=float);
# arrays for 5th parton reaction
sigma5_MSSM = np.array([], dtype=float);
# arrays for 6th parton reaction
sigma6_MSSM_dg = np.array([], dtype=float);
sigma6_MSSM_ug = np.array([], dtype=float);
sigma6_MSSM_sg = np.array([], dtype=float);
sigma6_MSSM_cg = np.array([], dtype=float);
sigma6_MSSM_bg = np.array([], dtype=float);


# arrays for 1st parton reaction
sigma1_MRSSM_dd = np.array([], dtype=float);
sigma1_MRSSM_du = np.array([], dtype=float);
sigma1_MRSSM_ds = np.array([], dtype=float);
sigma1_MRSSM_dc = np.array([], dtype=float);
sigma1_MRSSM_db = np.array([], dtype=float);

sigma1_MRSSM_uu = np.array([], dtype=float);
sigma1_MRSSM_us = np.array([], dtype=float);
sigma1_MRSSM_uc = np.array([], dtype=float);
sigma1_MRSSM_ub = np.array([], dtype=float);

sigma1_MRSSM_ss = np.array([], dtype=float);
sigma1_MRSSM_sc = np.array([], dtype=float);
sigma1_MRSSM_sb = np.array([], dtype=float);

sigma1_MRSSM_cc = np.array([], dtype=float);
sigma1_MRSSM_cb = np.array([], dtype=float);

sigma1_MRSSM_bb = np.array([], dtype=float);
# arrays for 2nd parton reaction
sigma2_MRSSM = np.array([], dtype=float);
# arrays for 3rd parton reaction
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
# arrays for 4th parton reaction
sigma4_MRSSM_dd = np.array([], dtype=float);
sigma4_MRSSM_uu = np.array([], dtype=float);
sigma4_MRSSM_ss = np.array([], dtype=float);
sigma4_MRSSM_cc = np.array([], dtype=float);
sigma4_MRSSM_bb = np.array([], dtype=float);
# arrays for 5th parton reaction
sigma5_MRSSM = np.array([], dtype=float);
# arrays for 6th parton reaction
sigma6_MRSSM_dg = np.array([], dtype=float);
sigma6_MRSSM_ug = np.array([], dtype=float);
sigma6_MRSSM_sg = np.array([], dtype=float);
sigma6_MRSSM_cg = np.array([], dtype=float);
sigma6_MRSSM_bg = np.array([], dtype=float);



f_MSSM1 = open('1_q+q_bar->sq+sq_dagger/MSSM_q+q_bar->sq+sq_dagger_mr=5.txt', 'r')
discard = f_MSSM1.readline()

for lines in f_MSSM1.readlines():
    m_squark = np.append(m_squark, float(lines.split()[0]))
    sigma1_MSSM_dd = np.append(sigma1_MSSM_dd, float(lines.split()[1]))
    sigma1_MSSM_du = np.append(sigma1_MSSM_du, float(lines.split()[2]))
    sigma1_MSSM_ds = np.append(sigma1_MSSM_ds, float(lines.split()[3]))
    sigma1_MSSM_dc = np.append(sigma1_MSSM_dc, float(lines.split()[4]))
    sigma1_MSSM_db = np.append(sigma1_MSSM_db, float(lines.split()[5]))
        
    sigma1_MSSM_uu = np.append(sigma1_MSSM_uu, float(lines.split()[6]))
    sigma1_MSSM_us = np.append(sigma1_MSSM_us, float(lines.split()[7]))
    sigma1_MSSM_uc = np.append(sigma1_MSSM_uc, float(lines.split()[8]))
    sigma1_MSSM_ub = np.append(sigma1_MSSM_ub, float(lines.split()[9]))
    
    sigma1_MSSM_ss = np.append(sigma1_MSSM_ss, float(lines.split()[10]))
    sigma1_MSSM_sc = np.append(sigma1_MSSM_sc, float(lines.split()[11]))
    sigma1_MSSM_sb = np.append(sigma1_MSSM_sb, float(lines.split()[12]))
    
    sigma1_MSSM_cc = np.append(sigma1_MSSM_cc, float(lines.split()[13]))
    sigma1_MSSM_cb = np.append(sigma1_MSSM_cb, float(lines.split()[14]))
    
    sigma1_MSSM_bb = np.append(sigma1_MSSM_bb, float(lines.split()[15]))

sigma1_MSSM = sigma1_MSSM_dd+2*sigma1_MSSM_du+2*sigma1_MSSM_ds+2*sigma1_MSSM_dc+2*sigma1_MSSM_db+sigma1_MSSM_uu+2*sigma1_MSSM_us+2*sigma1_MSSM_uc+2*sigma1_MSSM_ub+sigma1_MSSM_ss+2*sigma1_MSSM_sc+2*sigma1_MSSM_sb+sigma1_MSSM_cc+2*sigma1_MSSM_cb+sigma1_MSSM_bb 

f_MSSM1.close()


f_MSSM2 = open('2_g+g->sq+sq_dagger/g+g->sq+sq_dagger.txt', 'r')
discard = f_MSSM2.readline()

for lines in f_MSSM2.readlines():
    discard = np.append(m_squark, float(lines.split()[0]))
    sigma2_MSSM = np.append(sigma2_MSSM, float(lines.split()[1]))
    
f_MSSM2.close()


f_MSSM3 = open('3_q+q->sq+sq/MSSM_q+q->sq+sq_mr=5.txt', 'r')
discard = f_MSSM3.readline()

for lines in f_MSSM3.readlines():
    discard = np.append(m_squark, float(lines.split()[0]))
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

sigma3_MSSM = sigma3_MSSM_dd+2*sigma3_MSSM_du+2*sigma3_MSSM_ds+2*sigma3_MSSM_dc+2*sigma3_MSSM_db+sigma3_MSSM_uu+2*sigma3_MSSM_us+2*sigma3_MSSM_uc+2*sigma3_MSSM_ub+sigma3_MSSM_ss+2*sigma3_MSSM_sc+2*sigma3_MSSM_sb+sigma3_MSSM_cc+2*sigma3_MSSM_cb+sigma3_MSSM_bb 

f_MSSM3.close()


f_MSSM4 = open('4_q+q_bar->sg+sg_bar/MSSM_q+q_bar->sg+sg_bar_mr=5.txt', 'r')
discard = f_MSSM4.readline()

for lines in f_MSSM4.readlines():
    discard = np.append(m_squark, float(lines.split()[0]))
    sigma4_MSSM_dd = np.append(sigma4_MSSM_dd, float(lines.split()[1]))
    sigma4_MSSM_uu = np.append(sigma4_MSSM_uu, float(lines.split()[2]))
    sigma4_MSSM_ss = np.append(sigma4_MSSM_ss, float(lines.split()[3]))
    sigma4_MSSM_cc = np.append(sigma4_MSSM_cc, float(lines.split()[4]))
    sigma4_MSSM_bb = np.append(sigma4_MSSM_bb, float(lines.split()[5]))

sigma4_MSSM = sigma4_MSSM_dd+sigma4_MSSM_uu+sigma4_MSSM_ss+sigma4_MSSM_cc+sigma4_MSSM_bb 

f_MSSM4.close()

f_MSSM5 = open('5_g+g->sg+sg/MSSM_g+g->sg+sg_bar_mr=5.txt', 'r')
discard = f_MSSM5.readline()

for lines in f_MSSM5.readlines():
    discard = np.append(m_squark, float(lines.split()[0]))
    sigma5_MSSM = np.append(sigma5_MSSM, float(lines.split()[1]))

f_MSSM5.close()


f_MSSM6 = open('6_q+g->sq+sg/q+g->sq+sg_mr=5.txt', 'r')
discard = f_MSSM6.readline()

for lines in f_MSSM6.readlines():
    discard = np.append(m_squark, float(lines.split()[0]))
    sigma6_MSSM_dg = np.append(sigma6_MSSM_dg, float(lines.split()[1]))
    sigma6_MSSM_ug = np.append(sigma6_MSSM_ug, float(lines.split()[2]))
    sigma6_MSSM_sg = np.append(sigma6_MSSM_sg, float(lines.split()[3]))
    sigma6_MSSM_cg = np.append(sigma6_MSSM_cg, float(lines.split()[4]))
    sigma6_MSSM_bg = np.append(sigma6_MSSM_bg, float(lines.split()[5]))

sigma6_MSSM = sigma6_MSSM_dg+sigma6_MSSM_ug+sigma6_MSSM_sg+sigma6_MSSM_cg+sigma6_MSSM_bg 

f_MSSM6.close()

sigma_MSSM = sigma1_MSSM+sigma2_MSSM+sigma3_MSSM+sigma4_MSSM+sigma5_MSSM+sigma6_MSSM

f_MRSSM1 = open('1_q+q_bar->sq+sq_dagger/MRSSM_q+q_bar->sq+sq_dagger_mr=5.txt', 'r')
discard = f_MRSSM1.readline()

for lines in f_MRSSM1.readlines():
    discard = np.append(m_squark, float(lines.split()[0]))
    sigma1_MRSSM_dd = np.append(sigma1_MRSSM_dd, float(lines.split()[1]))
    sigma1_MRSSM_du = np.append(sigma1_MRSSM_du, float(lines.split()[2]))
    sigma1_MRSSM_ds = np.append(sigma1_MRSSM_ds, float(lines.split()[3]))
    sigma1_MRSSM_dc = np.append(sigma1_MRSSM_dc, float(lines.split()[4]))
    sigma1_MRSSM_db = np.append(sigma1_MRSSM_db, float(lines.split()[5]))
        
    sigma1_MRSSM_uu = np.append(sigma1_MRSSM_uu, float(lines.split()[6]))
    sigma1_MRSSM_us = np.append(sigma1_MRSSM_us, float(lines.split()[7]))
    sigma1_MRSSM_uc = np.append(sigma1_MRSSM_uc, float(lines.split()[8]))
    sigma1_MRSSM_ub = np.append(sigma1_MRSSM_ub, float(lines.split()[9]))
    
    sigma1_MRSSM_ss = np.append(sigma1_MRSSM_ss, float(lines.split()[10]))
    sigma1_MRSSM_sc = np.append(sigma1_MRSSM_sc, float(lines.split()[11]))
    sigma1_MRSSM_sb = np.append(sigma1_MRSSM_sb, float(lines.split()[12]))
    
    sigma1_MRSSM_cc = np.append(sigma1_MRSSM_cc, float(lines.split()[13]))
    sigma1_MRSSM_cb = np.append(sigma1_MRSSM_cb, float(lines.split()[14]))
    
    sigma1_MRSSM_bb = np.append(sigma1_MRSSM_bb, float(lines.split()[15]))

sigma1_MRSSM = sigma1_MRSSM_dd+2*sigma1_MRSSM_du+2*sigma1_MRSSM_ds+2*sigma1_MRSSM_dc+2*sigma1_MRSSM_db+sigma1_MRSSM_uu+2*sigma1_MRSSM_us+2*sigma1_MRSSM_uc+2*sigma1_MRSSM_ub+sigma1_MRSSM_ss+2*sigma1_MRSSM_sc+2*sigma1_MRSSM_sb+sigma1_MRSSM_cc+2*sigma1_MRSSM_cb+sigma1_MRSSM_bb 

f_MRSSM1.close()


f_MRSSM2 = open('2_g+g->sq+sq_dagger/g+g->sq+sq_dagger.txt', 'r')
discard = f_MRSSM2.readline()

for lines in f_MRSSM2.readlines():
    discard = np.append(m_squark, float(lines.split()[0]))
    sigma2_MRSSM = np.append(sigma2_MRSSM, float(lines.split()[1]))
    
f_MRSSM2.close()


f_MRSSM3 = open('3_q+q->sq+sq/MRSSM_q+q->sq+sq_mr=5.txt', 'r')
discard = f_MRSSM3.readline()

for lines in f_MRSSM3.readlines():
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

sigma3_MRSSM = sigma3_MRSSM_dd+2*sigma3_MRSSM_du+2*sigma3_MRSSM_ds+2*sigma3_MRSSM_dc+2*sigma3_MRSSM_db+sigma3_MRSSM_uu+2*sigma3_MRSSM_us+2*sigma3_MRSSM_uc+2*sigma3_MRSSM_ub+sigma3_MRSSM_ss+2*sigma3_MRSSM_sc+2*sigma3_MRSSM_sb+sigma3_MRSSM_cc+2*sigma3_MRSSM_cb+sigma3_MRSSM_bb 

f_MRSSM3.close()


f_MRSSM4 = open('4_q+q_bar->sg+sg_bar/MRSSM_q+q_bar->sg+sg_bar_mr=5.txt', 'r')
discard = f_MRSSM4.readline()

for lines in f_MRSSM4.readlines():
    discard = np.append(m_squark, float(lines.split()[0]))
    sigma4_MRSSM_dd = np.append(sigma4_MRSSM_dd, float(lines.split()[1]))
    sigma4_MRSSM_uu = np.append(sigma4_MRSSM_uu, float(lines.split()[2]))
    sigma4_MRSSM_ss = np.append(sigma4_MRSSM_ss, float(lines.split()[3]))
    sigma4_MRSSM_cc = np.append(sigma4_MRSSM_cc, float(lines.split()[4]))
    sigma4_MRSSM_bb = np.append(sigma4_MRSSM_bb, float(lines.split()[5]))

sigma4_MRSSM = sigma4_MRSSM_dd+sigma4_MRSSM_uu+sigma4_MRSSM_ss+sigma4_MRSSM_cc+sigma4_MRSSM_bb 

f_MRSSM4.close()

f_MRSSM5 = open('5_g+g->sg+sg/MRSSM_g+g->sg+sg_bar_mr=5.txt', 'r')
discard = f_MRSSM5.readline()

for lines in f_MRSSM5.readlines():
    discard = np.append(m_squark, float(lines.split()[0]))
    sigma5_MRSSM = np.append(sigma5_MRSSM, float(lines.split()[1]))

f_MRSSM5.close()


f_MRSSM6 = open('6_q+g->sq+sg/q+g->sq+sg_mr=5.txt', 'r')
discard = f_MRSSM6.readline()

for lines in f_MRSSM6.readlines():
    discard = np.append(m_squark, float(lines.split()[0]))
    sigma6_MRSSM_dg = np.append(sigma6_MRSSM_dg, float(lines.split()[1]))
    sigma6_MRSSM_ug = np.append(sigma6_MRSSM_ug, float(lines.split()[2]))
    sigma6_MRSSM_sg = np.append(sigma6_MRSSM_sg, float(lines.split()[3]))
    sigma6_MRSSM_cg = np.append(sigma6_MRSSM_cg, float(lines.split()[4]))
    sigma6_MRSSM_bg = np.append(sigma6_MRSSM_bg, float(lines.split()[5]))

sigma6_MRSSM = sigma6_MRSSM_dg+sigma6_MRSSM_ug+sigma6_MRSSM_sg+sigma6_MRSSM_cg+sigma6_MRSSM_bg 

f_MRSSM6.close()

sigma_MRSSM = sigma1_MRSSM+sigma2_MRSSM+sigma3_MRSSM+sigma4_MRSSM+sigma5_MRSSM+sigma6_MRSSM


sigma_min = 10**(-2)
sigma_max = 10**(8)

fig = plt.figure(1,figsize=(17, 9))
#fig.suptitle(r'LO cross-sections for sparticle production at the LHC at $\sqrt{s}=13$TeV', fontsize=25)


first_window = plt.subplot(121)
#plt.title("MSSM", size = 22)
plt.xlabel(r"$m_{\tilde{q}}$ in GeV", size = 22)
plt.ylabel(r"$\sigma^{\mathrm{B}}_{\mathrm{MSSM}}$ in fb", size = 22)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)

# set scientific notation
plt.yscale('log')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.axis([min(m_squark),max(m_squark),sigma_min,sigma_max])
#plt.axis([min(m_squark),max(m_squark),0,1])
plt.axes(first_window)

first_window.xaxis.set_major_formatter(FormatStrFormatter('%0.0f'))

plt.plot(m_squark, sigma1_MSSM*10**3, lw=2, ls="--", c='orange', label = r"$q\overline{q} \to \tilde{q}\tilde{q}^\dagger$")
plt.plot(m_squark, sigma2_MSSM*10**3, lw=2, ls="--", c='red', label = r"$GG \to \tilde{q}\tilde{q}^\dagger$")
plt.plot(m_squark, sigma3_MSSM*10**3, lw=2, ls="-", c='green', label = r"$qq \to \tilde{q}\tilde{q}$")
plt.plot(m_squark, sigma4_MSSM*10**3, lw=2, ls=":", c='deepskyblue', label = r"$q\overline{q} \to \tilde{g}\tilde{g}$")
plt.plot(m_squark, sigma5_MSSM*10**3, lw=2, ls=":", c='darkblue', label = r"$GG \to \tilde{g}\tilde{g}$")
plt.plot(m_squark, sigma6_MSSM*10**3, lw=2, ls="-.", c='black', label = r"$qG \to \tilde{q}\tilde{g}$")


plt.legend(loc='best',prop={'size':21})

props = dict(boxstyle='round', facecolor='w', alpha=0.5)
first_window.text(600, 10**7, r"$\frac{m_{\tilde{g}}}{m_{\tilde{q}}} = 5$", fontsize=22,
        verticalalignment='top', bbox=props)



second_window = plt.subplot(122)
#plt.title(r"MRSSM", size = 22)
plt.xlabel(r"$m_{\tilde{q}}$ in GeV", size = 22)
plt.ylabel(r"$\sigma^{\mathrm{B}}_{\mathrm{MRSSM}}$ in fb", size = 22)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)

# set scientific notation
plt.yscale('log')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.axis([min(m_squark),max(m_squark),sigma_min,sigma_max])
#plt.axis([min(m_squark),max(m_squark),0,1])
plt.axes(second_window)

second_window.xaxis.set_major_formatter(FormatStrFormatter('%0.0f'))

plt.plot(m_squark, sigma1_MRSSM*10**3, lw=2, ls="--", c='orange', label = r"$q\overline{q} \to \tilde{q}\tilde{q}^\dagger$")
plt.plot(m_squark, sigma2_MRSSM*10**3, lw=2, ls="--", c='red', label = r"$GG \to \tilde{q}\tilde{q}^\dagger$")
plt.plot(m_squark, sigma3_MRSSM*10**3, lw=2, ls="-", c='green', label = r"$qq \to \tilde{q}\tilde{q}$")
plt.plot(m_squark, sigma4_MRSSM*10**3, lw=2, ls=":", c='deepskyblue', label = r"$q\overline{q} \to \tilde{g}\overline{\tilde{g}}$")
plt.plot(m_squark, sigma5_MRSSM*10**3, lw=2, ls=":", c='darkblue', label = r"$GG \to \tilde{g}\overline{\tilde{g}}$")
plt.plot(m_squark, sigma6_MRSSM*10**3, lw=2, ls="-.", c='black', label = r"$qG \to \tilde{q}\tilde{g}$")


plt.legend(loc='best',prop={'size':21})

props = dict(boxstyle='round', facecolor='w', alpha=0.5)
second_window.text(600, 10**7, r"$\frac{m_{\tilde{g}}}{m_{\tilde{q}}} = 5$", fontsize=22,
        verticalalignment='top', bbox=props)

plt.subplots_adjust(wspace = 0.3, top=0.85)

plt.show()
plt.draw()
