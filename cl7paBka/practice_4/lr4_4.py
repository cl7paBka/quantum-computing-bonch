from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, circuit_drawer
import matplotlib.pyplot as plt

qc_h = QuantumCircuit(1)

qc_h.h(0)
qc_h.h(0)
qc_h.measure_all()

qc_h1 = QuantumCircuit(1)

qc_h1.x(0)
qc_h1.h(0)
qc_h1.h(0)
qc_h1.measure_all()

qc_h.draw(output='mpl', filename=f"результат_гейт_адамара_0.png")
plt.show()

simulator = AerSimulator()

qc_h.save_statevector()
compiled_circuit_h = transpile(qc_h, simulator)
result_h = simulator.run(compiled_circuit_h).result()

statevector_h = result_h.get_statevector()
print(f"{statevector_h}")

compiled_circuit_h = transpile(qc_h, simulator)
result_h = simulator.run(compiled_circuit_h).result()
counts_h = result_h.get_counts()

plot_histogram(counts_h)
plt.show()

qc_h1.draw(output='mpl', filename=f"результат_гейт_адамара_1.png")
plt.show()

qc_h1.save_statevector()
compiled_circuit_h1 = transpile(qc_h1, simulator)
result_h1 = simulator.run(compiled_circuit_h1).result()

statevector_h1 = result_h1.get_statevector()
print(f"{statevector_h1}")

compiled_circuit_h1 = transpile(qc_h1, simulator)
result_h1 = simulator.run(compiled_circuit_h1).result()
counts_h1 = result_h1.get_counts()

plot_histogram(counts_h1)
plt.show()