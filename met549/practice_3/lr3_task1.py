from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import Aer, AerSimulator
import matplotlib.pyplot as plt

# установка симулятора
simulator = AerSimulator()

# 1 задача
# схема scheme1_4_1
qc1 = QuantumCircuit(2, 2)

# X-гейт к кубиту q0
qc1.x(0)

# H-гейт к кубитам q0 и q1
qc1.h(0)
qc1.h(1)

# применение CNOT (контроль на q1, управление на q0)
qc1.cx(1, 0)

# измерение q0
qc1.measure(0, 0)

# визуализация 1 схемы
qc1.draw(output='mpl')
plt.show()

# транспиляция схемы для симуляции
compiled_qc1 = transpile(qc1, simulator)

# симуляция с числом измерений 1000
result1 = simulator.run(compiled_qc1, shots=1000).result()

# получение результатов симуляции
counts1 = result1.get_counts()

# визуализация результатов
print("Гистограмма для scheme1_4_1:")
plot_histogram(counts1)
plt.show()

# 2 задача
# схема scheme1_4_2 (правая схема)
qc2 = QuantumCircuit(2, 2)

# применение X-гейта к кубиту q0
qc2.x(0)

# применение Hadamard-гейта к кубитам q0 и q1
qc2.h(0)
qc2.h(1)

# применение CNOT (контроль на q1, управление на q0)
qc2.cx(1, 0)

# измерение q0 и q1
qc2.measure(0, 0)
qc2.measure(1, 1)

# визуализация 2 схемы
qc2.draw(output='mpl')
plt.show()

# транспиляция схемы для симуляции
compiled_qc2 = transpile(qc2, simulator)

# симуляция с числом измерений 1000
result2 = simulator.run(compiled_qc2, shots=1000).result()

# получение результатов симуляции
counts2 = result2.get_counts()

# визуализация результатов
print("Гистограмма для scheme1_4_2:")
plot_histogram(counts2)
plt.show()