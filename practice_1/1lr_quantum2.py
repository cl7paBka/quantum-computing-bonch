import numpy as np
from kaleidoscope import qsphere

# квантовое состояние пятикубитной системы с пятью компонентами
state = np.zeros(2**5, dtype=complex)

# амплитуды вероятностей для 0, 7, 15, 27 и 30
state[0] = 1/(4*np.sqrt(2))     # амплитуда для состояния 0
state[7] = 1/(2*np.sqrt(2))     # амплитуда для состояния 7
state[15] = 3/(4*np.sqrt(2))    # амплитуда для состояния 15
state[27] = np.sqrt(2)          # амплитуда для состояния 27
state[30] = 1/4                # амплитуда для состояния 30

# визуализирую на Q-сфере в десятичной системе счисления
qsphere(state, state_labels_kind='ints').show()
