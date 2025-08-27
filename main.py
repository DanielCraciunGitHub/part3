from qiskit import QuantumCircuit
from qiskit.circuit.library import HGate, MCXGate
import matplotlib.pyplot as plt

def main() -> None:
    mcx_gate = MCXGate(3)
    hadamard_gate = HGate()
    print(hadamard_gate)
    qc = QuantumCircuit(4)
    qc.append(hadamard_gate, [0])
    qc.append(mcx_gate, [0, 1, 2, 3])
    
    qc.draw("mpl")
    plt.show()
    

if __name__ == "__main__":
    main()
