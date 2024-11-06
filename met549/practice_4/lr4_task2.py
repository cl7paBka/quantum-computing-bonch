from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import numpy as np
import matplotlib.pyplot as plt

# Создаем квантовую схему
qc = QuantumCircuit(1)

# Вычисляем угол theta
theta = 2 * np.arccos(2 / np.sqrt(5))

# Применяем R_y к кубиту
qc.ry(theta, 0)

# Измеряем состояние кубита
qc.measure_all()

# Визуализируем квантовую схему
print("Квантовая схема:")
qc.draw('mpl')  # Используем matplotlib для визуализации схемы
plt.show()

# Выполняем симуляцию
simulator = Aer.get_backend('aer_simulator')
compiled_circuit = transpile(qc, simulator)
result = simulator.run(compiled_circuit).result()

# Получаем результаты
counts = result.get_counts()
print("Результаты измерений:", counts)

# Визуализация результатов
plot_histogram(counts)
plt.show()

print('|0〉  появляется примерно в 80% случаев, а в состоянии  |1〉  — в 20% случаев. это объясняется углом поворота')
