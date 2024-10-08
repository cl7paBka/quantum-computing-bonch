# Импорт необходимых библиотек
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.circuit.library import QFT
import matplotlib.pyplot as plt


# Функция для создания схемы QFT
def qft_circuit(n):
    qc = QuantumCircuit(n)
    qc.append(QFT(n), range(n))  # Добавляем QFT на все кубиты
    qc.barrier()
    return qc


# Функция для создания схемы обратного QFT
def inverse_qft_circuit(n):
    qc = QuantumCircuit(n)
    qc.append(QFT(n, inverse=True), range(n))  # Обратное преобразование Фурье
    qc.barrier()
    return qc


# Функция для тестирования различных входных значений
def test_qft_for_value(value, n_qubits):
    qc = QuantumCircuit(n_qubits)

    # Инициализируем состояние на основе двоичного представления value
    binary_value = format(value, f'0{n_qubits}b')

    # Применяем X-гейты для установки состояния
    for i, bit in enumerate(reversed(binary_value)):
        if bit == '1':
            qc.x(i)
    qc.barrier()

    # Прямое квантовое преобразование Фурье
    qc = qc.compose(qft_circuit(n_qubits))  # Используем compose для объединения схем

    # Обратное квантовое преобразование Фурье
    qc = qc.compose(inverse_qft_circuit(n_qubits))  # Используем compose для обратного QFT

    # Измеряем кубиты
    qc.measure_all()

    # Симуляция схемы
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    result = simulator.run(compiled_circuit).result()

    # Результаты выполнения
    counts = result.get_counts(qc)
    print(f"Результаты измерений для входного значения {value} ({binary_value}): {counts}")

    # Визуализация результатов с помощью matplotlib
    plot_histogram(counts)
    plt.show()


# Функция для вывода анализа результатов
def print_analysis():
    print("Анализ результатов измерений\n")

    print("1. Входные значения и результаты измерений:")
    print("- Входное значение 7 (111) -> результат: {'111': 1024}")
    print("- Входное значение 3 (011) -> результат: {'011': 1024}")
    print("- Входное значение 5 (101) -> результат: {'101': 1024}")
    print("- Входное значение 6 (110) -> результат: {'110': 1024}\n")

    print("2. Прямое и обратное квантовое преобразование Фурье:")
    print("- Прямое квантовое преобразование Фурье (QFT) изменяет амплитуды "
          "состояний в базисе Фурье.")
    print("- Обратное квантовое преобразование Фурье (Inverse QFT) восстанавливает "
          "исходное состояние кубитов.")
    print("- После выполнения обратного преобразования состояние возвращается "
          "в исходный вычислительный базис.\n")

    print("3. Результаты:")
    print("- В каждом случае измеренное состояние полностью совпадает с "
          "исходным значением.")
    print("- Для всех входных значений вероятность получения исходного состояния "
          "составляет 100% (1024 симуляции).\n")

    print("4. Выводы:")
    print("- Прямое и обратное квантовое преобразование Фурье работают корректно "
          "и взаимно обратны друг другу.")
    print("- Квантовое преобразование Фурье изменяет только амплитуды состояния "
          "кубитов.")
    print("- Обратное преобразование Фурье гарантирует восстановление исходного "
          "состояния.\n")

    print("Заключение:")
    print("Эта схема демонстрирует, что амплитуды изменяются в базисе Фурье,")
    print("но после обратного преобразования состояние полностью возвращается "
          "в вычислительный базис.")


# Основной блок программы #
###########################
# Создаем схему для значения 7 (111 в двоичной системе)
n_qubits = 3
qc = QuantumCircuit(n_qubits)

# Инициализируем состояние 7 = 111
qc.x(0)
qc.x(1)
qc.x(2)
qc.barrier()

# Прямое квантовое преобразование Фурье
qc = qc.compose(qft_circuit(n_qubits))

# Обратное квантовое преобразование Фурье
qc = qc.compose(inverse_qft_circuit(n_qubits))

# Измеряем кубиты
qc.measure_all()

# Симуляция схемы
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
result = simulator.run(compiled_circuit).result()

# Результаты выполнения
counts = result.get_counts(qc)
print("Результаты измерений:", counts)

# Визуализация результатов с помощью matplotlib
plot_histogram(counts)
plt.show()  # Отображаем гистограмму с помощью matplotlib

# Тестируем для значений 3, 5 и 6
test_values = [3, 5, 6]
for value in test_values:
    test_qft_for_value(value, n_qubits)

# Вывод анализа
print_analysis()
