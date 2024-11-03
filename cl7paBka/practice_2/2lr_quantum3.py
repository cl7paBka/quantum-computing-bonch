from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Создаем квантовую схему scheme1_3 с 2 кубитами и 2 классическими битами
scheme1_3 = QuantumCircuit(2, 2)

# Применяем Hadamard-гейт к кубиту 0
scheme1_3.h(0)

# Применяем X-гейт к кубиту 1
scheme1_3.x(1)

# Применяем CNOT-гейт с управляющим кубитом 0 и целевым кубитом 1
scheme1_3.cx(0, 1)

# Измеряем состояния кубитов и сохраняем результаты в классические биты
scheme1_3.measure([0, 1], [0, 1])

# Визуализируем схему
scheme1_3.draw(output='mpl')

# Выполним симуляцию с 1000 измерениями
backend = Aer.get_backend('qasm_simulator')
transpiled_circuit = transpile(scheme1_3, backend)

# Запуск схемы с указанием количества измерений (shots)
job = backend.run(transpiled_circuit, shots=1000)

# Получаем результаты
result = job.result()
counts = result.get_counts(transpiled_circuit)

# Выводим результаты
print("Результаты: ", counts)
print("""
Объяснение схемы:
1. Hadamard-гейт (H) на кубите q0 создаёт суперпозицию:
2. X-гейт на кубите q1 переводит кубит в состояние |1〉.
3. CNOT-гейт использует кубит q0 как управляющий кубит и кубит q1 как целевой. Он применяет X-гейт к кубиту q1, если кубит q0 находится в состоянии |1〉.
4. В результате измеряются оба кубита, и результаты сохраняются в классические биты.""")
# Визуализируем результаты с помощью гистограммы
plot_histogram(counts)
plt.show()
