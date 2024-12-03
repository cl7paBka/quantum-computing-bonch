from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer, AerSimulator
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.quantum_info import Statevector
import numpy as np
import matplotlib.pyplot as plt

alpha_prob = 0.6
beta_prob = 0.4

theta_b = 2 * np.arccos(np.sqrt(alpha_prob))
qc_b = QuantumCircuit(1)
qc_b.rx(theta_b, 0)

simulator = AerSimulator()
qc_b.save_statevector()
compiled_circuit = transpile(qc_b, simulator)

result = simulator.run(compiled_circuit).result()

statevector = result.get_statevector()
print(f"{statevector}")

qc_b.measure_all()
compiled_circuit = transpile(qc_b, simulator)
result = simulator.run(compiled_circuit).result()
counts = result.get_counts()

plot_histogram(counts)
plt.show()