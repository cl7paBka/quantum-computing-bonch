from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, circuit_drawer
import matplotlib.pyplot as plt

simulator = AerSimulator()
# Инициализация схемы для OR
qc_or = QuantumCircuit(3, 1)

# Инвертируем входные кубиты для реализации операции ИЛИ
qc_or.x(0)
qc_or.x(1)

# Гейт Тоффоли для реализации OR
qc_or.ccx(0, 1, 2)

# Возвращаем кубиты в исходное состояние
qc_or.x(0)
qc_or.x(1)

# Измерение
qc_or.measure(2, 0)

# Транспиляция схемы
compiled_circuit_or = transpile(qc_or, simulator)

# Вывод схемы на экран
circuit_drawer(qc_or, output='mpl')
plt.show()

# Выполнение симуляции
job_or = simulator.run(compiled_circuit_or, shots=1024)
result_or = job_or.result()

# Результаты измерений
counts_or = result_or.get_counts(compiled_circuit_or)

# Построение гистограммы
plot_histogram(counts_or)
plt.show()

# Инициализация схемы для AND
qc_and = QuantumCircuit(3, 1)

# Применяем гейт Тоффоли
qc_and.ccx(0, 1, 2)

# Измерение
qc_and.measure(2, 0)

# Транспиляция схемы
compiled_circuit_and = transpile(qc_and, simulator)

# Вывод схемы на экран
circuit_drawer(qc_and, output='mpl')
plt.show()

# Выполнение симуляции
job_and = simulator.run(compiled_circuit_and, shots=1024)
result_and = job_and.result()

# Результаты измерений
counts_and = result_and.get_counts(compiled_circuit_and)

# Построение гистограммы
plot_histogram(counts_and)
plt.show()
