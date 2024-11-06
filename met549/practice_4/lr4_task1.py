from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer, AerSimulator
from qiskit.visualization import plot_histogram
import numpy as np
import matplotlib.pyplot as plt

# Рассчитываем угол
theta = 2 * np.arctan(np.sqrt(2/3))

# Создаем квантовую схему с одним кубитом
qc = QuantumCircuit(1, 1)

# Применяем гейт Rx с рассчитанным углом
qc.rx(theta, 0)

# Измеряем кубит
qc.measure(0, 0)

qc.draw('mpl')  # Используем matplotlib для визуализации схемы
plt.show()

# Транспилируем схему для целевого бэкенда
backend = Aer.get_backend('qasm_simulator')
transpiled_circuit = transpile(qc, backend)

# Выполняем транспилированную схему и получаем результаты
job = backend.run(transpiled_circuit, shots=1024)
results = job.result()
counts = results.get_counts()

plot_histogram(counts)
plt.show()

print('|0〉  появляется примерно в 60% случаев, а в состоянии  |1〉  — в 40% случаев. это объясняется углом поворота')