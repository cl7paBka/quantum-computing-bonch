# Задача 1: Импорт библиотек
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
from matplotlib import pyplot as plt


# Задача 2: Реализация схемы оценки фазы

# Реализация QFT
def qft(circuit, n):
    """
    Добавляет обратное квантовое преобразование Фурье (QFT) в схему.
    circuit: квантовая схема, куда добавляется QFT
    n: число кубитов для применения QFT
    """
    for qubit in range(n):
        circuit.h(qubit)
        for other_qubit in range(qubit + 1, n):
            circuit.cp(np.pi / 2 ** (other_qubit - qubit), other_qubit, qubit)

    # Разворот кубитов в конце
    for qubit in range(n // 2):
        circuit.swap(qubit, n - qubit - 1)


# Реализация схемы оценки фазы
def phase_estimation_circuit(theta, num_qubits=6):
    """
    Строит квантовую схему для оценки фазы с использованием контролируемых P-гейтов и обратного преобразования Фурье.
    theta: фаза, которую нужно оценить
    num_qubits: число управляющих кубитов (по умолчанию 6)
    """
    qc = QuantumCircuit(num_qubits + 1, num_qubits)  # 6 управляющих кубитов и 1 вспомогательный

    # Применение Х-гейта к состоянию |1> на вспомогательном кубите (q6)
    qc.x(num_qubits)

    # Применение Hadamard-гейтов ко всем управляющим кубитам (q0, q1, ..., q5)
    for qubit in range(num_qubits):
        qc.h(qubit)

    # Применение контролируемых P-гейтов с разными степенями фаз для каждого управляющего кубита
    for qubit in range(num_qubits):
        exponent = 2 ** qubit  # Степени 2: 1, 2, 4, 8, 16, 32
        qc.cp(2 * np.pi * theta / exponent, qubit, num_qubits)  # P(2pi * theta / exponent)

    # Применение обратного квантового преобразования Фурье (QFT) для управляющих кубитов
    qft(qc, num_qubits)

    # Измерение управляющих кубитов (q0 - q5)
    qc.measure(range(num_qubits), range(num_qubits))

    return qc


# Пример создания схемы для theta = 1/3
theta = 1 / 3
qc = phase_estimation_circuit(theta)

# Отрисовка схемы с помощью matplotlib
qc.draw('mpl')
plt.show()

# Пример создания схемы для theta = 1/3
theta = 1 / 3
qc = phase_estimation_circuit(theta)
qc.draw('mpl')  # Для отрисовки схемы


# Задача 3: Проведение экспериментов для различных значений фазы

def run_experiments(thetas, num_qubits=6):
    """
    Выполняет симуляцию схемы оценки фазы для различных значений theta.
    thetas: список фаз для тестирования
    num_qubits: число управляющих кубитов (по умолчанию 6)
    """
    # Создаем симулятор
    simulator = AerSimulator()

    # Выполняем симуляцию для каждого значения theta
    for theta in thetas:
        # Создание схемы
        qc = phase_estimation_circuit(theta, num_qubits)

        # Транспиляция схемы для симулятора
        compiled_circuit = transpile(qc, simulator)

        # Запуск симуляции
        result = simulator.run(compiled_circuit).result()

        # Получение результатов измерений
        counts = result.get_counts(qc)

        # Печать результатов
        print(f"Theta: {theta}")
        plot_histogram(counts)


thetas = [1 / 2, 1 / 3, 1 / 4, 1 / 6, 1 / 8, 1 / 12, 1 / 16, 1 / 32, 1 / 64]
run_experiments(thetas)


# Задача 4: Вычисление оценки фазы

def calculate_phase_estimation(counts, num_qubits):
    """
    Вычисляет оценку фазы, используя результат измерений.
    counts: словарь с результатами измерений
    num_qubits: число управляющих кубитов
    """
    # Найдем состояние с максимальной амплитудой
    max_state = max(counts, key=counts.get)

    # Преобразование состояния в десятичное значение
    decimal = int(max_state, 2) / (2 ** num_qubits)

    return decimal


def analyze_results(thetas, num_qubits=6):
    """
    Выполняет симуляцию, оценивает фазы и считает процентное отклонение.
    thetas: список фаз для тестирования
    num_qubits: число управляющих кубитов
    """
    simulator = AerSimulator()

    for theta in thetas:
        # Создание и компиляция схемы
        qc = phase_estimation_circuit(theta, num_qubits)
        compiled_circuit = transpile(qc, simulator)

        # Запуск симуляции
        result = simulator.run(compiled_circuit).result()
        counts = result.get_counts(qc)

        # Оценка фазы
        estimated_phase = calculate_phase_estimation(counts, num_qubits)
        error = abs(estimated_phase - theta) / theta * 100

        # Вывод результатов
        print(f"Theta: {theta}, Estimated Phase: {estimated_phase}, Error: {error:.2f}%")


analyze_results(thetas)


# Задача 5: Оценка фазы для θ = 1/128 и θ = 1/1024

def estimate_large_phases():
    """
    Выполняет оценку фаз для θ = 1/128 и θ = 1/1024 с увеличенным количеством управляющих кубитов (10).
    """
    simulator = AerSimulator()

    # Увеличение числа управляющих кубитов до 10
    qc_128 = phase_estimation_circuit(1 / 128, num_qubits=10)
    qc_1024 = phase_estimation_circuit(1 / 1024, num_qubits=10)

    # Транспиляция и запуск схемы для θ = 1/128
    compiled_128 = transpile(qc_128, simulator)
    result_128 = simulator.run(compiled_128).result()
    counts_128 = result_128.get_counts(qc_128)
    estimated_phase_128 = calculate_phase_estimation(counts_128, 10)

    # Транспиляция и запуск схемы для θ = 1/1024
    compiled_1024 = transpile(qc_1024, simulator)
    result_1024 = simulator.run(compiled_1024).result()
    counts_1024 = result_1024.get_counts(qc_1024)
    estimated_phase_1024 = calculate_phase_estimation(counts_1024, 10)

    # Вывод результатов
    print(f"Estimated Phase for θ = 1/128: {estimated_phase_128}")
    print(f"Estimated Phase for θ = 1/1024: {estimated_phase_1024}")


estimate_large_phases()
