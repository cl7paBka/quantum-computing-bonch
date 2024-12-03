#pip install qiskit matplotlib numpy
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer, AerSimulator
from qiskit.visualization import plot_histogram
import numpy as np
import matplotlib.pyplot as plt

q0_prob = 0.05
q1_prob = 0.1
q2_prob = 0.2

theta_q0 = 2 * np.arccos(np.sqrt(q0_prob))
theta_q1 = 2 * np.arccos(np.sqrt(q1_prob))
theta_q2 = 2 * np.arccos(np.sqrt(q2_prob))

qc = QuantumCircuit(3)
qc.rx(theta_q0, 0)
qc.ry(theta_q1, 1)
qc.u(theta_q2, 0, 0, 2)

simulator = AerSimulator()
qc.measure_all()

qc.draw(output='mpl', filename=f"результат_scheme2_3.png")

compiled_circuit = transpile(qc, simulator)

job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(qc)
print(counts)

plot_histogram(counts)
plt.show()
