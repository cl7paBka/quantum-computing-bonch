from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, circuit_drawer
import matplotlib.pyplot as plt

# Инициализация квантовой схемы с 3 кубитами и 1 классическим битом
qc = QuantumCircuit(3, 1)

# Применение H-гейтов к первым двум кубитам
qc.h(0)
qc.h(1)

# Применение гейта Тоффоли (CCX) с двумя управляющими кубитами и одним целевым
qc.ccx(0, 1, 2)

# Измерение третьего кубита и запись результата в классический бит
qc.measure(2, 0)

# Транспиляция схемы
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)

# Вывод схемы на экран
circuit_drawer(qc, output='mpl')
plt.show()

# Выполнение симуляции
job = simulator.run(compiled_circuit, shots=1024)
result = job.result()

# Результаты измерений
counts = result.get_counts(compiled_circuit)

# Построение гистограммы
plot_histogram(counts)
plt.show()
