from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

# Создаем схему scheme1_1 с 2 кубитами и 2 классическими битами
scheme1_1 = QuantumCircuit(2, 2)

# Кубит 0 уже находится в состоянии |0〉, ничего не делаем
# Применяем X-гейт к кубиту 1, чтобы он перешел в состояние |1〉
scheme1_1.x(1)

# Измеряем состояния кубитов и сохраняем результаты в классические биты
scheme1_1.measure([0, 1], [0, 1])

# Визуализируем схему
scheme1_1.draw(output='mpl')

# Транспиляция схемы для указанного backend
backend = Aer.get_backend('qasm_simulator')
transpiled_circuit = transpile(scheme1_1, backend)

# Запуск схемы напрямую с использованием метода run
job = backend.run(transpiled_circuit, shots=500)

# Получение результатов
result = job.result()
counts = result.get_counts(transpiled_circuit)

# Выводим результаты
print("Результаты: ", counts)
print(f"""
В схеме нет случайности, так как она детерминирована:
Кубит 0 всегда в состоянии |0〉.
Кубит 1 всегда в состоянии |1〉 после применения X-гейта.
Все измерения будут показывать 01, что означает, что первый кубит (слева) находится в состоянии |0〉, а второй кубит — в состоянии |1〉.
В словаре 'counts' = {counts}, 10 - перевёрнуто, читается как 01 (10 --> 01 в двоичной системе)
""")