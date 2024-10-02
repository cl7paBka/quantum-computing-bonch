from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import numpy as np
import matplotlib.pyplot as plt

# Задача 2: Использование однокубитного гейта Ry для состояния |c>
alpha_prob_c = 0.8
beta_prob_c = 0.2

# Вычисляем угол для Ry
theta_c = 2 * np.arccos(np.sqrt(alpha_prob_c))

# Создаем квантовую схему
qc_c = QuantumCircuit(1)
qc_c.ry(theta_c, 0)

# Определяем симулятор
simulator = AerSimulator()

# Симуляция состояния
qc_c.save_statevector()
compiled_circuit = transpile(qc_c, simulator)
result = simulator.run(compiled_circuit).result()

# Получаем вектор состояния
statevector_c = result.get_statevector()
print(f"Statevector for Task 2: {statevector_c}")

# Визуализация
qc_c.measure_all()  # Добавляем измерение
compiled_circuit = transpile(qc_c, simulator)
result = simulator.run(compiled_circuit).result()
counts = result.get_counts()

# Построение гистограммы
plot_histogram(counts)
plt.show()
