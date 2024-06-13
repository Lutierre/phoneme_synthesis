import numpy as np

from models.formant import Formant


class Sound:
    def __init__(self, frequency=None, base_frequency=120):
        self.frequency = frequency
        self.base_frequency = base_frequency
        self.signal = np.array([[0][0]])

        # würdet ihr die Formanten als Felder darstellen?
        self.first_formant = Formant()
        self.second_formant = Formant()
        self.third_formant = Formant()





