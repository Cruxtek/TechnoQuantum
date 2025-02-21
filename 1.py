from qiskit import QuantumCircuit
#control de heisemberg 
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
#jugando con qubits
qc.measure([0, 1], [0, 1])
from matplotlib import pyplot as plt
qc.draw('mpl')
plt.savefig('heisembergqt.jpg')