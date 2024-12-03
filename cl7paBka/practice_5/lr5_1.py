from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import  Aer, AerSimulator
from qiskit.visualization import plot_histogram, circuit_drawer
import matplotlib.pyplot as plt

q = QuantumRegister(3, 'q')
c = ClassicalRegister(1, 'c')

circuit = QuantumCircuit(q, c)
circuit.h(q[0])
circuit.h(q[1])
circuit.ccx(q[0], q[1], q[2])
circuit.h(q[0])
circuit.h(q[1])
circuit.measure(q[2], c[0])

simulator = AerSimulator()
compiled_circuit = transpile(circuit, simulator)
result = simulator.run(compiled_circuit).result()
circuit_drawer(circuit, output='mpl')
plt.show()
counts = result.get_counts(circuit)
print("Результаты:", counts)
plot_histogram(counts)
plt.show()