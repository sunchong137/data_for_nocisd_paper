import numpy as np
from pyscf import gto, scf, ci
np.set_printoptions(edgeitems=30, linewidth=100000, precision=5)
from noci_jax import nocisd
from noci_jax import slater, pyscf_helper, select_ci

nH = 10
bl = 1.1
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

dt = 0.1
tmats, coeffs = nocisd.compress(myci, civec=civec, dt1=dt, dt2=dt, tol2=1e-5)
nvir, nocc = tmats.shape[2:]
rmats_new = slater.tvecs_to_rmats(tmats, nvir, nocc)
rmats_fix = np.zeros((1, 2, norb, nocc))
rmats_fix[0, 0,:nocc, :nocc] = np.eye(nocc)
rmats_fix[0, 1,:nocc, :nocc] = np.eye(nocc)

# select through m_tol
m_tol = 1e-6
r_select = select_ci.select_rmats_ovlp(rmats_fix, rmats_new, m_tol=m_tol)

# select through e_tol
e_tol = 1e-8
r_select_n = select_ci.select_rmats_energy(rmats_fix, r_select[1:], mo_coeff, h1e, h2e, e_tol=e_tol)