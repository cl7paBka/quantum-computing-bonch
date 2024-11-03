import numpy as np
from matplotlib.colors import LinearSegmentedColormap, rgb2hex
from kaleidoscope import bloch_sphere
from qiskit.visualization import plot_bloch_vector
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer, AerSimulator
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.quantum_info import Statevector
import math
import matplotlib.pyplot as plt

# установка симулятора
simulator = AerSimulator()

# scheme1_5_1
qc1 = QuantumCircuit(1, 1)
qc1.h(0)
qc1.reset(0)
qc1.measure(0, 0)

# scheme1_5_2
qc2 = QuantumCircuit(1, 1)
qc2.reset(0)
qc2.x(0)
qc2.measure(0, 0)

# scheme1_5_3
qc3 = QuantumCircuit(1, 1)
qc3.h(0)
qc3.measure(0, 0)

# scheme1_5_4
qc4 = QuantumCircuit(1, 1)
qc4.x(0)
qc4.h(0)
qc4.measure(0, 0)

# scheme1_5_5
qc5 = QuantumCircuit(1, 1)
qc5.rx(math.pi / 5, 0)
qc5.measure(0, 0)

# scheme1_5_6
qc6 = QuantumCircuit(1, 1)
qc6.rx(math.pi / 5, 0)
qc6.x(0)
qc6.measure(0, 0)

schemes = [qc1, qc2, qc3, qc4, qc5, qc6]

# симуляция схем с результатами и визуализацией схем
print("""
Для схемы 1, после применения гейта Адамара кубит сбрасывается в состояние |0⟩, поэтому результаты измерений всегда будут равны 0.
В схеме 2, после сброса в состояние |0⟩ и применения X-гейта, кубит переходит в состояние |1⟩, что приводит к тому, что результаты измерений будут равны 1.
В схеме 3, после сброса в состояние |0⟩, применение X-гейта переводит кубит в состояние |1⟩, а затем гейт Адамара создает суперпозицию состояний, что приводит к распределению результатов измерений между 0 и 1.
Схема 4 использует только вращение Rx(π/5). Поскольку этот угол не приводит кубит точно в состояния |0⟩ или |1⟩, результаты измерений будут варьироваться, но с преобладанием состояния 0.
В схеме 5, после применения гейта Адамара, кубит оказывается в суперпозиции, и результаты измерений будут равномерно распределены между 0 и 1.
В схеме 6 сначала выполняется вращение Rx(π/5), а затем X-гейт. Это изменяет фазу кубита, и результаты измерений будут чаще показывать 1, но также могут встречаться и 0.""")
results = []
for i, qc in enumerate(schemes):
    print(f"Схема scheme1_5_{i + 1}:")

    # отображение схемы
    qc.draw(output='mpl')
    plt.show()  # Необходимо для отображения схемы в стандартном скрипте Python

    # компиляция и выполнение схемы на симуляторе
    compiled_circuit = transpile(qc, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()

    # получение результатов
    counts = result.get_counts(compiled_circuit)
    results.append(counts)

    # печать и отображение результатов
    print(f"Результаты для схемы scheme1_5_{i + 1}: {counts}")
    plot_histogram(counts)
    plt.title(f"Результаты для схемы scheme1_5_{i + 1}")
    plt.show()


# сфера блоха
state_5 = Statevector([1, 0])  # пример для |0⟩
state_6 = Statevector([0, 1])  # пример для |1⟩

# визуализация для схемы 5
plot_bloch_multivector(state_5)
plt.title("Сфера Блоха для схемы scheme1_5_5")
plt.show()

# визуализация для схемы 6
plot_bloch_multivector(state_6)
plt.title("Сфера Блоха для схемы scheme1_5_6")
plt.show()