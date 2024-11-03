from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Создаем схему scheme1_2 с 1 кубитом и 1 классическим битом
scheme1_2 = QuantumCircuit(1, 1)

# Применяем H-гейт для создания суперпозиции состояния
scheme1_2.h(0)

# Измеряем состояние кубита и сохраняем результат в классический бит
scheme1_2.measure(0, 0)

# Визуализируем схему
scheme1_2.draw(output='mpl')

# Выполним симуляцию с различным количеством shots
shots_list = [1, 2, 8, 1024, 10000]
results = {}

# Инициализируем симулятор
backend = Aer.get_backend('qasm_simulator')

for shots in shots_list:
    # Транспиляция схемы для указанного backend
    transpiled_circuit = transpile(scheme1_2, backend)

    # Запуск схемы напрямую с использованием метода run
    job = backend.run(transpiled_circuit, shots=shots)

    # Получение результатов
    result = job.result()
    counts = result.get_counts(transpiled_circuit)

    # Сохраняем результаты
    results[shots] = counts

    # Визуализация результатов
    print(f"Результаты для {shots} измерений: {counts}")
    plot_histogram(counts)
    plt.show()
