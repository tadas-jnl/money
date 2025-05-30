import pickle

class Zurnalas:
    def __init__(self):
        try:
            with open("biudzetas.pkl", "rb") as file:
                self.zurnalas = pickle.load(file)
        except (FileNotFoundError, EOFError):
            self.zurnalas = [[], []]

    def irasyti(self, irasas):
        try:
            irasas = float(irasas)
            if irasas > 0: self.zurnalas[0].append(irasas)
            elif irasas < 0: self.zurnalas[1].append(irasas)
            else: pass
        except (ValueError, TypeError) as err:
            print(f"Neteisingai įvesta suma: {err}")

        with open("biudzetas.pkl", "wb") as file:
            pickle.dump(self.zurnalas, file)




