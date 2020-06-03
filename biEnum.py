from enum import Enum

class transcriptionEquivalent(Enum):

    A = "T"
    G = "C"
    C = "G"
    T = "U"

    def __str__(self):
        return str(self.value)