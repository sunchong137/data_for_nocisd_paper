import numpy as np
from fancyplt import sciplot
import matplotlib.pyplot as plt
from matplotlib import rcParams
import os 

save_dir = "./figures/"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
    
params = sciplot.SciRcParams
rcParams.update(params)
pclrs = sciplot.PCLRS # using pastel colors
lw = 2
mrkrs = ["o", "^", "d", "p", "s"]

def plot_n2_diss_curve(basis="631g"):
    sfig_name = save_dir + f"N2_{basis}_diss_curve.pdf"
    # load refs
    cicc = np.load(f"./results/energy_N2_{basis}_ci_ccsd.npy")
    uhf = np.load(f"./results/energy_N2_{basis}_uhf.npy")
    shci = np.load(f"./results/energy_N2_{basis}_shci.npy")
    dat1 = np.loadtxt(f"./results/energy_N2_{basis}_fedsd_n1.txt")
    fig, ax = plt.subplots()
    ax.plot(uhf[:, 0], uhf[:, 1], c=pclrs["grey"],label="UHF") # marker=mrkrs[0], mfc="none", mew=2, 
    ax.plot(cicc[:, 0], cicc[:, 1], c=pclrs["deeppurple"], marker=mrkrs[1], mfc="none", mew=2, label="CISD")
    ax.plot(cicc[:, 0], cicc[:, 2], c=pclrs["deepblue"], marker=mrkrs[2], mfc="none", mew=2, label="CCSD")
    
    ax.plot(dat1[:, 0], dat1[:, 2], c=pclrs["green"], marker=mrkrs[4], mfc="none", mew=2, label="NOCISD(2)")
    ax.plot(shci[:, 0], shci[:, 1], c='grey', label="SHCI")
    ax.legend()
    ax.set_xlabel(r"$R_{\mathrm{N-N}}$ ($\mathrm{\AA}$)")
    ax.set_ylabel(r"$E$ (Hartree)")
    ax.grid(True, color=pclrs["grey"], linestyle='--')
    #plt.show()
    fig.savefig(sfig_name)

plot_n2_diss_curve()
