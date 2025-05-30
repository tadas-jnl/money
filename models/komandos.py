from dataclasses import dataclass
from models.zurnalas import Zurnalas
import os
def clear():
    os.system('clear')

#  sukurti klasę 'Ataskaita', kuri rodys Pajamas, Išslaidas, Balansą
@dataclass()
class Ataskaita(Zurnalas):
    def __init__(self):
        super().__init__()
    def spauzdinti(self):
        # clear()
        self.pajamos = self.zurnalas[0]
        self.islaidos = self.zurnalas[1]
        self.balansas = sum(self.zurnalas[0]) + sum(self.zurnalas[1])
        len_list = max(len(self.pajamos), len(self.islaidos))
        self.pajamos += [""] * (len_list - len(self.pajamos))
        self.islaidos += [""] * (len_list - len(self.islaidos))
        print(f"\n{'Pajamos':>12} (€)  | {'Išlaidos':>12} (€)")
        print("-" * 38)
        for x, y in zip(self.pajamos, self.islaidos):
            print(f"{str(x):>16}  |  {str(y):>16}")
        print("-" * 38)

        print(f"Balansas: {self.balansas:,.2f} €\n".center(38))
