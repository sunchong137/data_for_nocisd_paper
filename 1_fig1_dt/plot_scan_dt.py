import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import os 

save_dir = "./figures/"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
    
params = {
        'font.family': 'serif',
        "mathtext.fontset" : "stix",
        'legend.fontsize': 'x-large',
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large',
         'figure.autolayout': True,
         'savefig.dpi': 400
         }
rcParams.update(params)

def plot_h6():
    data1 = np.loadtxt("results/h6_sto3g.txt")
    data2 = np.loadtxt("results/h6_631g.txt")

    fig, ax = plt.subplots()
    ax.plot(data1[:, 0], np.log10(np.abs(data1[:, 1])), c="navy", marker="o", label="STO3G")
    ax.plot(data2[:, 0], np.log10(np.abs(data2[:, 1])), c="cornflowerblue", marker="^", label="631G")

    # ax.set_ylim(-0.006, 0.006)
    xmin, xmax = ax.get_xlim()
    x = np.linspace(xmin, xmax, 4)
    y = np.zeros(4)
    # ax.plot(x, y, '--', c="grey")
    ax.set_xlim(xmin, xmax)
    #ax.set_xticks(np.arange(0,1,0.1))
    ax.legend()
    plt.xlabel(r"$\delta t$")
    plt.ylabel(r"$\log_{10}(|\Delta E|)$")
    # plt.show()
    fig.savefig("figures/h6_scan_dt.png")

def plot_mols():
    n2 = np.loadtxt("results/n2_sto3g.txt")
    lif = np.loadtxt("results/lif_sto3g_R1.5.txt")
    h10 = np.loadtxt("results/h10_sto3g.txt")
    fig, ax = plt.subplots()

    ax.plot(n2[:, 0], np.log10(np.abs(n2[:, 1])), lw=2, c="chocolate", marker="o", label=r"$\mathrm{N}_2$")
    ax.plot(lif[:, 0], np.log10(np.abs(lif[:, 1])), lw=2, c="olivedrab", marker="^", label="LiF")
    ax.plot(h10[:, 0], np.log10(np.abs(h10[:, 1])), lw=2, c="rebeccapurple", marker="d", label=r"$\mathrm{H}_{10}$")
    ax.legend()

    plt.xlabel(r"$\delta t$")
    plt.ylabel(r"$\log_{10}(|\Delta E|)$")
    fig.savefig("figures/scan_mol.png")
    # plt.show() 

plot_h6()
