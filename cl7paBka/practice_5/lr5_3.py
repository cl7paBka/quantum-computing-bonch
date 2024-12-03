from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator, Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(2, 1)

qc.cx(0, 1)
qc.measure(1, 0)
simulator = AerSimulator()
transpiled_qc = transpile(qc, simulator)

result = simulator.run(transpiled_qc).result()

counts = result.get_counts()

qc.draw('mpl', filename="результат_function3.png")
plot_histogram(counts)
plt.show()