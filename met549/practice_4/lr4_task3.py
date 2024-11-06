import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit_aer import Aer
import numpy as np
from qiskit.visualization import plot_histogram

# Функция для вычисления угла R_y
def get_theta(probability):
    return 2 * np.arccos(np.sqrt(probability))

# Создаем квантовую схему на 3 кубита
qc = QuantumCircuit(3)

# Углы для R_y, чтобы достичь заданных вероятностей
theta_q0 = get_theta(0.05)  # Вероятность состояния |0⟩ кубита q0
theta_q1 = get_theta(0.1)   # Вероятность состояния |0⟩ кубита q1
theta_q2 = get_theta(0.2)   # Вероятность состояния |0⟩ кубита q2

# Применяем R_y к каждому кубиту
qc.ry(theta_q0, 0)
qc.ry(theta_q1, 1)
qc.ry(theta_q2, 2)

# Измеряем все кубиты
qc.measure_all()

# Визуализируем квантовую схему
print("Квантовая схема:")
qc.draw('mpl')
plt.show()

# Выполняем симуляцию
simulator = Aer.get_backend('aer_simulator')
result = simulator.run(qc).result()

# Получаем результаты измерений
counts = result.get_counts()
print("Результаты измерений:", counts)

# Визуализация результатов
plot_histogram(counts)
plt.show()


print(' вероятности результатов измерений напрямую зависят от углов вращения')