from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, circuit_drawer
import numpy as np
import matplotlib.pyplot as plt

# Задача 3: Трёхкубитная схема scheme2_3
qc_3 = QuantumCircuit(3)

# Используем Ry и Rz для подготовки состояний
# Кубит q0 в состоянии суперпозиции 0.05
theta_q0 = 2 * np.arccos(np.sqrt(0.05))
qc_3.ry(theta_q0, 0)

# Кубит q1 в состоянии суперпозиции 0.6
theta_q1 = 2 * np.arccos(np.sqrt(0.4))
qc_3.ry(theta_q1, 1)

# Кубит q2 в состоянии суперпозиции 0.65
theta_q2 = 2 * np.arccos(np.sqrt(0.65))
qc_3.rz(theta_q2, 2)

# Добавляем измерения всех кубитов
qc_3.measure_all()

# Отображаем схему
qc_3.draw('mpl')  # Используем matplotlib для визуализации схемы
plt.show()

# Определяем симулятор
simulator = AerSimulator()

# Симуляция схемы
compiled_circuit_3 = transpile(qc_3, simulator)
result_3 = simulator.run(compiled_circuit_3).result()

# Получаем результаты измерений
counts_3 = result_3.get_counts()

# Гистограмма результатов
plot_histogram(counts_3)
plt.show()
