from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer, AerSimulator
from qiskit.visualization import plot_histogram
import numpy as np
import matplotlib.pyplot as plt

# Определение угла theta для варианта b
alpha_prob = 0.6
beta_prob = 0.4

theta_b = 2 * np.arccos(np.sqrt(alpha_prob))

# Создание квантовой схемы
qc_b = QuantumCircuit(1)
qc_b.rx(theta_b, 0)

# Симуляция
simulator = AerSimulator()  # Использование нового симулятора
qc_b.save_statevector()  # Сохраняем вектор состояния для последующего анализа
compiled_circuit = transpile(qc_b, simulator)  # Транспиляция схемы

# Запуск симуляции напрямую, без использования assemble() и Qobj
result = simulator.run(compiled_circuit).result()

# Получение вектора состояния
statevector = result.get_statevector()
print(f"Statevector: {statevector}")

# Визуализация
qc_b.measure_all()  # Добавляем измерение всех кубитов для получения результатов
compiled_circuit = transpile(qc_b, simulator)  # Перетранспиляция схемы
result = simulator.run(compiled_circuit).result()
counts = result.get_counts()

# Гистограмма результатов
plot_histogram(counts)
plt.show()
