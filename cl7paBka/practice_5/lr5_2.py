from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

scheme_2 = QuantumCircuit(3, 1)
scheme_2.x(0)
scheme_2.x(1)
scheme_2.ccx(0, 1, 2)
scheme_2.x(0)
scheme_2.x(1)
scheme_2.x(2)
scheme_2.measure(2, 0)
scheme_2.draw('mpl', filename="результат_or.png")
plt.show()

simulator = AerSimulator()
compiled_circuit = transpile(scheme_2, simulator)

job = simulator.run(compiled_circuit, shots=1024)
result = job.result()

counts = result.get_counts(compiled_circuit)

plot_histogram(counts)
plt.show()

scheme_3 = QuantumCircuit(3, 1)
scheme_3.ccx(0, 1, 2)
scheme_3.measure(2, 0)
scheme_3.draw('mpl', filename="результат_and.png")
plt.show()

simulator = AerSimulator()
compiled_circuit = transpile(scheme_3, simulator)

job = simulator.run(compiled_circuit, shots=1024)
result = job.result()

counts = result.get_counts(compiled_circuit)

plot_histogram(counts)
plt.show()