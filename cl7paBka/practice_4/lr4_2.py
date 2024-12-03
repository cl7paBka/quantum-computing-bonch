from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import numpy as np
import matplotlib.pyplot as plt

qc = QuantumCircuit(1)
theta = 2 * np.arcsin(np.sqrt(0.2))
qc.ry(theta, 0)
qc.z(0)
qc.measure_all()

simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
result = simulator.run(compiled_circuit).result()
counts = result.get_counts()
plot_histogram(counts)
plt.show()

