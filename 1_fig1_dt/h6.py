import numpy as np
from pyscf import gto, scf, ci
np.set_printoptions(edgeitems=30, linewidth=100000, precision=5)
from noci_jax import nocisd
from noci_jax import slater, pyscf_helper
import os 

save_dir = "./results/"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

nH = 6
bl = 1.2
geom = []
for i in range(nH):
    geom.append(['H', .0, .0, i*bl])

mol = gto.Mole()
mol.atom = geom
mol.unit = "angstrom"
mol.basis = "631g"
mol.cart = True
mol.build()

mf = scf.UHF(mol)
mf.kernel()
mo1 = mf.stability()[0]                                                             
init = mf.make_rdm1(mo1, mf.mo_occ)                                                 
mf.kernel(init) 

h1e, h2e, e_nuc = pyscf_helper.get_integrals(mf, ortho_ao=False)
norb, nocc, nvir, mo_coeff = pyscf_helper.get_mos(mf)
e_hf = mf.energy_tot()
nelec = mol.nelectron
myci = ci.UCISD(mf)
e_corr, civec = myci.kernel()
e_cisd = e_hf + e_corr 

dt_vals = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1]
# dt_vals = [0.1]
res_de = []
for dt in dt_vals:
    tmats, coeffs = nocisd.compress(myci, civec=civec, dt1=dt, dt2=dt, tol2=1e-7)
    nvir, nocc = tmats.shape[2:]
    rmats = slater.tvecs_to_rmats(tmats, nvir, nocc)

    # E = slater.noci_energy(rmats, mo_coeff, h1e, h2e, return_mats=False, lc_coeffs=coeffs, e_nuc=e_nuc)
    E = slater.noci_energy_lc(rmats, mo_coeff, h1e, h2e, coeffs, e_nuc=e_nuc)
    err = E - e_cisd
    print(dt, err)
    res_de.append([dt, err])

res_de = np.asarray(res_de)
np.savetxt(save_dir+"/h6_{}.txt".format(mol.basis), res_de)