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
sigma1_MSSM = np.array([], dtype=float);
# arrays for 2nd parton reaction
sigma2 = np.array([], dtype=float);
# arrays for 3rd parton reaction
sigma3_MSSM = np.array([], dtype=float);
# arrays for 4th parton reaction
sigma4_MSSM = np.array([], dtype=float);
# arrays for 5th parton reaction
sigma5_MSSM = np.array([], dtype=float);
# arrays for 6th parton reaction
sigma6 = np.array([], dtype=float);


# arrays for 1st parton reaction
sigma1_MRSSM = np.array([], dtype=float);
# arrays for 3rd parton reaction
sigma3_MRSSM = np.array([], dtype=float);
# arrays for 4th parton reaction
sigma4_MRSSM = np.array([], dtype=float);
# arrays for 5th parton reaction
sigma5_MRSSM = np.array([], dtype=float);



f_MSSM1 = open('MSSM_1_qqbar_sqsqdagger.txt', 'r')

for lines in f_MSSM1.readlines():
    m_squark = np.append(m_squark, float(lines.split()[0]))
    sigma1_MSSM = np.append(sigma1_MSSM, float(lines.split()[1]))

f_MSSM1.close()


f_2 = open('MSSM_MRSSM_2_GG_sqsq.txt', 'r')

for lines in f_2.readlines():
    discard = f_2.readline()
    sigma2 = np.append(sigma2, float(lines.split()[1]))

f_2.close()


f_MSSM3 = open('MSSM_3_qq_sqsq.txt', 'r')

for lines in f_MSSM3.readlines():
    discard = f_MSSM3.readline()
    sigma3_MSSM = np.append(sigma3_MSSM, float(lines.split()[1]))

f_MSSM3.close()


f_MSSM4 = open('MSSM_4_qqbar_gg.txt', 'r')

for lines in f_MSSM4.readlines():
    discard = np.append(m_squark, float(lines.split()[0]))
    sigma4_MSSM = np.append(sigma4_MSSM, float(lines.split()[1]))

f_MSSM4.close()

f_MSSM5 = open('MSSM_5_GG_gg.txt', 'r')

for lines in f_MSSM5.readlines():
    discard = np.append(m_squark, float(lines.split()[0]))
    sigma5_MSSM = np.append(sigma5_MSSM, float(lines.split()[1]))

f_MSSM5.close()


f_6 = open('MSSM_MRSSM_6_qG_sqg.txt', 'r')

for lines in f_6.readlines():
    discard = np.append(m_squark, float(lines.split()[0]))
    sigma6 = np.append(sigma6, float(lines.split()[1]))

f_6.close()


f_MRSSM1 = open('MRSSM_1_qqbar_sqsqdagger.txt', 'r')

for lines in f_MRSSM1.readlines():
    discard = np.append(m_squark, float(lines.split()[0]))
    sigma1_MRSSM = np.append(sigma1_MRSSM, float(lines.split()[1]))

f_MRSSM1.close()


f_MRSSM3 = open('MRSSM_3_qq_sqLsqR.txt', 'r')

for lines in f_MRSSM3.readlines():
    discard = f_MRSSM3.readline()
    sigma3_MRSSM = np.append(sigma3_MRSSM, float(lines.split()[1]))

f_MRSSM3.close()


f_MRSSM4 = open('MRSSM_4_qqbar_ggbar.txt', 'r')

for lines in f_MRSSM4.readlines():
    discard = np.append(m_squark, float(lines.split()[0]))
    sigma4_MRSSM = np.append(sigma4_MRSSM, float(lines.split()[1]))

f_MRSSM4.close()

f_MRSSM5 = open('MRSSM_5_GG_ggbar.txt', 'r')

for lines in f_MRSSM5.readlines():
    discard = np.append(m_squark, float(lines.split()[0]))
    sigma5_MRSSM = np.append(sigma5_MRSSM, float(lines.split()[1]))

f_MRSSM5.close()


sigma_min = 10**(-2)
sigma_max = 10**(7)

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
#plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.axis([min(m_squark),max(m_squark),sigma_min,sigma_max])
#plt.axis([min(m_squark),max(m_squark),0,1])
plt.axes(first_window)

first_window.xaxis.set_major_formatter(FormatStrFormatter('%0.0f'))

plt.plot(m_squark, sigma1_MSSM, lw=2, ls="--", c='orange', label = r"$q\overline{q} \to \tilde{q}\tilde{q}^\dagger$")
plt.plot(m_squark, sigma2, lw=2, ls="--", c='red', label = r"$GG \to \tilde{q}\tilde{q}^\dagger$")
plt.plot(m_squark, sigma3_MSSM, lw=2, ls="-", c='green', label = r"$qq \to \tilde{q}\tilde{q}$")
plt.plot(m_squark, sigma4_MSSM, lw=2, ls=":", c='deepskyblue', label = r"$q\overline{q} \to \tilde{g}\tilde{g}$")
plt.plot(m_squark, sigma5_MSSM, lw=2, ls=":", c='darkblue', label = r"$GG \to \tilde{g}\tilde{g}$")
plt.plot(m_squark, sigma6, lw=2, ls="-.", c='black', label = r"$qG \to \tilde{q}\tilde{g}$")
#plt.plot(m_squark, sigma1_MSSM+sigma2, lw=2, ls="--", c='red', label = r"$\tilde{q}\tilde{q}^\dagger$")
#plt.plot(m_squark, sigma3_MSSM, lw=2, ls="-", c='green', label = r"$\tilde{q}\tilde{q}$")
#plt.plot(m_squark, sigma4_MSSM+sigma5_MSSM, lw=2, ls=":", c='darkblue', label = r"$\tilde{g}\tilde{g}$")
#plt.plot(m_squark, sigma6, lw=2, ls="-.", c='black', label = r"$\tilde{q}\tilde{g}$")

plt.legend(loc=1,prop={'size':21})

props = dict(boxstyle='round', facecolor='w', alpha=0.5)
first_window.text(800, 5*10**5, r"$\frac{m_{\tilde{g}}}{m_{\tilde{q}}} = 0.9$", fontsize=22,
        verticalalignment='top', bbox=props)



second_window = plt.subplot(122)
#plt.title(r"MRSSM", size = 22)
plt.xlabel(r"$m_{\tilde{q}}$ in GeV", size = 22)
plt.ylabel(r"$\sigma^{\mathrm{B}}_{\mathrm{MRSSM}}$ in fb", size = 22)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)

# set scientific notation
plt.yscale('log')
#plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.axis([min(m_squark),max(m_squark),sigma_min,sigma_max])
#plt.axis([min(m_squark),max(m_squark),0,1])
plt.axes(second_window)

second_window.xaxis.set_major_formatter(FormatStrFormatter('%0.0f'))

plt.plot(m_squark, sigma1_MRSSM, lw=2, ls="--", c='orange', label = r"$q\overline{q} \to \tilde{q}\tilde{q}^\dagger$")
plt.plot(m_squark, sigma2, lw=2, ls="--", c='red', label = r"$GG \to \tilde{q}\tilde{q}^\dagger$")
plt.plot(m_squark, sigma3_MRSSM, lw=2, ls="-", c='green', label = r"$qq \to \tilde{q}\tilde{q}$")
plt.plot(m_squark, sigma4_MRSSM, lw=2, ls=":", c='deepskyblue', label = r"$q\overline{q} \to \tilde{g}\overline{\tilde{g}}$")
plt.plot(m_squark, sigma5_MRSSM, lw=2, ls=":", c='darkblue', label = r"$GG \to \tilde{g}\overline{\tilde{g}}$")
plt.plot(m_squark, sigma6, lw=2, ls="-.", c='black', label = r"$qG \to \tilde{q}\tilde{g}$")
#plt.plot(m_squark, sigma1_MRSSM+sigma2, lw=2, ls="--", c='red', label = r"$\tilde{q}\tilde{q}^\dagger$")
#plt.plot(m_squark, sigma3_MRSSM, lw=2, ls="-", c='green', label = r"$\tilde{q}\tilde{q}$")
#plt.plot(m_squark, sigma4_MRSSM+sigma5_MRSSM, lw=2, ls=":", c='darkblue', label = r"$\tilde{g}\overline{\tilde{g}}$")
#plt.plot(m_squark, sigma6, lw=2, ls="-.", c='black', label = r"$\tilde{q}\tilde{g}$")

plt.legend(loc=1,prop={'size':21})

second_window.text(800, 5*10**5, r"$\frac{m_{\tilde{g}}}{m_{\tilde{q}}} = 0.9$", fontsize=22,
        verticalalignment='top', bbox=props)

plt.subplots_adjust(wspace = 0.3, top=0.85)

plt.show()
plt.draw()
