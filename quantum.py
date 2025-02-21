
import matplotlib as inline
import ipyvuetify
import jupyter
import numpy as np
import scqubits as scq

cos2phi_qubit = scq.Cos2PhiQubit.create()

cos2phi_qubit = scq.Cos2PhiQubit(EJ = 20.0,
                                 ECJ = 2.0,
                                 EL = 1.0,
                                 EC = 0.04,
                                 dCJ = 0.0,
                                 dL = 0.8,
                                 dEJ = 0.0,
                                 flux = 0.5,
                                 ng = 0.0,
                                 ncut = 7,
                                 phi_cut = 7,
                                 zeta_cut = 40)

print(cos2phi_qubit)

cos2phi_qubit.plot_potential()

cos2phi_qubit.dL = 0.0
cos2phi_qubit.n_cut = 10
cos2phi_qubit.phi_cut = 10

cos2phi_qubit.eigenvals(evals_count=10)

