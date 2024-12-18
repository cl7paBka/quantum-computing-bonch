# Код для google colaboratory

!pip uninstall qiskit -y   
!pip uninstall tweedledum -y   
!pip install qiskit==0.43.0   
!pip install tweedledum   
!pip install pylatexenc    
   
from qiskit.circuit.library import PhaseOracle   
   
from qiskit import QuantumCircuit, transpile   
from qiskit.circuit.library import GroverOperator   
from qiskit_aer import AerSimulator   
from qiskit.visualization import plot_histogram   
 
task_content = """p cnf 4 2  
-1 2 -3 4 0  
1 -2 -3 -4 0  
"""   
 
with open("task.txt", "w") as file:  
    file.write(task_content)  
  
oracle = PhaseOracle.from_dimacs_file('task.txt')  
 
display(oracle.draw(output='mpl'))  
   
n = 4   
grover_circuit = QuantumCircuit(n)  
grover_circuit.h(range(n)) 
   
grover_operator = GroverOperator(oracle)   
grover_circuit.append(grover_operator, range(n))  
  
grover_circuit.measure_all()  
  
display(grover_circuit.draw(output='mpl')) 
 
simulator = AerSimulator()  
compiled_circuit = transpile(grover_circuit, simulator)  
result = simulator.run(compiled_circuit, shots=1024).result()  
counts = result.get_counts()  
  
display(plot_histogram(counts))



## Ссылка
https://colab.research.google.com/drive/11p1qJ8dkUBUBMLDmMPYBGPdZllHDRyJe?usp=sharing