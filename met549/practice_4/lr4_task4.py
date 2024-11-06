import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit_aer import Aer
import numpy as np
from qiskit.visualization import plot_histogram

from qiskit_aer import AerSimulator


# Создаем квантовую цепь с 1 кубитом
qc = QuantumCircuit(1)

# Применяем гейт Адамара к кубиту
qc.h(0)

# Визуализируем схему
print("Схема квантовой цепи:")
qc.draw('mpl')
plt.show()

qc.measure_all()

# Создаем симулятор

simulator = Aer.get_backend('aer_simulator')
result = simulator.run(qc).result()

# Получаем результаты измерений
counts = result.get_counts()
print("Результаты измерений:", counts)

# Визуализация результатов
plot_histogram(counts)
plt.show()

print('равное распределение вероятностей между состояниями |0⟩ и |1⟩')