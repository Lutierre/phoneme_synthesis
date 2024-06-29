import numpy as np


class Sound:
    def __init__(self, f1_factor, f2_factor, f3_factor, base_frequency=120):
        self.base_frequency = base_frequency
        self.signal = np.array([[0][0]])

        first_formant = f1_factor * base_frequency
        second_formant = f2_factor * base_frequency
        third_formant = f3_factor * base_frequency

        t = np.linspace(0, 1, 500, endpoint=False)

        signal = (np.sin(2 * np.pi * base_frequency * t) + np.sin(2 * np.pi * first_formant * t)
                  + np.sin(2 * np.pi * second_formant * t) + np.sin(2 * np.pi * third_formant * t))