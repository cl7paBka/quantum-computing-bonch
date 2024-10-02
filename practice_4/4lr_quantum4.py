from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import numpy as np
import matplotlib.pyplot as plt

# Задача 4: Проверка унитарности гейта Адамара
qc_h = QuantumCircuit(1)

# Применяем гейт Адамара дважды
qc_h.h(0)
qc_h.h(0)

# Определяем симулятор
simulator = AerSimulator()

# Симуляция вектора состояния
qc_h.save_statevector()
compiled_circuit_h = transpile(qc_h, simulator)
result_h = simulator.run(compiled_circuit_h).result()

# Получаем вектор состояния
statevector_h = result_h.get_statevector()
print(f"Statevector after applying Hadamard twice: {statevector_h}")

# Визуализация: добавляем измерение и выполняем симуляцию
qc_h.measure_all()
compiled_circuit_h = transpile(qc_h, simulator)
result_h = simulator.run(compiled_circuit_h).result()
counts_h = result_h.get_counts()

# Гистограмма результатов измерения
plot_histogram(counts_h)
plt.show()
