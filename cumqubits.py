import numpy as np

import scqubits as scq
from scqubits import HilbertSpace, InteractionTerm, ParameterSweep

def energies(frequency_r, frequency_q, g, n_cutoff):
    delta = frequency_r - frequency_q
    energies1 = (np.arange(1, n_cutoff) - 0.5) * frequency_r
    energies2 = np.sqrt(delta**2/4 + np.arange(1, n_cutoff) * g**2)
    energies_plus = energies1 + energies2
    energies_minus = energies1 - energies2
    energies_0 = np.asarray([[-0.5 * frequency_q]])
    all_energies = np.append(energies_0, energies_minus)
    all_energies = np.append(all_energies, energies_plus)
    return np.sort(all_energies)

frequency_q = 1.0
frequency_r = 0.8
g = 0.1


qubit = scq.GenericQubit(E=frequency_q)

osc = scq.Oscillator(
    E_osc=frequency_r,
    truncated_dim=10  # up to 9 photons
)

# Form a list of all components making up the Hilbert space.
hilbertspace = HilbertSpace([qubit, osc])

hilbertspace.add_interaction(
    g_strength = g,
    op1 = qubit.sm_operator,
    op2 = osc.creation_operator,
    add_hc = True
)

print(hilbertspace)

