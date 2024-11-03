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



simulator = AerSimulator()

# Шаг 1: Создание квантовых схем

# (scheme1_5_1)
qc1 = QuantumCircuit(1, 1)
qc1.h(0)
qc1.reset(0)
qc1.measure(0, 0)

# (scheme1_5_2)
qc2 = QuantumCircuit(1, 1)
qc2.reset(0)
qc2.x(0)
qc2.measure(0, 0)

# (scheme1_5_3)
qc3 = QuantumCircuit(1, 1)
qc3.h(0)
qc3.measure(0, 0)

# (scheme1_5_4)
qc4 = QuantumCircuit(1, 1)
qc4.x(0)
qc4.h(0)
qc4.measure(0, 0)

# (scheme1_5_5)
qc5 = QuantumCircuit(1, 1)
qc5.rx(math.pi / 5, 0)
qc5.measure(0, 0)

# (scheme1_5_6)
qc6 = QuantumCircuit(1, 1)
qc6.rx(math.pi / 5, 0)
qc6.x(0)
qc6.measure(0, 0)

schemes = [qc1, qc2, qc3, qc4, qc5, qc6]

# Шаг 2: Симуляция схем с результатами и визуализацией схем
print("""
Для схемы 1, так как кубит сбрасывается в состояние |0⟩ после применения гейта Адамара, результатом измерений будет всегда 0.
Для схемы 2, после сброса в состояние |0⟩ и применения X-гейта, кубит переходит в состояние |1⟩, поэтому результат измерений будет 1.
Для схемы 3, после сброса в состояние |0⟩, применение X-гейта переведёт кубит в состояние |1⟩, а гейт Адамара создаст суперпозицию состояний, поэтому результаты измерений будут распределяться между 0 и 1.
Схема 4 использует только вращение Rx(π/5). Так как угол не приводит кубит точно в состояния |0⟩ или |1⟩, результат измерений будет варьироваться, но с преобладанием состояния 0.
Для схемы 5, после применения гейта Адамара кубит переходит в суперпозицию, и измерения будут поровну распределяться между 0 и 1.
Для схемы 6, сначала применяется вращение Rx(π/5), а затем X-гейт. Это меняет фазу кубита, и результатом измерений будет чаще 1, но могут встречаться и 0.
""")
results = []
for i, qc in enumerate(schemes):
    print(f"Схема scheme1_5_{i + 1}:")

    # Отображение схемы с помощью метода draw и matplotlib
    qc.draw(output='mpl')
    plt.show()  # Необходимо для отображения схемы в стандартном скрипте Python

    # Компиляция и выполнение схемы на симуляторе
    compiled_circuit = transpile(qc, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()

    # Получение результатов
    counts = result.get_counts(compiled_circuit)
    results.append(counts)

    # Печать и отображение результатов
    print(f"Результаты для схемы scheme1_5_{i + 1}: {counts}")
    plot_histogram(counts)
    plt.title(f"Результаты для схемы scheme1_5_{i + 1}")
    plt.show()
# -----------------------
state_5 = Statevector([1, 0])  # пример для |0⟩
state_6 = Statevector([0, 1])  # пример для |1⟩

# Визуализация для схемы 5
plot_bloch_multivector(state_5)
plt.title("Сфера Блоха для схемы scheme1_5_5")
plt.show()

# Визуализация для схемы 6
plot_bloch_multivector(state_6)
plt.title("Сфера Блоха для схемы scheme1_5_6")
plt.show()