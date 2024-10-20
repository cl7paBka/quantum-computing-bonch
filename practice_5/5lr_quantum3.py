from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator, Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Создание квантовой схемы для выполнения операции XOR (⨁)
qc = QuantumCircuit(2, 1)  # 2 кубита и 1 классический бит

# Применение операции CNOT для реализации XOR (x1 ⨁ x2)
qc.cx(0, 1)  # CNOT (контроль на 0, таргет на 1)
qc.measure(1, 0)  # Измерение кубита 1 и запись результата в классический бит

# Транспиляция схемы для симулятора
simulator = AerSimulator()  # Новый симулятор из qiskit_aer
transpiled_qc = transpile(qc, simulator)

# Выполнение симуляции
result = simulator.run(transpiled_qc).result()

# Получение результатов измерений
counts = result.get_counts()

# Построение схемы и гистограммы
qc.draw('mpl')
plot_histogram(counts)
plt.show()
