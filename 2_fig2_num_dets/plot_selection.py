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

n2eq = np.loadtxt("results/n2_R1.1.txt")
h6eq = np.loadtxt("results/h6_R1.0.txt")
lifeq = np.loadtxt("results/lif_R1.4.txt")
n2l = np.loadtxt("results/n2_R2.0.txt")
h6l = np.loadtxt("results/h6_R2.5.txt")
lifl = np.loadtxt("results/lif_R4.0.txt")

def plot_compress():
    fig, ax = plt.subplots()
    width = 0.25

    dclr = ["blueviolet", "teal", "chocolate"]
    lclr = ["plum", "paleturquoise", "bisque"]
    tags = np.array([0, 1, 2])
    tags2 = tags + len(tags)
    ax.bar(tags, h6eq[:, 0], width, color=dclr[2], edgecolor="k", label=r"H$_6$")
    ax.bar(tags, h6eq[:, 1], width, color=lclr[2], edgecolor="k")
    ax.bar(tags+width, lifeq[:, 0], width, color=dclr[1], edgecolor="k", label="LiF")
    ax.bar(tags+width, lifeq[:, 1], width, color=lclr[1], edgecolor="k")
    ax.bar(tags+width*2, n2eq[:, 0], width, color=dclr[0], edgecolor="k", label=r"N$_2$")
    ax.bar(tags+width*2, n2eq[:, 1], width, color=lclr[0], edgecolor="k")

    # ax.bar(tags2, n2l[:, 0], width, color="blueviolet", edgecolor="k")
    # ax.bar(tags2+width, n2l[:, 1], width, color="plum", edgecolor="k")
    ax.set_xticks(tags+width, ["STO-3G", "6-31G", "CCPV-DZ"])
    ax.set_ylabel("Number of NOSDs")
    plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))

    ax.legend()
    fig.savefig("figures/cisd_compress_bar.png")
    # plt.show()

def plot_metric():
    fig, ax = plt.subplots()
    width = 0.25

    dclr = ["blueviolet", "teal", "chocolate"]
    lclr = ["plum", "paleturquoise", "bisque"]
    tags = np.array([0, 1, 2])
    tags2 = tags + len(tags)
    ax.bar(tags, h6eq[:, 1], width, color=dclr[2], edgecolor="k", label=r"H$_6$")
    ax.bar(tags, h6eq[:, 2], width, color=lclr[2], edgecolor="k")
    ax.bar(tags+width, lifeq[:, 1], width, color=dclr[1], edgecolor="k", label="LiF")
    ax.bar(tags+width, lifeq[:, 2], width, color=lclr[1], edgecolor="k")
    ax.bar(tags+width*2, n2eq[:, 1], width, color=dclr[0], edgecolor="k", label=r"N$_2$")
    ax.bar(tags+width*2, n2eq[:, 2], width, color=lclr[0], edgecolor="k")

    # ax.bar(tags2, h6l[:, 1], width, color=dclr[2], edgecolor="k", label=r"H$_6$")
    # ax.bar(tags2, h6l[:, 2], width, color=lclr[2], edgecolor="k")
    # ax.bar(tags2+width, lifl[:, 1], width, color=dclr[1], edgecolor="k", label="LiF")
    # ax.bar(tags2+width, lifl[:, 2], width, color=lclr[1], edgecolor="k")
    # ax.bar(tags2+width*2, n2l[:, 1], width, color=dclr[0], edgecolor="k", label=r"N$_2$")
    # ax.bar(tags2+width*2, n2l[:, 2], width, color=lclr[0], edgecolor="k")

    # ax.bar(tags2, n2l[:, 0], width, color="blueviolet", edgecolor="k")
    # ax.bar(tags2+width, n2l[:, 1], width, color="plum", edgecolor="k")
    ax.set_xticks(tags+width, ["STO-3G", "6-31G", "CCPV-DZ"])
    ax.set_ylabel("Number of NOSDs")
    plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))

    ax.legend()
    # fig.savefig("figures/metric_tol.png")
    plt.show()

def plot_energy():

    # n2eq = n2eq[:-1]
    # h6eq = h6eq[:-1]
    # lifeq = lifeq[:-1]
    # n2l = n2l[:-1]
    # h6l = h6l[:-1]
    # lifl = lifl[:-1]

    fig, ax = plt.subplots()
    width = 0.25

    dclr = ["blueviolet", "teal", "chocolate"]
    lclr = ["plum", "paleturquoise", "bisque"]
    wclr = ["lavenderblush", "azure", "floralwhite"]
    tags = np.array([0, 1])
    tags2 = tags + len(tags)
    plot_patterns = False
    if plot_patterns:
        ptrns = [ "//" ,  "xx", "\\", "*", "|" , "-", "++", "o", "O"] # "" means empty
    else: 
        ptrns = ["", "", ""]
    ax.bar(tags, h6eq[:-1, 1], width, color=dclr[2], hatch=ptrns[0], edgecolor="k", label=r"H$_6$")
    ax.bar(tags, h6eq[:-1, 2], width, color=lclr[2], hatch=ptrns[1], edgecolor="k")
    ax.bar(tags, h6eq[:-1, 3], width, color=wclr[2], hatch=ptrns[2], edgecolor="k")

    ax.bar(tags+width, lifeq[:-1, 1], width, color=dclr[1], hatch=ptrns[0], edgecolor="k", label="LiF")
    ax.bar(tags+width, lifeq[:-1, 2], width, color=lclr[1], hatch=ptrns[1], edgecolor="k")
    ax.bar(tags+width, lifeq[:-1, 3], width, color=wclr[1], hatch=ptrns[2], edgecolor="k")
    
    ax.bar(tags+width*2, n2eq[:-1, 1], width, color=dclr[0], hatch=ptrns[0], edgecolor="k", label=r"N$_2$")
    ax.bar(tags+width*2, n2eq[:-1, 2], width, color=lclr[0], hatch=ptrns[1], edgecolor="k")
    ax.bar(tags+width*2, n2eq[:-1, 3], width, color=wclr[0], hatch=ptrns[2], edgecolor="k")

    ax.bar(tags2, h6l[:-1, 1], width, color=dclr[2], hatch=ptrns[0], edgecolor="k")
    ax.bar(tags2, h6l[:-1, 2], width, color=lclr[2], hatch=ptrns[1], edgecolor="k")
    ax.bar(tags2, h6l[:-1, 3], width, color=wclr[2], hatch=ptrns[2], edgecolor="k")

    ax.bar(tags2+width, lifl[:-1, 1], width, color=dclr[1], hatch=ptrns[0], edgecolor="k")
    ax.bar(tags2+width, lifl[:-1, 2], width, color=lclr[1], hatch=ptrns[1], edgecolor="k")
    ax.bar(tags2+width, lifl[:-1, 3], width, color=wclr[1], hatch=ptrns[2], edgecolor="k")

    ax.bar(tags2+width*2, n2l[:-1, 1], width, color=dclr[0], hatch=ptrns[0], edgecolor="k")
    ax.bar(tags2+width*2, n2l[:-1, 2], width, color=lclr[0], hatch=ptrns[1], edgecolor="k")
    ax.bar(tags2+width*2, n2l[:-1, 3], width, color=wclr[0], hatch=ptrns[2], edgecolor="k")
    # else:
    #     ax.bar(tags, h6eq[:-1, 1], width, color=dclr[2], edgecolor="k", label=r"H$_6$")
    #     ax.bar(tags, h6eq[:-1, 2], width, color=lclr[2], edgecolor="k")
    #     ax.bar(tags, h6eq[:-1, 3], width, color=wclr[2], edgecolor="k")

    #     ax.bar(tags+width, lifeq[:-1, 1], width, color=dclr[1], edgecolor="k", label="LiF")
    #     ax.bar(tags+width, lifeq[:-1, 2], width, color=lclr[1], edgecolor="k")
    #     ax.bar(tags+width, lifeq[:-1, 3], width, color=wclr[1], edgecolor="k")
        
    #     ax.bar(tags+width*2, n2eq[:-1, 1], width, color=dclr[0],  edgecolor="k", label=r"N$_2$")
    #     ax.bar(tags+width*2, n2eq[:-1, 2], width, color=lclr[0],  edgecolor="k")
    #     ax.bar(tags+width*2, n2eq[:-1, 3], width, color=wclr[0],  edgecolor="k")

    #     ax.bar(tags2, h6l[:-1, 1], width, color=dclr[2], edgecolor="k")
    #     ax.bar(tags2, h6l[:-1, 2], width, color=lclr[2], edgecolor="k")
    #     ax.bar(tags2, h6l[:-1, 3], width, color=wclr[2], edgecolor="k")

    #     ax.bar(tags2+width, lifl[:-1, 1], width, color=dclr[1], edgecolor="k")
    #     ax.bar(tags2+width, lifl[:-1, 2], width, color=lclr[1], edgecolor="k")
    #     ax.bar(tags2+width, lifl[:-1, 3], width, color=wclr[1], edgecolor="k")

    #     ax.bar(tags2+width*2, n2l[:-1, 1], width, color=dclr[0], edgecolor="k")
    #     ax.bar(tags2+width*2, n2l[:-1, 2], width, color=lclr[0], edgecolor="k")
    #     ax.bar(tags2+width*2, n2l[:-1, 3], width, color=wclr[0], edgecolor="k")
    # ax.bar(tags2, n2l[:, 0], width, color="blueviolet", edgecolor="k")
    # ax.bar(tags2+width, n2l[:, 1], width, color="plum", edgecolor="k")
    ax.set_xticks(np.array([0,1,2,3])+width, ["STO-3G", "6-31G", "STO-3G", "6-31G"])
    ax.set_ylabel("Number of NOSDs")
    plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))

    ymin, ymax = ax.get_ylim()
    x = np.ones(2)*1.75
    y = np.array([ymin, ymax])
    ax.plot(x, y, color='gray')
    ax.set_ylim(ymin, ymax)
    ax.legend()
    fig.savefig("figures/energy_tol.png")
    # plt.show()

plot_energy()
