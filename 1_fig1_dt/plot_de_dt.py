import numpy as np
from fancyplt import sciplot
import matplotlib.pyplot as plt
from matplotlib import rcParams
import os 

save_dir = "./figures/"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
    
params = sciplot.SciRcParams
params["lines.markersize"] = 4
rcParams.update(params)
pclrs = sciplot.PCLRS # using pastel colors
brtc = sciplot.BRTC # bright colors
lw = 2
mrkrs = ["o", "^", "d", "p", "s"]

def line_plot_dt():
    save_name = save_dir + "fig1_scan_dt.pdf"
    sto1 = np.loadtxt("./data/N2_sto3g_cisd_bl1.00.txt")
    sto2 = np.loadtxt("./data/N2_sto3g_cisd_bl1.50.txt")
    sto3 = np.loadtxt("./data/N2_sto3g_cisd_bl3.00.txt")
    g6311 = np.loadtxt("./data/N2_631g_cisd_bl1.00.txt")
    g6312 = np.loadtxt("./data/N2_631g_cisd_bl1.50.txt")
    g6313 = np.loadtxt("./data/N2_631g_cisd_bl3.00.txt")
    fig, ax = plt.subplots()
    
    ax.plot(sto1[:, 0], np.log10(np.abs(sto1[:, 1])), c=brtc['red'], lw=2, marker="o", label=r"$R = 1.0 \mathrm{\AA}$")
    ax.plot(sto2[:, 0], np.log10(np.abs(sto2[:, 1])), c=brtc["blue"], lw=2, marker="s", label=r"$R = 1.5 \mathrm{\AA}$")
    ax.plot(sto3[:, 0], np.log10(np.abs(sto3[:, 1])), c=brtc["green"], lw=2, marker="^",  label=r"$R = 3.0 \mathrm{\AA}$")
    ax.plot(g6311[:, 0], np.log10(np.abs(g6311[:, 1])), ls='-.', c=brtc['red'], lw=1.5, marker="o")
    ax.plot(g6312[:, 0], np.log10(np.abs(g6312[:, 1])), ls='-.', c=brtc["blue"], lw=1.5, marker="s")
    ax.plot(g6313[:, 0], np.log10(np.abs(g6313[:, 1])), ls='-.', c=brtc["green"], lw=1.5, marker="^")
    
    xmin, xmax = [-0.02, 1.02] 
    ymin, ymax = ax.get_ylim()
    ax.fill_between([xmin, xmax], ymin, -3, color=pclrs["grey"], alpha=0.5, edgecolor="none", zorder=0)

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.grid(True, color=pclrs["grey"], linestyle='--', lw=0.5)

    ax.legend()
    plt.xlabel(r"$\delta t$")
    plt.ylabel(r"$\log_{10}(|\Delta E|)$")
    # plt.show() 
    fig.savefig(save_name)


line_plot_dt()
