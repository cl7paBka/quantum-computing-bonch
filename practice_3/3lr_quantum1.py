from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import Aer, AerSimulator
import matplotlib.pyplot as plt

# Установка симулятора
simulator = AerSimulator()

# 1. Схема scheme1_4_1 (левая схема)
qc1 = QuantumCircuit(2, 2)

# Применение X-гейта к кубиту q0
qc1.x(0)

# Применение Hadamard-гейта к кубитам q0 и q1
qc1.h(0)
qc1.h(1)

# Применение CNOT (контроль на q1, управление на q0)
qc1.cx(1, 0)

# Измерение q0
qc1.measure(0, 0)

# Транспиляция схемы для симуляции
compiled_qc1 = transpile(qc1, simulator)

# Симуляция с числом измерений 1000
result1 = simulator.run(compiled_qc1, shots=1000).result()

# Получение результатов симуляции
counts1 = result1.get_counts()

# 2. Схема scheme1_4_2 (правая схема)
qc2 = QuantumCircuit(2, 2)

# Применение X-гейта к кубиту q0
qc2.x(0)

# Применение Hadamard-гейта к кубитам q0 и q1
qc2.h(0)
qc2.h(1)

# Применение CNOT (контроль на q1, управление на q0)
qc2.cx(1, 0)

# Измерение q0 и q1
qc2.measure(0, 0)
qc2.measure(1, 1)

# Транспиляция схемы для симуляции
compiled_qc2 = transpile(qc2, simulator)

# Симуляция с числом измерений 1000
result2 = simulator.run(compiled_qc2, shots=1000).result()

# Получение результатов симуляции
counts2 = result2.get_counts()

# Визуализация результатов
print("Гистограмма для scheme1_4_1:")
plot_histogram(counts1)
plt.show()

print("Гистограмма для scheme1_4_2:")
plot_histogram(counts2)
plt.show()
