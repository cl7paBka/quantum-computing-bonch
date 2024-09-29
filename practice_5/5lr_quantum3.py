from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, circuit_drawer
import matplotlib.pyplot as plt

simulator = AerSimulator()

# Инициализация схемы для XOR
qc_xor = QuantumCircuit(2, 1)

# Применение CNOT гейта для реализации XOR
qc_xor.cx(0, 1)

# Измерение второго кубита
qc_xor.measure(1, 0)

# Транспиляция схемы
compiled_circuit_xor = transpile(qc_xor, simulator)

# Вывод схемы на экран
circuit_drawer(qc_xor, output='mpl')
plt.show()

# Выполнение симуляции
job_xor = simulator.run(compiled_circuit_xor, shots=1024)
result_xor = job_xor.result()

# Результаты измерений
counts_xor = result_xor.get_counts(compiled_circuit_xor)

# Построение гистограммы
plot_histogram(counts_xor)
plt.show()
